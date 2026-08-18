import pytest
from fastapi.testclient import TestClient
from hms_backend.app.main import app

client = TestClient(app)


def test_openapi_schema_compatibility():
    res = client.get("/openapi.json")
    assert res.status_code == 200
    schema = res.json()
    assert "openapi" in schema
    assert "paths" in schema
    assert "/api/v1/admin/dashboard" in schema["paths"]


def test_legacy_route_alias_compatibility():
    # Direct legacy routes check
    res_admin = client.get("/api/admin/dashboard")
    assert res_admin.status_code == 200

    res_patients = client.get("/api/reception/patients")
    assert res_patients.status_code == 200

    res_docs = client.get("/api/doctor/appointments")
    assert res_docs.status_code == 200
