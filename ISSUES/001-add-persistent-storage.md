Title: Add persistent storage (SQLite) and ORM models

Description

Add persistent storage to the FastAPI app using SQLite and SQLModel (or SQLAlchemy).

Acceptance criteria

- Add SQLModel/SQLAlchemy dependency to project requirements (update `requirements.txt`).
- Create a `src/models.py` with `Student`, `Activity`, and `Participant` models:
  - Student: `admission_no` (primary key), `name`, `email`, `grade`, `photo_path`
  - Activity: `id`, `name` (unique), `description`, `schedule`, `max_participants`
  - Participant: `id`, `activity_id` (FK), `student_email` (FK)
- Update `src/app.py` to connect to the SQLite DB and use sessions for DB operations.
- Include an `init_db()` routine that creates tables at startup when DB is missing.

Notes

- Prefer SQLite for local dev to keep setup minimal; make DB path configurable via an environment variable `DATABASE_URL`.
- Keep API backward-compatible: existing `/activities` endpoint should read from DB.

Labels: enhancement, backend
