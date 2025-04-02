from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal 
from ..models import Lab

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()
# @router.post("/", response_model=labResponse)