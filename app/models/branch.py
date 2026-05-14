# from sqlalchemy import Column, Integer, String, ForeignKey
# from app.db.database import Base

# class Branch(Base):
#     __tablename__ = "branches"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     location = Column(String)
#     company_id = Column(Integer, ForeignKey("companies.id"))




from pydantic import BaseModel

class BranchCreateSchema(BaseModel):
    name: str
    location: str
    lattitude: float
    longitude: float
    radius: float
    company_id: str