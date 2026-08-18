import pytest
from fastapi.testclient import TestClient
from hms_backend.app.main import app

client = TestClient(app)


def test_create_and_delete_across_modules():
    # 1. Patient Registration (Reception)
    resp = client.post("/api/v1/patients", json={
        "Patient ID": "PAT-9999",
        "Name": "Audit Test Patient",
        "Phone": "+91 99999 88888",
        "Registered Date": "2026-08-13",
        "Status": "Active"
    })
    assert resp.status_code == 200
    pat_data = resp.json()
    pat_id = pat_data["id"]
    assert pat_id is not None

    # Delete patient -> should mark soft deleted and log in deleted_records
    del_resp = client.delete(f"/api/v1/patients/{pat_id}")
    assert del_resp.status_code == 200

    # 2. Doctor Appointments
    resp = client.post("/api/v1/doctor/appointments", json={
        "Time": "11:00 AM",
        "Patient Name": "Audit Patient 2",
        "Doctor": "Dr. Priya Nair",
        "Status": "Scheduled"
    })
    assert resp.status_code == 200
    doc_appt_id = resp.json()["id"]

    del_resp = client.delete(f"/api/v1/doctor/appointments/{doc_appt_id}")
    assert del_resp.status_code == 200

    # 3. Nurse Vitals
    resp = client.post("/api/v1/nurse/patient-vitals", json={
        "Patient": "Nurse Test Patient",
        "BP": "120/80 mmHg",
        "Heart Rate": "75 bpm",
        "Temp": "98.6 °F",
        "Recorded At": "10:00 AM"
    })
    assert resp.status_code == 200
    vitals_id = resp.json()["id"]

    del_resp = client.delete(f"/api/v1/nurse/patient-vitals/{vitals_id}")
    assert del_resp.status_code == 200

    # 4. Pharmacy Inventory
    resp = client.post("/api/v1/pharmacy/inventory", json={
        "Medicine Name": "Test Drug 500mg",
        "Batch No": "BAT-TEST-1",
        "Expiry Date": "2028-12-31",
        "Stock Qty": "200 Units",
        "Status": "Available"
    })
    assert resp.status_code == 200
    med_id = resp.json()["id"]

    del_resp = client.delete(f"/api/v1/pharmacy/inventory/{med_id}")
    assert del_resp.status_code == 200

    # 5. Billing Invoices
    resp = client.post("/api/v1/billing/invoices", json={
        "Invoice ID": "INV-TEST-99",
        "Patient": "Billing Test Patient",
        "Total Amount": "$150.00",
        "Due Date": "2026-08-20",
        "Status": "Pending"
    })
    assert resp.status_code == 200
    inv_id = resp.json()["id"]

    del_resp = client.delete(f"/api/v1/billing/invoices/{inv_id}")
    assert del_resp.status_code == 200

    # 6. Verify Deleted Records Audit Table Endpoint
    audit_resp = client.get("/api/v1/admin/deleted-records")
    assert audit_resp.status_code == 200
    audit_records = audit_resp.json()
    assert len(audit_records) >= 5
