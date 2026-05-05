# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# # ROUTES
# from app.routes.auth_routes import router as auth_router
# from app.routes.company_routes import router as company_router
# from app.routes import branch_routes
# from app.routes import department_routes
# # from app.routes import vendor_routes
# from app.routes.vendor_routes import router as vendor_router
# from app.routes.procurement_routes import router as procurement_router

# # 👉 ADD THIS (VERY IMPORTANT)
# from app.api.requirement_routes import router as requirement_router


# app = FastAPI()

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # INCLUDE ROUTERS
# app.include_router(auth_router)
# app.include_router(company_router)
# app.include_router(branch_routes.router)
# app.include_router(department_routes.router)
# # app.include_router(vendor_routes.router)
# app.include_router(vendor_router)
# app.include_router(procurement_router)

# # 👉 ADD THIS LINE (MAIN FIX)
# app.include_router(requirement_router)


# @app.get("/")
# def home():
#     return {"message": "Admin Backend Running"}




# import os

# print("MONGO_URI:", os.getenv("MONGO_URI"))
# print("DB_NAME:", os.getenv("DB_NAME"))
















from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ROUTES
from app.routes.auth_routes import router as auth_router
from app.routes.company_routes import router as company_router
from app.routes import branch_routes
from app.routes import department_routes
from app.routes.vendor_routes import router as vendor_router   # ✅ FIXED
from app.routes.procurement_routes import router as procurement_router
from app.api.requirement_routes import router as requirement_router
from app.routes.product_routes import router as product_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
      "http://localhost:5173",
      "https://traxoerp.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# INCLUDE ROUTERS
app.include_router(auth_router)
app.include_router(company_router)
app.include_router(branch_routes.router)
app.include_router(department_routes.router)
app.include_router(vendor_router)   # ✅ FIXED
app.include_router(procurement_router)
app.include_router(requirement_router)
app.include_router(product_router)

@app.get("/")
def home():
    return {"message": "Admin Backend Running"}

print("Admin Backend Running...")
import os
print("MONGO_URI:", os.getenv("MONGO_URI"))
print("DB_NAME:", os.getenv("DB_NAME"))

