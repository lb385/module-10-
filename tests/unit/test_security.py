from app.security import hash_password, verify_password


def test_hash_password_is_not_plain_text():
    raw = "SuperSecret123"
    hashed = hash_password(raw)

    assert hashed != raw
    assert hashed.startswith("$2")


def test_verify_password_success_and_failure():
    raw = "SuperSecret123"
    hashed = hash_password(raw)

    assert verify_password(raw, hashed) is True
    assert verify_password("WrongPassword", hashed) is False
