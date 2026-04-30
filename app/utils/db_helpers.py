

from app.models.user_model import user_entity
from app.db.database import users_collection, company_collection

# Get user by email
# def get_user_by_email(email):
#     # user = db.find_one({"email": email})
#     user = users_collection.find_one({"email": email})
#     if user:
#         return user
#     return None

def get_user_by_email(email):
    return users_collection.find_one({"email": email})

# Get user by token
# def get_user_by_token(token):
#     user = users_collection.find_one({"reset_token": token})
#     if user:
#         return user
#     return None
def get_user_by_token(token):
    return users_collection.find_one({"reset_token": token})

# Update user

def update_user(filter_query, update_data):
    users_collection.update_one(
        filter_query,
        {"$set": update_data}
    )

def create_company(data):
    return company_collection.insert_one(data)

