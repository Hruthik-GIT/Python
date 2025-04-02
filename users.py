from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal  # Change app.database to relative import
from ..models import User
from ..schemas import UserCreate, UserResponse
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, hashed_password="hashedpw")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
