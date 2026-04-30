from app.utils.db_helpers import create_company
from app.db.database import company_collection

def create_company_controller(data):
    company_data = data.dict()
    create_company(company_data)
    return {"message": "Company onboarded successfully"}

def get_companies_controller():
    companies = list(company_collection.find())

    for company in companies:
        company["_id"] = str(company["_id"])   # ✅ FIX

    if len(companies) == 0:
        return {"message": "No companies found"}

    return {"companies": companies}
