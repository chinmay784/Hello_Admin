# from pydantic import BaseModel

# class BranchCreate(BaseModel):
#     name: str
#     location: str

# class BranchResponse(BaseModel):
#     id: int
#     name: str
#     location: str

#     class Config:
#         orm_mode = True
        



from pydantic import BaseModel

# ✅ Create Branch
class BranchCreate(BaseModel):
    name: str
    location: str
    company_id: str   # 🔥 required

# ✅ Get Branch by Company
class BranchByCompany(BaseModel):
    company_id: str

# ✅ Response Schema
class BranchResponse(BaseModel):
    _id: str
    name: str
    location: str
    company_id: str


class BranchByCompany(BaseModel):
    company_id: str