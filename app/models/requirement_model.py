from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Requirement(BaseModel):
    title: str
    description: str
    quantity: int
    product_Name: str
    category: str
    company_Name: str
    status: str = "open"
    created_at: datetime = datetime.utcnow()

    # ✅ New field (array of IDs)
    ApproveVendor_ids: List[str] = []   # or Optional[List[str]] = None