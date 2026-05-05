
from pymongo import MongoClient
from app.core.config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
print("MongoDB Connected Successfully")

# users_collection = db["users"]
# ✅ NEW COLLECTION
users_collection = db["adminUsers"]
company_collection = db["companies"]

vendor_collection = db["vendors"]
procurement_collection = db["procurement"]

requirement_collection = db["requirements"]
product_collection = db["products"]