# from fastapi import APIRouter
# from app.schemas.auth_schema import RegisterSchema, LoginSchema
# from app.controllers.auth_controller import register_controller, login_controller
# from app.utils.db_helpers import get_user_by_email, get_user_by_token, update_user
# from app.utils.hash import hash_password

# router = APIRouter(prefix="/auth", tags=["Auth"])

# @router.post("/register")
# def register(data: RegisterSchema):
#     return register_controller(data)

# @router.post("/login")
# def login(data: LoginSchema):
#     return login_controller(data)

# from fastapi import APIRouter, HTTPException
# from app.schemas.password_schema import ForgotPasswordSchema, ResetPasswordSchema
# from app.utils.token import generate_reset_token
# from app.utils.email import send_reset_email
# # from app.utils.db_helpers import get_user_by_email, get_user_by_token, save_user, hash_password
# from app.utils.db_helpers import get_user_by_email, get_user_by_token, update_user
# from app.utils.hash import hash_password
# router = APIRouter()

# # @router.post("/forgot-password")
# # def forgot_password(data: ForgotPasswordSchema):
# #     user = get_user_by_email(data.email)
    
# #     if not user:
# #         raise HTTPException(status_code=404, detail="User not found")

# #     token = generate_reset_token()
# #     print(token)
# #     user.reset_token = token
# #     save_user(user)  # commit to DB

# #     send_reset_email(user.email, token)

# #     return {"message": "Reset link sent to email"}

# @router.post("/forgot-password")
# def forgot_password(data: ForgotPasswordSchema):
#     try:
#         print("API HIT")

#         user = get_user_by_email(data.email)

#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")

#         token = generate_reset_token()

#         update_user(
#             {"email": data.email},
#             {"reset_token": token}
#         )

#         return {
#             "message": "Reset token generated",
#             "token": token
#         }

#     except Exception as e:
#         print("ERROR:", str(e))
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # @router.post("/reset-password")
# # def reset_password(data: ResetPasswordSchema):

# #     user = get_user_by_token(data.token)

# #     if not user:
# #         raise HTTPException(status_code=400, detail="Invalid token")

# #     user.password = hash_password(data.new_password)
# #     user.reset_token = None

# #     save_user(user)

# #     return {"message": "Password updated successfully"}

# @router.post("/reset-password")
# def reset_password(data: ResetPasswordSchema):
#     try:
#         user = get_user_by_token(data.token)

#         if not user:
#             raise HTTPException(status_code=400, detail="Invalid token")

#         hashed_password = hash_password(data.new_password)

#         update_user(
#             {"reset_token": data.token},
#             {
#                 "password": hashed_password,
#                 "reset_token": None
#             }
#         )

#         return {"message": "Password updated successfully"}

#     except Exception as e:
#         print("ERROR:", str(e))
#         raise HTTPException(status_code=500, detail="Internal Server Error")


from datetime import datetime

from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.controllers.auth_controller import register_controller, login_controller
from app.schemas.password_schema import ForgotPasswordSchema, ResetPasswordSchema
from app.utils.db_helpers import get_user_by_email, get_user_by_token, update_user
from app.utils.hash import hash_password
from app.utils.token import generate_reset_token
# from app.utils.email import send_reset_email   # keep off for now
from app.db.database import db
from app.db.database import modules_collection

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(data: RegisterSchema):
    return register_controller(data)


@router.post("/login")
def login(data: LoginSchema):
    return login_controller(data)

@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordSchema):
    try:
        print("🔥 API HIT")
        print("Email:", data.email)

        user = get_user_by_email(data.email)
        print("User found:", user)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        token = generate_reset_token()
        print("Token:", token)

        update_user(
            {"email": data.email},
            {"reset_token": token}
        )

        return {
            "message": "Reset token generated",
            "token": token
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/reset-password")
def reset_password(data: ResetPasswordSchema):
    try:
        user = get_user_by_token(data.token)

        if not user:
            raise HTTPException(status_code=400, detail="Invalid token")

        hashed_password = hash_password(data.new_password)

        update_user(
            {"reset_token": data.token},
            {
                "password": hashed_password,
                "reset_token": None
            }
        )

        return {"message": "Password updated successfully"}

    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")
    


# from bson import ObjectId

# @router.get("/fetch-All-depertments-Onthe-basis-of-Branch/{branch_id}")
# def get_all_departments(branch_id: str):

#     try:
#         departments = list(
#             db["departments"].find(
#                 {"branch_id": ObjectId(branch_id)},
#                 {"_id": 0, "name": 1}
#             )
#         )

#         return departments

#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

from bson import ObjectId

@router.get("/fetch-All-DepertmentHead-Onthe-basis-of-Depertment/{department_id}")
def get_DepertmentHead(department_id: str):

    try:
        depertment_Head = list(
            db["department_head"].find(
                {"department_id": ObjectId(department_id)},
                {
                    "_id": 0,
                    "head_name": 1,
                    "head_email": 1,
                    "head_mobileno": 1
                }
            )
        )

        # and i want to send department name also in response so i will do one more query to get department name
        department = db["departments"].find_one(
            {"_id": ObjectId(department_id)},
            {"_id": 0, "name": 1}
        )
        

        # Combine department name with department head information
        for head in depertment_Head:
            head["department_name"] = department.get("name", "Unknown")

        return depertment_Head

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




# =====================================================
# CREATE WEBSITE / MODULE /WORK
# =====================================================
from app.schemas.module_schema import ModuleCreate

@router.post("/create-module")
def create_module(data: ModuleCreate):

    try:

        module_data = {

            "module_name": data.module_name,

            "module_url": data.module_url,

            "department_id": ObjectId(data.department_id),

            "created_at": datetime.utcnow()
        }

        result = modules_collection.insert_one(module_data)

        return {
            "message": "Module Created Successfully",
            "module_id": str(result.inserted_id)
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

# ----------------------------------------------
# work on Admin Add Employee under department head
# ----------------------------------------------

@router.post("/add-employee-under-department-head")
def add_employee_under_department_head(employee_data: dict):
    try:
        # Validate input data
        required_fields = ["name", "email", "mobile_no", "department_id"]
        for field in required_fields:
            if field not in employee_data:
                raise HTTPException(status_code=400, detail=f"Missing field: {field}")

        # Create employee record
        employee_record = {
            "name": employee_data["name"],
            "email": employee_data["email"],
            "mobile_no": employee_data["mobile_no"],
            "department_id": ObjectId(employee_data["department_id"]),
            "created_at": datetime.utcnow()
        }

        # Insert into database
        result = db["employees"].insert_one(employee_record)

        return {
            "message": "Employee added successfully",
            "employee_id": str(result.inserted_id)
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))