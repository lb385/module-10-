# Reflection

## What went well

- Implemented a clean separation between model, schema, security, and route layers.
- Added deterministic tests for hashing, schema validation, and integration behavior.
- Automated CI/CD to verify quality before deployment.

## Challenges faced

- Ensuring uniqueness constraints are tested reliably required using a real Postgres DB.
- Managing environment-driven database configuration for both local and CI execution.
- Preventing sensitive fields (`password_hash`) from leaking in response models.

## What I learned

- How to structure secure user creation pipelines in FastAPI.
- How to combine unit and integration tests in one workflow.
- How to automate container build, scan, and Docker Hub deployment with GitHub Actions.
