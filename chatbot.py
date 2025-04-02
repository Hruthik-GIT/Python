# chatbot.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from pydantic import BaseModel  # Add this import

router = APIRouter()

# Pydantic model for request body
class ChatRequest(BaseModel):
    user_message: str

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(Text, nullable=False)
    bot_response = Column(Text, nullable=False)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    user_message = request.user_message.lower()  # Convert to lowercase for case-insensitive matching
    if "hello" in user_message:
        response = "Hello! How can I help you?"
    elif "how are you" in user_message:
        response = "I'm doing great, thanks for asking! How about you?"
    elif "bye" in user_message:
        response = "Goodbye! See you next time."
    elif "help" in user_message:
        response = "Sure, I’m here to assist! What do you need help with?"
    elif "what are you?" in user_message:
        response = "I'm the Chatbot built by CyberEdge Students to assist you with operations on the BAU Portal."
    else:
        response = "I'm still learning! Could you try something else?"
    
    new_message = Message(user_message=user_message, bot_response=response)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    
    return {"user": user_message, "bot": response}