from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.config import settings
from app.core.security import create_access_token

router = APIRouter()

class AdminLoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def admin_login(payload: AdminLoginRequest):
    if payload.username == settings.ADMIN_USERNAME and payload.password == settings.ADMIN_PASSWORD:
        token = create_access_token({"sub": payload.username, "role": "admin"})
        return {"message": "admin login successful", "token": token}
    raise HTTPException(status_code=401, detail="Invalid admin credentials")

@router.get("/summary")
def admin_summary():
    return {
        "users": 128,
        "active_subscriptions": 91,
        "monthly_revenue_usd": 3003,
        "signals_today": 24,
        "system_status": "healthy"
    }
