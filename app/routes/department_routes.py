from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from app.db.database import db
from app.schemas.department_schema import DepartmentCreate, DepartmentByBranch
from app.utils.dependencies import get_current_user   # your auth middleware

router = APIRouter(prefix="/departments", tags=["Departments"])


# ✅ CREATE DEPARTMENT (only logged-in user)
@router.post("/create")
def create_department(
    data: DepartmentCreate,
    current_user=Depends(get_current_user)
):
    try:
        branch_id = ObjectId(data.branch_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid branch_id")

    department = {
        "name": data.name,
        "branch_id": branch_id
    }

    result = db["departments"].insert_one(department)

    return {
        "message": "Department created",
        "id": str(result.inserted_id)
    }


# ✅ GET DEPARTMENTS BY BRANCH
@router.post("/get-by-branch")
def get_departments(
    data: DepartmentByBranch,
    current_user=Depends(get_current_user)
):
    try:
        branch_id = ObjectId(data.branch_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid branch_id")

    departments = []

    for dept in db["departments"].find({"branch_id": branch_id}):
        departments.append({
            "_id": str(dept["_id"]),
            "name": dept.get("name"),
            "branch_id": str(dept.get("branch_id"))
        })

    return {"departments": departments}


# ✅ DELETE DEPARTMENT
@router.delete("/{department_id}")
def delete_department(
    department_id: str,
    current_user=Depends(get_current_user)
):
    try:
        dept_id = ObjectId(department_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid ID")

    result = db["departments"].delete_one({"_id": dept_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Department not found")

    return {"message": "Deleted successfully"}