from datetime import datetime
from app.utils.hash import verify_password
from app.db.database import db
from app.utils.jwt import create_token
from app.services.email_service import send_email
from app.utils.vendor_Code_Creation import generate_vendor_code


vendor_collection = db["vendors"]


def generate_vendor_id():
    count = vendor_collection.count_documents({})
    return f"VEND{1000 + count + 1}"


# def create_vendor(data: dict):
#     vendor_id = generate_vendor_id()

#     vendor_data = {
#         "vendor_id": vendor_id,
#         "company_details": data["company_details"],
#         "contact_details": data["contact_details"],
#         "location_details": data["location_details"],
#         "financial_details": data["financial_details"],
#         "online_presence": data.get("online_presence"),
#         "status": "PENDING",  # important for approval flow
#         "vendor_code":"",
#         "code_sent": False,
#         "created_at": datetime.utcnow()
#     }

#     result = vendor_collection.insert_one(vendor_data)
#     vendor_data["_id"] = str(result.inserted_id)

#     return vendor_data


# def create_vendor(data: dict):
#     vendor_id = generate_vendor_id()

#     vendor_data = {
#         "vendor_id": vendor_id,

#         # 🔹 Legal Info
#         "legal_details": {
#             "legal_entity_name": data["legal_details"]["legal_entity_name"],
#             "business_structure": data["legal_details"]["business_structure"],
#             "pan_number": data["legal_details"]["pan_number"],
#             "gstin": data["legal_details"]["gstin"],
#             "registered_address": data["legal_details"]["registered_address"],
#             "communication_address": data["legal_details"]["communication_address"],
#         },

#         # 🔹 Contact Info
#         "contact_details": {
#             "primary_contact_person": data["contact_details"]["primary_contact_person"],
#             "secondary_contact_person": data["contact_details"].get("secondary_contact_person"),
#             "email": data["contact_details"]["email"],
#             "mobile_number": data["contact_details"]["mobile_number"],
#         },

#         # 🔹 Bank Details
#         "bank_details": {
#             "bank_name": data["bank_details"]["bank_name"],
#             "account_number": data["bank_details"]["account_number"],
#             "ifsc_code": data["bank_details"]["ifsc_code"],
#             "swift_code": data["bank_details"].get("swift_code"),
#             "cancelled_cheque_file": data["bank_details"].get("cancelled_cheque_file"),
#         },

#         # 🔹 Documents
#         "documents": {
#             "pan_card": data["documents"].get("pan_card"),
#             "gst_certificate": data["documents"].get("gst_certificate"),
#             "incorporation_certificate": data["documents"].get("incorporation_certificate"),
#             "msme_certificate": data["documents"].get("msme_certificate"),
#             "cancelled_cheque": data["documents"].get("cancelled_cheque"),
#             "address_proof": data["documents"].get("address_proof"),
#             "iatf_iso_certificate": data["documents"].get("iatf_iso_certificate"),
#             "quality_certifications": data["documents"].get("quality_certifications"),
#             "stellantis_docs": data["documents"].get("stellantis_docs"),
#         },

#         # 🔹 Compliance
#         "compliance": {
#             "anti_bribery": data["compliance"].get("anti_bribery", False),
#             "conflict_of_interest": data["compliance"].get("conflict_of_interest", False),
#             "esg": data["compliance"].get("esg"),
#             "pf_esi_details": data["compliance"].get("pf_esi_details"),
#             "code_of_conduct_accepted": data["compliance"].get("code_of_conduct_accepted", False),
#         },

#         # 🔹 Existing fields
#         "status": "PENDING",
#         "vendor_code": "",
#         "code_sent": False,
#         "created_at": datetime.utcnow()
#     }

#     result = vendor_collection.insert_one(vendor_data)
#     vendor_data["_id"] = str(result.inserted_id)

#     return vendor_data

import json
from datetime import datetime
from app.utils.cloudinary_upload import upload_file

from app.utils.s3_upload import upload_file_s3

# async def create_vendor(
#     legal_details,
#     contact_details,
#     bank_details,
#     compliance,
#     pan_card,
#     gst_certificate,
#     cancelled_cheque,
#     address_proof,
#     iso_certificate
# ):
#     # Convert JSON string → dict
#     legal_details = json.loads(legal_details)
#     contact_details = json.loads(contact_details)
#     bank_details = json.loads(bank_details)
#     compliance = json.loads(compliance)

#     # Upload files to Cloudinary
#     pan_url = upload_file(pan_card)
#     gst_url = upload_file(gst_certificate)
#     cheque_url = upload_file(cancelled_cheque)
#     address_url = upload_file(address_proof)
#     iso_url = upload_file(iso_certificate) if iso_certificate else None

#     vendor_data = {
#         "vendor_id": generate_vendor_id(),

#         "legal_details": legal_details,
#         "contact_details": contact_details,
#         "bank_details": bank_details,
#         "compliance": compliance,

#         "documents": {
#             "pan_card": pan_url,
#             "gst_certificate": gst_url,
#             "cancelled_cheque": cheque_url,
#             "address_proof": address_url,
#             "iso_certificate": iso_url
#         },

#         "status": "PENDING",
#         "vendor_code": "",
#         "code_sent": False,
#         "created_at": datetime.utcnow()
#     }

#     vendor_collection.insert_one(vendor_data)

#     return {"message": "Vendor Registered Successfully"}


async def create_vendor(
    legal_details,
    contact_details,
    bank_details,
    compliance,
    pan_card,
    gst_certificate,
    cancelled_cheque,
    address_proof,
    iso_certificate
):

    import json
    from datetime import datetime

    # ✅ Convert JSON

    legal_details = json.loads(legal_details)
    contact_details = json.loads(contact_details)
    bank_details = json.loads(bank_details)
    compliance = json.loads(compliance)



    # ✅ Upload to S3
    pan_url = upload_file_s3(pan_card, "vendors/docs")
    gst_url = upload_file_s3(gst_certificate, "vendors/docs")
    cheque_url = upload_file_s3(cancelled_cheque, "vendors/docs")
    address_url = upload_file_s3(address_proof, "vendors/docs")
    iso_url = upload_file_s3(iso_certificate, "vendors/docs") if iso_certificate else None

    vendor_data = {
        "vendor_id": generate_vendor_id(),

        "legal_details": legal_details,
        "contact_details": contact_details,
        "bank_details": bank_details,
        "compliance": compliance,

        "documents": {
            "pan_card": pan_url,
            "gst_certificate": gst_url,
            "cancelled_cheque": cheque_url,
            "address_proof": address_url,
            "iso_certificate": iso_url
        },

        "status": "PENDING",
        "vendor_code": "",
        "code_sent": False,
        "created_at": datetime.utcnow()
    }

    vendor_collection.insert_one(vendor_data)

    return {"message": "Vendor Registered Successfully"}




def get_all_vendors():
    vendors = list(vendor_collection.find())
    for v in vendors:
        v["_id"] = str(v["_id"])
    return vendors

from datetime import datetime

PENDING = "PENDING"
APPROVED = "APPROVED"
REJECTED = "REJECTED"


def get_pending_vendors():
    vendors = list(vendor_collection.find({"status": PENDING}))
    for v in vendors:
        v["_id"] = str(v["_id"])
    return vendors


def approve_vendor(vendor_id: str, admin_id: str = "admin"):
    vendor = vendor_collection.find_one({"vendor_id": vendor_id})

    if not vendor:
        return {"error": "Vendor not found"}

    if vendor["status"] == APPROVED:
        return {"message": "Vendor already approved"}

    if vendor["status"] == REJECTED:
        return {"error": "Rejected vendor cannot be approved directly"}

    vendor_collection.update_one(
        {"vendor_id": vendor_id},
        {"$set": {
            "status": APPROVED,
            "approved_at": datetime.utcnow(),
            "approved_by": admin_id
        }}
    )

    return {"message": "Vendor approved successfully"}

def reject_vendor(vendor_id: str, reason: str = "Not specified", admin_id: str = "admin"):
    vendor = vendor_collection.find_one({"vendor_id": vendor_id})

    if not vendor:
        return {"error": "Vendor not found"}

    if vendor["status"] == REJECTED:
        return {"message": "Vendor already rejected"}

    vendor_collection.update_one(
        {"vendor_id": vendor_id},
        {"$set": {
            "status": REJECTED,
            "rejected_at": datetime.utcnow(),
            "rejected_by": admin_id,
            "rejection_reason": reason
        }}
    )

    return {"message": "Vendor rejected successfully"}




# async def login_vendor(data):
#     vendor = vendor_collection.find_one({
#         "contact_details.email": data.email
#     })

#     if not vendor:
#         return {"error": "Vendor not found"}

#     if vendor.get("status") != "APPROVED":
#         return {"error": "Vendor not approved by admin"}

#     if data.password != vendor['contact_details']['phone_number']:
#         return {"error": "Invalid password"}

#     # ✅ Create token
#     token = create_token({
#         "id": str(vendor["_id"]),
#         "email": vendor["contact_details"]["email"],
#         "vendor_id": vendor["vendor_id"]
#     })

#     # ✅ SEND EMAIL ONLY ONCE
#     if not vendor.get("code_sent", False):
#         email = vendor["contact_details"]["email"]
#         # vendor_code = vendor.get("vendor_code", "TIAPL/SC/001")  # fallback

#         vendor_code = generate_vendor_code()

#         await send_email(
#             email,
#             vendor_code
#         )

#         # ✅ Update DB
#         vendor_collection.update_one(
#            {"_id": vendor["_id"]},
#            {
#               "$set": {
#                  "code_sent": True,
#                  "vendor_code": vendor_code   # ✅ store code here
#                }
#             }
#     )

#     return {
#         "token": token,
#         "vendor_id": vendor["vendor_id"],
#         "email": vendor["contact_details"]["email"],
#         "company_name": vendor["company_details"]["company_name"]
#     }


async def login_vendor(data):
    vendor = vendor_collection.find_one({
        "contact_details.email": data.email
    })

    if not vendor:
        return {"error": "Vendor not found"}

    if vendor.get("status") != "APPROVED":
        return {"error": "Vendor not approved by admin"}

    # ✅ FIXED FIELD
    if data.password != vendor['contact_details']['phone_number']:
        return {"error": "Invalid password"}

    token = create_token({
        "id": str(vendor["_id"]),
        "email": vendor["contact_details"]["email"],
        "vendor_id": vendor["vendor_id"]
    })

    if not vendor.get("code_sent", False):
        email = vendor["contact_details"]["email"]
        vendor_code = generate_vendor_code()

        await send_email(email, vendor_code,vendor["legal_details"]["legal_entity_name"])

        vendor_collection.update_one(
            {"_id": vendor["_id"]},
            {
                "$set": {
                    "code_sent": True,
                    "vendor_code": vendor_code
                }
            }
        )

    return {
        "token": token,
        "id": str(vendor["_id"]),   # ✅ FIX HERE
        "vendor_id": vendor["vendor_id"],
        "email": vendor["contact_details"]["email"],
        "company_name": vendor["legal_details"]["legal_entity_name"]  # ✅ FIXED
    }


from app.db.database import requirement_collection 
def vendorSee_AllRequerments():
    print("Hello from service")
    
    requi_cursor = requirement_collection.find()
    requi_list = list(requi_cursor)

    if not requi_list:
        return {"error": "No requirements found"}

    # Convert ObjectId to string
    for item in requi_list:
        item["_id"] = str(item["_id"])

    return requi_list


def vendor_Add_Product():
    print("Hello from service")