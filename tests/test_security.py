import pytest
from fastapi.testclient import TestClient
from hms_backend.app.main import app
from hms_backend.app.core.security import hash_password, verify_password, create_access_token, decode_access_token

client = TestClient(app)


def test_auth_login_security():
    res = client.post("/api/v1/auth/login", json={"username": "admin@hospital.com", "password": "admin123"})
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["role"] == "admin"


def test_invalid_login_rejection():
    res = client.post("/api/v1/auth/login", json={"username": "admin@hospital.com", "password": "wrong_password_999"})
    assert res.status_code == 401


def test_invalid_jwt_decoding():
    decoded = decode_access_token("invalid.jwt.token.string")
    assert decoded is None


def test_password_hash_security_strength():
    hashed = hash_password("SuperSecretKey2026")
    assert len(hashed) >= 64
    assert hashed != hash_password("DifferentSecretKey")


def test_cors_headers():
    res = client.options("/api/v1/admin/dashboard", headers={"Origin": "http://localhost:5174", "Access-Control-Request-Method": "GET"})
    assert res.status_code in [200, 204]
    assert "access-control-allow-origin" in res.headers
