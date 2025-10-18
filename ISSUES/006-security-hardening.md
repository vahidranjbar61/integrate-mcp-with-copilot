Title: Security hardening and tech-debt cleanup

Description

Address security issues and upgrade dependencies to follow modern best practices.

Acceptance criteria

- Replace any use of deprecated APIs and ensure dependencies in `requirements.txt` are pinned to supported versions.
- Add password hashing (bcrypt) and remove plaintext password usage.
- Add input validation and CSRF protection guidelines for form-based frontends.
- Add a short security checklist to `SECURITY.md` documenting secrets handling, DB creds, and upload policies.
- Add unit tests that validate key input sanitization behavior.

Labels: security, maintenance
