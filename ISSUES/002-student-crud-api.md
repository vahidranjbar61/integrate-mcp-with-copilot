Title: Implement Student CRUD API

Description

Add REST endpoints to manage student profiles (create/read/update/delete) and return JSON responses.

Acceptance criteria

- Add endpoints under `/students`:
  - POST `/students` to create a student (accepts JSON with `admission_no`, `name`, `email`, `grade`)
  - GET `/students` to list students (support query params `name`, `admission_no`, `grade`)
  - GET `/students/{admission_no}` to retrieve a single student
  - PUT `/students/{admission_no}` to update student fields
  - DELETE `/students/{admission_no}` to remove a student
- Use the DB models from Issue 001 and respond with appropriate HTTP status codes.
- Add unit tests for the happy-path of each endpoint.

Labels: enhancement, api
