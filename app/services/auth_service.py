from app.db.database import users_collection
from app.utils.hash import hash_password, verify_password
from app.utils.jwt import create_token


# REGISTER
def register_user(data):
    existing = users_collection.find_one({"email": data.email})

    if existing:
        return {"error": "User already exists"}

    hashed_pw = hash_password(data.password)

    user = {
        "name": data.name,
        "email": data.email,
        "password": hashed_pw,
        "role": "admin"
    }

    users_collection.insert_one(user)

    return {"message": "User registered successfully"}


# LOGIN
def login_user(data):
    user = users_collection.find_one({"email": data.email})

    if not user:
        return {"error": "User not found"}

    if not verify_password(data.password, user["password"]):
        return {"error": "Invalid password"}

    token = create_token({
        "id": str(user["_id"]),
        "email": user["email"],
        "role": user["role"]
    })

    return {"token": token,"user":user["email"], "role": user["role"],"name": user["name"]}


# from app.db.database import users_collection

# def register_user(data):
#     users_collection.insert_one(data)
#     return {"message": "User registered"}

from app.db.database import db
from app.core.hash import verify_password
from app.core.security import create_access_token

vendor_collection = db["vendors"]


def vendor_login(email: str, password: str):
    vendor = vendor_collection.find_one({
        "contact_details.email": email
    })

    # ❌ email not found
    if not vendor:
        return {"error": "Invalid email or password"}

    # ❌ not approved (IMPORTANT as per your workflow)
    if vendor["status"] != "APPROVED":
        return {"error": "Vendor not approved by admin"}

    # ❌ wrong password
    if not verify_password(password, vendor["password"]):
        return {"error": "Invalid email or password"}

    # ✅ create token
    token = create_access_token({
        "vendor_id": vendor["vendor_id"],
        "role": "vendor"
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "vendor_id": vendor["vendor_id"]
    }