import os
from datetime import datetime
from typing import Dict
from fastapi import HTTPException
import motor.motor_asyncio
from bson.objectid import ObjectId
import bcrypt
from backend.models.users import User, UserLogin, Admin
from backend.models.services import ServiceProvider, Appointments

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASS")
# MONGO_URL = "mongodb://localhost:27017"
MONGO_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@cluster0.rmqx2.mongodb.net/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.fixie
users = db.get_collection("users")
admin_users = db.get_collection("admin_users")
services = db.get_collection("services")
appoointments = db.get_collection("appointments")

def hash_password(password: str)->str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str)->bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

async def add_user(user: User)->Dict:
    user = user.model_dump()
    user["password"] = hash_password(user["password"])
    result = await users.insert_one(user)
    user_in_db = await find_user(result.inserted_id)
    return user_in_db

async def find_user(id: str)->Dict:
    user = await users.find_one({"_id": ObjectId(id)})
    return user

async def check_auth(user: UserLogin)->Dict:
    user_in_db = await users.find_one({"email": user["email"]})
    if user_in_db and verify_password(user["password"], user_in_db["password"]):
        return user_in_db
    return {}

async def add_admin(admin: Admin)->Dict:
    admin = admin.model_dump()
    admin["password"] = hash_password(admin["password"])
    result = await admin_users.insert_one(admin)
    admin_in_db = await find_admin(result.inserted_id, by="_id")
    return admin_in_db

async def find_admin(query: str, by:str="email")->Dict:
    admin = await admin_users.find_one({by: query})
    return admin

async def check_admin_auth(admin: Admin)->Dict:
    admin_in_db = await admin_users.find_one({"email": admin["email"]})
    if admin_in_db and verify_password(admin["password"], admin_in_db["password"]):
        return admin_in_db
    return {}

async def add_service_provider(service_provider: ServiceProvider)->Dict:
    service_provider = service_provider.model_dump()
    result = await services.insert_one(service_provider)
    service_provider_in_db = await find_service_provider(result.inserted_id)
    return service_provider_in_db

async def find_service_provider(id: str)->Dict:
    service_provider = await services.find_one({"_id": ObjectId(id)})
    service_provider.pop("_id")
    return service_provider

async def get_services()->Dict:
    service_providers = []
    async for service_provider in services.find():
        service_provider["_id"] = str(service_provider["_id"])
        service_providers.append(service_provider)
    
    return {"services": service_providers}

async def add_rating(id: str, rating: float)->Dict:
    service_provider = await find_service_provider(id)
    service_provider["rating"] = rating
    await services.update_one({"_id": ObjectId(id)}, {"$set": service_provider})
    return service_provider

async def find_appointment(id: str)->Dict:
    appointment = await appoointments.find_one({"_id": ObjectId(id)})
    appointment["_id"] = str(appointment["_id"])
    return appointment

async def create_appointment(appointment: Appointments)->Dict:
    appointment = appointment.model_dump()
    dt = datetime.strptime(appointment['datetime'], "%Y-%m-%dT%H:%M")
    if dt < datetime.now():
        return HTTPException(status_code=400, detail="Please enter a valid date in the future.")
    result = await appoointments.insert_one(appointment)
    appointment_in_db = await find_appointment(result.inserted_id)
    return appointment_in_db