import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
JWT_SECRET = os.getenv("JWT_SECRET")

# MAIL_FROM = os.getenv("MAIL_FROM")
# MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
# MAIL_SERVER = os.getenv("MAIL_SERVER")
# MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")