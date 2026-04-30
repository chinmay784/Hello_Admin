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


from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.controllers.auth_controller import register_controller, login_controller
from app.schemas.password_schema import ForgotPasswordSchema, ResetPasswordSchema
from app.utils.db_helpers import get_user_by_email, get_user_by_token, update_user
from app.utils.hash import hash_password
from app.utils.token import generate_reset_token
# from app.utils.email import send_reset_email   # keep off for now

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
    