from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
    gender: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "waowaemail@tiv.com",
                "password": "thispasswordisbad",
                "gender": "male"
            }
        }

class UserLogin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "waowaemail@tiv.com",
                "password": "thispasswordisbad",
            }
        }


class Admin(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "bossmode@tiv.com",
                "password": "thispasswordisslightlybetter"
            }
        }
