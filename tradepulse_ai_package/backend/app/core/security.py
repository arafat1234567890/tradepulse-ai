from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import settings

ALGORITHM = "HS256"


def create_access_token(data: dict, minutes: int = 120):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=minutes)
    payload.update({"exp": expire})
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)
