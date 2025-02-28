from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.db.database import find_admin

from ..auth.auth_handler import decodeJWT

class UserBearerAuth(HTTPBearer):
    def __init__(self, auto_error: bool = True)->None:
        super(UserBearerAuth, self).__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request)->HTTPAuthorizationCredentials:
        credentials = await super(UserBearerAuth, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or token has expired.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
    
    def verify_jwt(self, jwt_token: str)->bool:
        is_valid: bool = False
        try:
            payload = decodeJWT(jwt_token)
        except:
            payload = None
        if payload:
            is_valid = True
        return is_valid
    

class AdminBearerAuth(HTTPBearer):
    def __init__(self, auto_error: bool = True)->None:
        super(AdminBearerAuth, self).__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request)->HTTPAuthorizationCredentials:
        credentials = await super(AdminBearerAuth, self).__call__(request)
        print("hola!")
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not await self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or token has expired.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    async def verify_jwt(self, jwt_token: str)->bool:
        is_valid: bool = False
        try:
            payload = decodeJWT(jwt_token)
        except:
            payload = None
        if payload:
            is_valid = True
            user_email = payload.get("user_email")
            user = await find_admin(user_email)
            if user:
                is_valid = True
            else:
                is_valid = False
        return is_valid