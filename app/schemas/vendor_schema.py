# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from datetime import datetime


# class CompanyDetails(BaseModel):
#     company_name: str
#     business_type: str  # Manufacturer / Supplier / Distributor
#     gst_number: str
#     pan_number: str
#     certifications: Optional[str]


# class ContactDetails(BaseModel):
#     contact_person_name: str
#     email: EmailStr
#     phone_number: str
#     alternate_phone_number: Optional[str]


# class LocationDetails(BaseModel):
#     address: str
#     city: str
#     state: str
#     country: str
#     pin_code: str


# class FinancialDetails(BaseModel):
#     payment_terms: str
#     bank_account_details: str


# class OnlinePresence(BaseModel):
#     website: Optional[str]


# # class VendorCreate(BaseModel):
# #     company_details: CompanyDetails
# #     contact_details: ContactDetails
# #     location_details: LocationDetails
# #     financial_details: FinancialDetails
# #     online_presence: Optional[OnlinePresence]

# class VendorCreate(BaseModel):
#     legal_details: dict
#     contact_details: dict
#     bank_details: dict
#     documents: dict
#     compliance: dict


# class VendorResponse(VendorCreate):
#     vendor_id: str
#     status: str
#     created_at: datetime

# from pydantic import BaseModel
# from typing import Optional


# class VendorRejectRequest(BaseModel):
#     reason: Optional[str] = "Not specified"    



# class VendorLogin(BaseModel):
#     email: str
#     password: str



from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# 🔹 Legal / Company Details (Rename for clarity)
class LegalDetails(BaseModel):
    legal_entity_name: str
    business_structure: str
    pan_number: str
    gstin: str
    registered_address: str
    communication_address: str


# 🔹 Contact
class ContactDetails(BaseModel):
    primary_contact_person: str
    secondary_contact_person: Optional[str]
    email: EmailStr
    mobile_number: str


# 🔹 Bank
class BankDetails(BaseModel):
    bank_name: str
    account_number: str
    ifsc_code: str
    swift_code: Optional[str]


# 🔹 Documents
class Documents(BaseModel):
    pan_card: Optional[str]
    gst_certificate: Optional[str]
    incorporation_certificate: Optional[str]
    msme_certificate: Optional[str]
    cancelled_cheque: Optional[str]
    address_proof: Optional[str]
    iatf_iso_certificate: Optional[str]
    quality_certifications: Optional[str]
    stellantis_docs: Optional[str]


# 🔹 Compliance
class Compliance(BaseModel):
    anti_bribery: Optional[bool] = False
    conflict_of_interest: Optional[bool] = False
    esg: Optional[str]
    pf_esi_details: Optional[str]
    code_of_conduct_accepted: Optional[bool] = False


# 🔹 FINAL MODEL (IMPORTANT)
class VendorCreate(BaseModel):
    legal_details: LegalDetails
    contact_details: ContactDetails
    bank_details: BankDetails
    documents: Documents
    compliance: Compliance


class VendorResponse(VendorCreate):
    vendor_id: str
    status: str
    created_at: datetime


class VendorLogin(BaseModel):
    email: str
    password: str


class VendorRejectRequest(BaseModel):
    reason: Optional[str] = "Not specified" 