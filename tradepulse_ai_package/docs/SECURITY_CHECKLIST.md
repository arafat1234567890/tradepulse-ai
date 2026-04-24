# Security Checklist

## Authentication

- Use hashed passwords, not plain text.
- Add email verification.
- Add 2FA for admin accounts.
- Use JWT expiration and refresh tokens.

## API Keys

- Encrypt user exchange API keys.
- Never store withdrawal-enabled API keys.
- Require read-only or trade-only keys.
- Allow users to delete API keys.

## Admin

- Protect admin routes.
- Log admin actions.
- Rate-limit login attempts.
- Change default password before production.

## Payments

- Use Stripe Checkout.
- Verify webhooks server-side.
- Do not trust frontend payment status.

## Infrastructure

- Use HTTPS.
- Use environment variables.
- Enable database backups.
- Monitor error logs.
