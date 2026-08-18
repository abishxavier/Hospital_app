import pytest
from datetime import timedelta
from hms_backend.app.core.security import hash_password, verify_password, create_access_token, decode_access_token
from hms_backend.app.services.billing_service import calculate_invoice_total
from hms_backend.app.services.pharmacy_service import check_low_stock_alerts
from hms_backend.app.services.ipd_service import allocate_bed
from hms_backend.app.schemas.user import UserCreate, LoginRequest
from hms_backend.app.schemas.patient import PatientCreate


def test_password_hashing():
    raw_pwd = "SecureHospitalPassword123"
    hashed = hash_password(raw_pwd)
    assert hashed != raw_pwd
    assert verify_password(raw_pwd, hashed) is True
    assert verify_password("WrongPassword", hashed) is False


def test_jwt_token_generation_and_decoding():
    payload = {"sub": "doctor@hospital.com", "role": "doctor"}
    token = create_access_token(payload, expires_delta=timedelta(minutes=30))
    assert isinstance(token, str)
    assert len(token) > 20

    decoded = decode_access_token(token)
    assert decoded is not None
    assert decoded["sub"] == "doctor@hospital.com"
    assert decoded["role"] == "doctor"


def test_calculate_invoice_total():
    items = [
        {"price": 50.0, "qty": 1},
        {"price": 35.5, "qty": 2},
        {"price": 10.0, "qty": 3},
    ]
    total = calculate_invoice_total(items)
    assert total == 151.00


def test_pharmacy_low_stock_alerts():
    class DummyMed:
        def __init__(self, med_id, name, stock_qty):
            self.id = med_id
            self.name = name
            self.stock_qty = stock_qty

    meds = [
        DummyMed(1, "Paracetamol", 1200),
        DummyMed(2, "Pantoprazole", 50),
    ]
    alerts = check_low_stock_alerts(meds)
    assert len(alerts) == 1
    assert alerts[0]["Medicine Name"] == "Pantoprazole"
    assert alerts[0]["Alert Type"] == "Low Stock"


def test_allocate_bed_service():
    res = allocate_bed(ward_id=2, bed_number="Room 105")
    assert res["status"] == "success"
    assert res["ward_id"] == 2
    assert res["bed_number"] == "Room 105"


def test_pydantic_user_schema():
    u = UserCreate(full_name="Dr. Test User", email="test@hospital.com", password="password123", role="doctor")
    assert u.email == "test@hospital.com"
    assert u.role == "doctor"


def test_pydantic_patient_schema():
    p = PatientCreate(full_name="Jane Doe", phone="+91 99999 88888", gender="Female")
    assert p.full_name == "Jane Doe"
    assert p.phone == "+91 99999 88888"
