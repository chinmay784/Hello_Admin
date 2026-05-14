from pydantic import BaseModel

class CompanyInfo(BaseModel):
    companyName: str
    legalName: str
    companyType: str
    industry: str
    yearOfIncorporation: str
    numberOfEmployees: str


class Address(BaseModel):
    registeredAddress: str
    operationalAddress: str
    city: str
    state: str
    country: str
    pinCode: str
    # lattitude: str
    # longitude: str


class Contact(BaseModel):
    email: str
    phone: str
    website: str


class AuthorizedPerson(BaseModel):
    fullName: str
    designation: str
    email: str
    phone: str
    idProofNumber: str


class BankDetails(BaseModel):
    bankName: str
    accountHolderName: str
    accountNumber: str
    ifscCode: str
    branchName: str


class TaxInformation(BaseModel):
    pan: str
    gst: str
    cin: str
    tan: str


class CompanySchema(BaseModel):
    companyInfo: CompanyInfo
    address: Address
    contact: Contact
    authorizedPerson: AuthorizedPerson
    bankDetails: BankDetails
    taxInformation: TaxInformation