from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    name: str
    branch_id: str

class DepartmentByBranch(BaseModel):
    branch_id: str