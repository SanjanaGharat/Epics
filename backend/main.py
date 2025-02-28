import os
from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

from backend.models.services import Appointments, ServiceProvider
from backend.models.users import User, UserLogin, Admin
from backend.auth.auth_handler import decodeJWT, signJWT
from backend.auth.auth_bearer import UserBearerAuth, AdminBearerAuth
from backend.db.database import (
    add_user, 
    check_admin_auth, 
    check_auth, 
    add_admin, 
    add_service_provider, 
    get_services, 
    find_service_provider, 
    create_appointment
)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
ADMIN_SECRET = os.getenv("ADMIN_SECRET") or "02supersecret144"

@app.get("/")
async def read_root()->Dict:
    return {"message": "This is the backend of our EPICS project."}

@app.post("/user/signup")
async def create_user(user: User = Body(...))->Dict:
    # validate user input
    added_user = await add_user(user)
    if added_user:
        return signJWT(user.email)
    
    return {"error": "An error occurred."}

@app.post("/user/login")
async def user_login(userInfo: UserLogin = Body(...))->Dict:
    userInfo = userInfo.model_dump()
    user_in_db = await check_auth(userInfo)
    if user_in_db:
        return signJWT(userInfo["email"])
    
    return {"error": "Given credentials are invalid."}

@app.post("/admin/signup")
async def create_admin(secret, admin: Admin = Body(...)):
    if secret != ADMIN_SECRET:
        return HTTPException(status_code=403, detail="Invalid secret.")
    added_admin = await add_admin(admin)
    if added_admin:
        return signJWT(admin.email)
    return {"error": "An error occurred."}

@app.post("/admin/login")
async def admin_login(adminInfo: Admin = Body(...))->Dict:
    adminInfo = adminInfo.model_dump()
    admin_in_db = await check_admin_auth(adminInfo)
    if admin_in_db:
        return signJWT(adminInfo["email"])
    
    return {"error": "Given credentials are invalid."}

@app.get("/secure", dependencies=[Depends(UserBearerAuth())])
async def secure_endpoint(token: str = Depends(UserBearerAuth()))->Dict:
    return {"message": "booo!"}

@app.get("/supersecure", dependencies=[Depends(AdminBearerAuth())])
async def super_secure_endpoint(token: str = Depends(AdminBearerAuth()))->Dict:
    decoded_token = decodeJWT(token)
    # do stuff with the token
    return {"message": "booo mega!"}

@app.post("/services/add")
async def add_service(service_provider: ServiceProvider = Body(...))->Dict:
    service_provider = service_provider
    image,cat = get_service_image_category(service_provider.service)
    service_provider.category = cat
    service_provider.image = image
    result = await add_service_provider(service_provider)
    # result.pop("_id")
    return result

def get_service_image_category(service:str):
    services = {
        "electrician": ("https://cdn-icons-png.flaticon.com/512/3467/3467234.png","Residential"),
        "ac repair": ("https://cdn-icons-png.flaticon.com/512/919/919081.png", "Residential"),
        "plumber": ("https://cdn-icons-png.flaticon.com/512/3998/3998390.png", "Residential"),
        "mobile repair" : ("https://cdn-icons-png.flaticon.com/512/12349/12349886.png", "Commercial"),
        "barber" : ("https://cdn-icons-png.flaticon.com/512/9054/9054739.png", "Residential"),
        "appliance repair": ("https://cdn-icons-png.flaticon.com/512/11311/11311315.png","Commercial"),
        "laptop repair": ("https://cdn-icons-png.flaticon.com/512/6265/6265665.png", "Commercial"),
        "carpenter": ("https://cdn-icons-png.flaticon.com/512/3998/3998402.png","Industrial"),
        "painter": ("https://cdn-icons-png.flaticon.com/512/838/838118.png", "Industrial"),
        "other": ("https://cdn-icons-png.flaticon.com/512/953/953789.png", "Commercial")
    }
    service = service.lower().strip().replace('-', ' ')
    if service in services:
        return services[service]
    if " ac " in service:
        return services["ac repair"]
    if "electric" in service:
        return services["electrician"]
    return services["other"]
    
@app.get("/services")
async def get_services_list()->Dict:
    return await get_services()

@app.get("/service")
async def get_service(id:str):
    return await find_service_provider(id)

@app.post("/appointments/create")
async def create_new_appointment(appointment: Appointments = Body(...)):
    return await create_appointment(appointment)
