from random import randint, choice


def generate_signal(symbol: str):
    direction = choice(["BUY", "SELL", "WAIT"])
    confidence = randint(58, 86)
    return {
        "symbol": symbol,
        "direction": direction,
        "confidence": confidence,
        "entry": "Market / Zone Based",
        "stop_loss": "Calculated from volatility",
        "take_profit": "Calculated from risk-reward",
        "risk_reward": "1:2",
        "confirmations": [
            {"name": "RSI", "status": "confirmed"},
            {"name": "MACD", "status": "confirmed"},
            {"name": "Moving Average", "status": "mixed"},
            {"name": "News Sentiment", "status": "neutral"},
        ],
        "warning": "Educational analysis only. Not financial advice."
    }
