from pydantic import BaseModel, Field

class ServiceProvider(BaseModel):
    name: str = Field(...)
    category: str = Field(...)
    service:str = Field(...)
    image: str = Field(...)
    rating: float = Field(...)
    cost: str = Field(...)
    description: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Akash Sharma",
                "category": "residential",
                "service": "Mistri",
                "image": "https://placehold.co/300",
                "rating": 4.20,
                "cost": "high",
                "description": "Expert in mistri services."
            }
        }