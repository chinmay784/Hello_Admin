from pydantic import BaseModel
from typing import List, Dict, Optional

class ProductCreate(BaseModel):
    product_name: str
    category: str
    sub_category: Optional[str]
    brand: Optional[str]
    model_number: Optional[str]
    price: float
    quantity_available: int
    minimum_order_quantity: int
    description: str
    specifications: Dict   # dynamic
    features: List[str]