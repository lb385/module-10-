import pytest
from pydantic import ValidationError

from app.schemas import UserCreate


def test_user_create_schema_valid_payload():
    payload = UserCreate(
        username="student1",
        email="student1@example.com",
        password="StrongPass123",
    )
    assert payload.username == "student1"


def test_user_create_schema_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="student2",
            email="not-an-email",
            password="StrongPass123",
        )


def test_user_create_schema_short_password():
    with pytest.raises(ValidationError):
        UserCreate(
            username="student3",
            email="student3@example.com",
            password="short",
        )
