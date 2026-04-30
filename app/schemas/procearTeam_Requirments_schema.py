from pydantic import BaseModel
from datetime import date

class RequirementCreate(BaseModel):
    component_name: str
    quantity: int
    specifications: str
    required_delivery_date: date