import pytest
from fastapi.testclient import TestClient
from hms_backend.app.main import app

client = TestClient(app)


def test_health_check_integration():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_patients_crud_integration():
    # 1. Fetch patients
    get_res = client.get("/api/v1/patients")
    assert get_res.status_code == 200
    initial_count = len(get_res.json())

    # 2. Register patient
    new_patient = {
        "Name": "Integration Patient Test",
        "Phone": "+91 88888 77777",
        "Email": "integration.patient@test.com"
    }
    post_res = client.post("/api/v1/patients", json=new_patient)
    assert post_res.status_code == 200
    created = post_res.json()
    assert created["Name"] == "Integration Patient Test"
    patient_id = created["id"]

    # 3. Verify count increased
    get_res_2 = client.get("/api/v1/patients")
    assert len(get_res_2.json()) == initial_count + 1

    # 4. Delete patient
    del_res = client.delete(f"/api/v1/patients/{patient_id}")
    assert del_res.status_code == 200
    assert del_res.json()["status"] == "success"


def test_doctors_crud_integration():
    # 1. Get doctors
    res = client.get("/api/v1/doctors")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

    # 2. Create doctor
    doc_payload = {
        "Doctor Name": "Dr. Integration Test",
        "Department": "Cardiology",
        "Phone": "+91 97777 66666"
    }
    create_res = client.post("/api/v1/doctors", json=doc_payload)
    assert create_res.status_code == 200
    doc_id = create_res.json()["id"]

    # 3. Clean up doctor
    del_res = client.delete(f"/api/v1/doctors/{doc_id}")
    assert del_res.status_code == 200
