from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, signals, admin, payments
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(signals.router, prefix="/api/signals", tags=["signals"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])

@app.get("/")
def root():
    return {"status": "online", "app": settings.APP_NAME}
