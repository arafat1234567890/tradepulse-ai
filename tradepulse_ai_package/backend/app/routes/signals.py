from fastapi import APIRouter
from app.services.signal_engine import generate_signal

router = APIRouter()

@router.get("/")
def get_signals():
    symbols = ["BTC/USDT", "ETH/USDT", "EUR/USD", "XAU/USD", "GBP/USD"]
    return [generate_signal(symbol) for symbol in symbols]

@router.get("/{symbol}")
def get_signal(symbol: str):
    return generate_signal(symbol.upper())
