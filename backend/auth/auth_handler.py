import jwt
import os
import time
from typing import Dict

SECRET_KEY = os.getenv("JWT_SECRET") or "arime0a0l0a0w0i0d0s0o0h0b0"
JWT_ALGORITHM = "HS256"
EXPIRATION_TIME_MINUTES = 360

def signJWT(user_email: str)->Dict:
    payload = {"user_email": user_email, "expires": time.time() + EXPIRATION_TIME_MINUTES * 60}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return {"token": jwt_token}

def decodeJWT(token: str)->Dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=JWT_ALGORITHM)
        return payload if payload["expires"] >= time.time() else {}
    except:
        return {}