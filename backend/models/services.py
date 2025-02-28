from pydantic import BaseModel, Field

class ServiceProvider(BaseModel):
    name: str = Field(...)
    category: str = Field(...)
    service:str = Field(...)
    image: str = Field(...)
    rating: float = Field(...)
    cost: str = Field(...)
    description: str = Field(...)
    address: str = Field(...)
    phone: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Akash Sharma",
                "category": "residential",
                "service": "Mistri",
                "image": "https://placehold.co/300",
                "rating": 4.20,
                "cost": "high",
                "description": "Expert in mistri services.",
                "address": "Enlightened Street",
                "phone": "+91 9001010101"
            }
        }


class Appointments(BaseModel):
    user_email: str = Field(...)
    user_name: str = Field(...)
    user_phone: str = Field(...)
    service_provider_id: str = Field(...)
    datetime:str = Field(...)
    extra_details: str = Field(...)
    status: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "user_email": "hola@v2.com",
                "user_name": "Hola",
                "user_phone": "+91 9001010101",
                "service_provider_id": "5f3f2b5c9d6e6e1e4c3d1b6d",
                "datetime":"2025-03-01T14:25",
                "status": "pending"
            }
        }