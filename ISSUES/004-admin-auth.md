Title: Add simple admin authentication and protect admin endpoints

Description

Add an admin login flow (cookie-based session) and protect create/update/delete student endpoints.

Acceptance criteria

- Add `/auth/login` and `/auth/logout` endpoints that accept credentials from `users` table (store credentials hashed).
- Protect endpoints that modify data (create/update/delete student, photo upload) with an admin-only dependency.
- Add a CLI command or startup check to create an initial admin user (or provide instructions to set an admin via env vars).
- Document the auth flow in `src/README.md`.

Labels: security, enhancement
