Title: Migrate selected Ayushmanas schema and import sample data

Description

Map the Ayushmanas `student.sql` schema to the new models and import a subset of sample data for testing.

Acceptance criteria

- Create a migration plan mapping `stud_adm` fields to the `Student` model.
- Write a script `scripts/import_ayushmanas.py` to parse `ISSUES/ayushmanas_student.sql` (copy of `student.sql`) and insert records into the SQLite DB.
- Import a small sample (10 students) and add a CI job or test that validates the import.

Notes

- We don't need to import `extra1/2/3` tables; merge meaningful fields into `Student` and `Participant` models.

Labels: migration, data
