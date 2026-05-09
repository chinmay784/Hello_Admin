from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    name: str
    branch_id: str

class DepartmentByBranch(BaseModel):
    branch_id: str




# ✅ UPDATE DEPARTMENT HEAD
class UpdateDepartmentHead(BaseModel):
    head_id: str
    head_name: str
    head_email: str
    head_mobileno: str