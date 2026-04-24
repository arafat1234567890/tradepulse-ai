from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.core.security import create_access_token

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/signup")
def signup(payload: SignupRequest):
    # Replace with database user creation and hashed passwords.
    token = create_access_token({"sub": payload.email, "role": "user"})
    return {"message": "signup successful", "token": token, "requires_payment": True}

@router.post("/login")
def login(payload: LoginRequest):
    # Demo login only. Replace with real database verification.
    if not payload.email or not payload.password:
        raise HTTPException(status_code=400, detail="Email and password required")
    token = create_access_token({"sub": payload.email, "role": "user"})
    return {"message": "login successful", "token": token}
