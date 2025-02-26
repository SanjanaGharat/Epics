from typing import Dict
import motor.motor_asyncio
from bson.objectid import ObjectId
import bcrypt
from backend.models.users import User, UserLogin, Admin

MONGO_URL = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.fixie
users = db.get_collection("users")
admin_users = db.get_collection("admin_users")

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