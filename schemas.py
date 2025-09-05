from pydantic import BaseModel, EmailStr
from typing import Optional

# 🚀 Request model for creating a user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# ✅ Response model for returning user info (without password)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # Enables ORM support for SQLAlchemy models

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
