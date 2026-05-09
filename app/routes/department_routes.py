from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from app.db.database import db
from app.schemas.department_schema import DepartmentCreate, DepartmentByBranch
from app.utils.dependencies import get_current_user   # your auth middleware
from app.schemas.department_schema import UpdateDepartmentHead
from app.db.database import depertment_Head_collection

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









@router.put("/assign-head/{department_id}")
def assign_department_head(
    department_id: str,
    data: UpdateDepartmentHead
):

    try:
        dept_id = ObjectId(department_id)
        head_id = ObjectId(data.head_id)

    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid ID"
        )

    # check department exists
    department = db["departments"].find_one({
        "_id": dept_id
    })

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    # check user exists
    # user = db["adminUsers"].find_one({
    #     "_id": head_id
    # })

    # if not user:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="User not found"
    #     )

    # update head_id
    db["departments"].update_one(
        {"_id": dept_id},
        {
            "$set": {
                "head_id": head_id
            }
        }
    )

    # and also do in or create depertment_head collections
    depertment_Head_collection.update_one(
        {"department_id": dept_id},
        {
            "$set": {
                "department_id": dept_id,
                "head_id": head_id,
                "head_name": data.head_name,
                "head_email": data.head_email,
                "head_mobileno": data.head_mobileno
            }
        },
        upsert=True
    )


    return {
        "message": "Department head assigned successfully"
    }


