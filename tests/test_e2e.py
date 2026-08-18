import pytest
from fastapi.testclient import TestClient
from hms_backend.app.main import app

client = TestClient(app)


def test_e2e_all_module_endpoints():
    endpoints = [
        "/api/v1/admin/dashboard",
        "/api/v1/admin/users",
        "/api/v1/admin/departments",
        "/api/v1/admin/doctors",
        "/api/v1/admin/staff",
        "/api/v1/admin/settings",
        "/api/v1/patients",
        "/api/v1/appointments",
        "/api/v1/opd/queue",
        "/api/v1/ipd/rooms",
        "/api/v1/ipd/admissions",
        "/api/v1/nursing/vitals",
        "/api/v1/nursing/notes",
        "/api/v1/nursing/medications",
        "/api/v1/laboratory/requests",
        "/api/v1/laboratory/samples",
        "/api/v1/laboratory/reports",
        "/api/v1/pharmacy/inventory",
        "/api/v1/pharmacy/prescriptions",
        "/api/v1/pharmacy/bills",
        "/api/v1/pharmacy/alerts",
        "/api/v1/billing/invoices",
        "/api/v1/billing/payments",
        "/api/v1/billing/charges/consultation",
        "/api/v1/ambulance/fleet",
        "/api/v1/ambulance/bookings",
        "/api/v1/reports",
    ]

    for ep in endpoints:
        res = client.get(ep)
        assert res.status_code == 200, f"Endpoint {ep} failed with status {res.status_code}"
        assert res.headers["content-type"].startswith("application/json")
        assert res.json() is not None
