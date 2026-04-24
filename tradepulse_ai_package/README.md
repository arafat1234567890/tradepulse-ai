# TradePulse AI - Full Starter Package

AI-assisted trading analysis platform starter with:

- Public landing website
- User signup/login UI
- User dashboard
- Live signal cards
- Market analysis page
- Trade journal page
- Strategy page
- Admin login and admin panel
- Payment/subscription placeholder
- Backend API structure
- Signal engine mock service
- Security and deployment notes

> Important: This platform must be marketed as educational market analysis, not guaranteed profit or guaranteed accuracy.

## Default Admin Credentials for Local Development

Create `backend/.env` from `backend/.env.example` and set:

```env
ADMIN_USERNAME=Abshira
ADMIN_PASSWORD=Mushtaq10.
```

For production, change the password immediately and use a password manager.

## Project Structure

```text
tradepulse_ai_package/
├── frontend/          # Next.js frontend
├── backend/           # FastAPI backend
└── docs/              # Product, legal, and design documents
```

## Quick Start

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Backend runs on:

```text
http://localhost:8000
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

## Admin Login

Open:

```text
http://localhost:3000/admin-login
```

Use the credentials configured in `backend/.env`.

## Main Pages

- `/` - Landing page
- `/login` - User login
- `/signup` - Signup/payment page
- `/dashboard` - User dashboard
- `/signals` - Live signals
- `/analysis` - Market analysis
- `/journal` - Trade journal
- `/strategies` - Strategies
- `/admin-login` - Admin login
- `/admin` - Admin panel

## Payment Notes

The package contains a Stripe placeholder. To activate payments:

1. Create a Stripe account.
2. Add Stripe keys in `.env`.
3. Replace the mock checkout endpoint with a real Stripe Checkout Session.

## Trading Platform Notes

This starter does not execute trades automatically. Broker/exchange API integrations should be added only after:

- Secure API key vault is implemented
- User consent screens are added
- Risk controls are enforced
- Legal review is completed

## Disclaimer

This platform provides educational analysis only. It does not provide financial advice and does not guarantee profits.
