from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt import decode_token  # you must have this

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials

        payload = decode_token(token)  # decode JWT

        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")

        return payload  # user data

    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")