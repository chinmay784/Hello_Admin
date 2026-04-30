from fastapi import APIRouter, Depends
from app.models.requirement_model import Requirement
from app.db.database import requirement_collection ,vendor_collection

router = APIRouter(prefix="/requirement", tags=["requirement"])

@router.post("/create-requirement")
def create_requirement(req: Requirement):
    requirement_collection.insert_one(req.dict())
    return {"message": "Requirement created successfully"}

@router.get("/vendor/requirements")
def get_all_requirements():
    requirements = list(requirement_collection.find({"status": "open"}))
    
    for r in requirements:
        r["_id"] = str(r["_id"])  # convert ObjectId
    
    return requirements

@router.get("/vendor/requirements")
def get_requirements(category: str = None):

    query = {"status": "open"}
    
    if category:
        query["category"] = category

    requirements = list(requirement_collection.find(query))
    
    for r in requirements:
        r["_id"] = str(r["_id"])

    return requirements




@router.get("/See-requirements")
def get_all_requirements():
    requirements = list(requirement_collection.find())

    if not requirements:
        return {"message": "No requirements found"}
    
    
    for r in requirements:
        r["_id"] = str(r["_id"])
    
    return requirements


from bson import ObjectId
# Procurement team can see all Vendor Approve Requirements
@router.get("/see-all-Vendor-Approve-requirements")
def see_all_vendor_approve_requirements(requirement_id: str):
    requirement = requirement_collection.find_one({"_id": ObjectId(requirement_id)})

    if not requirement:
        return {"message": "No approved requirements found"}

    # ✅ FIX: Convert ObjectId to string
    requirement["_id"] = str(requirement["_id"])

    vendor_ids = requirement.get("ApproveVendor_ids", [])

    if not vendor_ids:
        return {"message": "No vendors approved yet"}

    # ✅ Fetch vendors using vendor_id
    vendors = list(vendor_collection.find({
        "vendor_id": {"$in": vendor_ids}
    }))

    # ✅ Convert ObjectId
    for v in vendors:
        v["_id"] = str(v["_id"])

    return {
        "requirement_id": requirement["_id"],
        "approved_vendors": vendors
    }