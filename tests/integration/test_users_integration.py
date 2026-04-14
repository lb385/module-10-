import pytest


@pytest.mark.integration
def test_create_user_success(integration_client):
    payload = {
        "username": "unique_user",
        "email": "unique_user@example.com",
        "password": "StrongPass123",
    }
    response = integration_client.post("/users", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["username"] == payload["username"]
    assert body["email"] == payload["email"]
    assert "password_hash" not in body
    assert "created_at" in body


@pytest.mark.integration
def test_create_user_duplicate_username_or_email(integration_client):
    payload = {
        "username": "duplicate_user",
        "email": "duplicate@example.com",
        "password": "StrongPass123",
    }

    first = integration_client.post("/users", json=payload)
    assert first.status_code == 201

    same_username = integration_client.post(
        "/users",
        json={
            "username": "duplicate_user",
            "email": "another@example.com",
            "password": "StrongPass123",
        },
    )
    assert same_username.status_code == 409

    same_email = integration_client.post(
        "/users",
        json={
            "username": "another_user",
            "email": "duplicate@example.com",
            "password": "StrongPass123",
        },
    )
    assert same_email.status_code == 409


@pytest.mark.integration
def test_create_user_invalid_email_rejected(integration_client):
    payload = {
        "username": "invalid_email_user",
        "email": "not-an-email",
        "password": "StrongPass123",
    }
    response = integration_client.post("/users", json=payload)

    assert response.status_code == 422
