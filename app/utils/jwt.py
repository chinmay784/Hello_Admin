from jose import jwt
from app.core.config import JWT_SECRET

def create_token(data: dict):
    return jwt.encode(data, JWT_SECRET, algorithm="HS256")

from app.core.config import JWT_SECRET

def decode_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except:
        return None