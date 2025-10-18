Title: Add photo upload and serve images

Description

Allow admins to upload student photos and serve them from the `static/images` directory.

Acceptance criteria

- Add endpoint POST `/students/{admission_no}/photo` to upload a photo file (multipart/form-data).
- Validate file type (jpg/png) and size (e.g., < 2MB).
- Save files under `static/images/{admission_no}.jpg` and record `photo_path` on the Student model.
- Ensure images are served statically via the existing `/static` mount.
- Add tests for the upload endpoint (mock file uploads).

Labels: feature, backend, storage
