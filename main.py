# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import List, Dict
from app.routes import users, labs
from .database import engine, Base
from app import chatbot  

# Database Models
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CyberEdge API", version="1.0")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Secret Key for JWT
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 for Login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Mock User Database (Replace with actual DB)
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "full_name": "Test User",
        "email": "testuser@example.com",
        "hashed_password": pwd_context.hash("testpassword"),  # Hashed password
        "disabled": False,
    }
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):
    user = fake_users_db.get(username)
    return user

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"message": f"Welcome {username}, you accessed a protected route!"}

@app.get("/")
def read_root():
    return {"message": "Hello Cy"}

# Include Other Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(labs.router, prefix="/labs", tags=["Labs"])
app.include_router(chatbot.router, prefix="/chat", tags=["Chatbot"])  # Add chatbot router

# --------------------- Testing Module ---------------------

# Sample 20 Questions
QUESTIONS = [
    {"id": 1, "question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid", "Rome"], "answer": "Paris"},
    {"id": 2, "question": "What is 5 + 3?", "options": ["5", "8", "10", "15"], "answer": "8"},
    {"id": 3, "question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"id": 4, "question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Tolstoy", "Hemingway", "Austen"], "answer": "Shakespeare"},
    {"id": 5, "question": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
    {"id": 6, "question": "What is the boiling point of water in Celsius?", "options": ["50", "75", "100", "120"], "answer": "100"},
    {"id": 7, "question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Da Vinci", "Picasso", "Rembrandt"], "answer": "Da Vinci"},
    {"id": 8, "question": "Which gas do plants use for photosynthesis?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"id": 9, "question": "What is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
    {"id": 10, "question": "What is 12 x 4?", "options": ["36", "42", "48", "52"], "answer": "48"},
]

# Request Model for Submitting Answers
class AnswerSubmission(BaseModel):
    answers: Dict[int, str]  # Dictionary where {question_id: selected_answer}


@app.get("/get-questions")
async def get_questions():
    """Returns the list of questions without answers (to prevent cheating)."""
    return [{"id": q["id"], "question": q["question"], "options": q["options"]} for q in QUESTIONS]


@app.post("/submit-answers")
async def submit_answers(submission: AnswerSubmission):
    """Receives user answers, calculates score, and returns result."""
    score = 0

    for q in QUESTIONS:
        question_id = q["id"]
        correct_answer = q["answer"]

        # Check if user provided an answer and if it is correct
        if submission.answers.get(question_id) == correct_answer:
            score += 1

    return {"total_score": score, "max_score": len(QUESTIONS), "message": f"You scored {score} out of {len(QUESTIONS)}"}
