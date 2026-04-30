
# from fastapi import APIRouter
# from app.db.database import db
# from bson import ObjectId

# router = APIRouter(prefix="/branches", tags=["Branches"])


# # CREATE BRANCH
# @router.post("/")
# def create_branch(name: str, location: str, company_id: str):
#     branch = {
#         "name": name,
#         "location": location,
#         "company_id": company_id
#     }

#     result = db["branches"].insert_one(branch)
#     branch["_id"] = str(result.inserted_id)

#     return branch


# # GET ALL BRANCHES
# @router.get("/")
# def get_branches():
#     branches = []

#     for branch in db["branches"].find():
#         branch["_id"] = str(branch["_id"])
#         branches.append(branch)

#     return branches


# # DELETE BRANCH
# @router.delete("/{branch_id}")
# def delete_branch(branch_id: str):
#     result = db["branches"].delete_one({"_id": ObjectId(branch_id)})

#     if result.deleted_count == 0:
#         return {"error": "Branch not found"}

#     return {"message": "Deleted successfully"}








from fastapi import APIRouter, HTTPException,Depends
from bson import ObjectId
from app.db.database import db
from app.models.branch import BranchCreateSchema 
from app.schemas.branch_schema import BranchByCompany
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/branches", tags=["Branches"])


# ✅ CREATE BRANCH
@router.post("/")
def create_branch(
    data: BranchCreateSchema,
    current_user=Depends(get_current_user)
):
    try:
        company = db["companies"].find_one({"_id": ObjectId(data.company_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid company_id")

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    branch = {
        "name": data.name,
        "location": data.location,
        "company_id": ObjectId(data.company_id)
    }

    result = db["branches"].insert_one(branch)

    return {
        "_id": str(result.inserted_id),
        "name": data.name,
        "location": data.location,
        "company_id": data.company_id
    }


# # ✅ GET ALL BRANCHES

@router.post("/get-by-company")
def get_branches(
    data: BranchByCompany,
    current_user=Depends(get_current_user)
):
    try:
        company_id = ObjectId(data.company_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid company_id")

    branches = []

    for branch in db["branches"].find({"company_id": company_id}):
        branches.append({
            "_id": str(branch["_id"]),
            "name": branch.get("name"),
            "location": branch.get("location"),
            "company_id": str(branch.get("company_id"))
        })

    return {"branches": branches}



# ✅ DELETE BRANCH
@router.delete("/{branch_id}")
def delete_branch(branch_id: str, current_user=Depends(get_current_user)):
    try:
        result = db["branches"].delete_one({"_id": ObjectId(branch_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid branch_id format")

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Branch not found")

    return {"message": "Deleted successfully"}