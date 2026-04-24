from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    APP_NAME: str = os.getenv("APP_NAME", "TradePulse AI")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-this-secret")
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "Abshira")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "Mushtaq10.")
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_PRICE_ID: str = os.getenv("STRIPE_PRICE_ID", "")

settings = Settings()
