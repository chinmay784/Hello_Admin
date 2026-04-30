from fastapi import APIRouter, HTTPException
import datetime
from app.schemas.procearTeam_Requirments_schema import RequirementCreate
from app.db.database import procurement_collection

router = APIRouter(prefix="/procurement", tags=["procurement"])


@router.post("/create")
def create_requirement(data: RequirementCreate):

    # ✅ Validations
    if not data.component_name:
        raise HTTPException(status_code=400, detail="Component name is required")

    if data.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    if not data.specifications:
        raise HTTPException(status_code=400, detail="Specifications required")

    if not data.required_delivery_date:
        raise HTTPException(status_code=400, detail="Delivery date required")

    # ✅ Save in DB
    new_requirement = {
        "component_name": data.component_name,
        "quantity": data.quantity,
        "specifications": data.specifications,
        "required_delivery_date": str(data.required_delivery_date),
        "status": "PENDING",  # default
        "created_at": datetime.datetime.utcnow()
    }

    result = procurement_collection.insert_one(new_requirement)

    return {
        "success": True,
        "message": "Requirement created successfully",
        "requirement_id": str(result.inserted_id)
    }