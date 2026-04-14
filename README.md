# FastAPI Secure User Model + CI/CD

This project implements a secure `User` model in FastAPI using SQLAlchemy and Pydantic, with password hashing, automated testing, and CI/CD to Docker Hub.

## Features

- SQLAlchemy `User` model with:
  - Unique `username`
  - Unique `email`
  - `password_hash` (never returns raw password)
  - `created_at` timestamp
- Pydantic schemas:
  - `UserCreate` for input validation
  - `UserRead` for safe response serialization
- Password hashing/verification using `passlib` + `bcrypt`
- Unit and integration tests with `pytest`
- GitHub Actions pipeline:
  - Runs tests against a real PostgreSQL service
  - Security scans with Trivy
  - Builds and pushes image to Docker Hub after successful tests

## Run tests locally

### 1) Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run tests

Brief overview:

- Run `tests/unit` for fast local validation (no database required).
- Run full `pytest` for unit + integration tests (requires PostgreSQL and `DATABASE_URL`).

Unit tests only:

```bash
pytest tests/unit -q
```

All tests (requires PostgreSQL and `DATABASE_URL`):

```bash
export DATABASE_URL="postgresql+psycopg2://postgres:postgres@localhost:5432/app_test"
pytest -q
```

### 3) Run app

```bash
uvicorn app.main:app --reload
```

## Docker Hub

- Docker Hub profile: https://hub.docker.com/u/lb385
- If the repository page is not found, create a Docker Hub repository named `module-10`, then rerun the GitHub Actions workflow.
- After the first successful push, use these links in this README:
  - https://hub.docker.com/r/lb385/module-10
  - https://hub.docker.com/r/lb385/module-10/tags

## GitHub Actions secrets required

- `DOCKERHUB_TOKEN`

## Submission checklist

- Add screenshot of successful GitHub Actions run.
- Add screenshot showing pushed Docker image in Docker Hub.
- Include your reflection document in the repository.
