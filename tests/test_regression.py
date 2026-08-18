import pytest
from fastapi.testclient import TestClient
from hms_backend.app.main import app

client = TestClient(app)


def test_regression_core_features():
    """Regression test ensuring all primary module actions remain fully functional."""
    
    # 1. Health & Root
    assert client.get("/health").status_code == 200
    assert client.get("/").status_code == 200

    # 2. Auth Login
    auth_res = client.post("/api/v1/auth/login", json={"username": "admin@hospital.com", "password": "admin123"})
    assert auth_res.status_code == 200

    # 3. Patient Registration & Query
    p_res = client.post("/api/v1/patients", json={"Name": "Regression Patient", "Phone": "+91 90000 11111"})
    assert p_res.status_code == 200
    pid = p_res.json()["id"]

    # 4. Doctor Query
    d_res = client.get("/api/v1/doctors")
    assert d_res.status_code == 200

    # 5. Clean up
    client.delete(f"/api/v1/patients/{pid}")
