from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(prefix="/doctor", tags=["doctor"])


# 1. View Appointments
@router.get("/appointments")
def get_appointments(doctor_name: str = None, db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Time": "10:30 AM", "Patient Name": "Aarav", "Doctor": "Dr. Madhavan", "Status": "In Consultation"},
        {"id": 2, "Time": "11:15 AM", "Patient Name": "Ishaan", "Doctor": "Dr. S. Karthikeyan", "Status": "Scheduled"},
        {"id": 3, "Time": "02:00 PM", "Patient Name": "Rahul", "Doctor": "Dr. Murugan Jeyaraman", "Status": "Scheduled"},
        {"id": 4, "Time": "03:30 PM", "Patient Name": "Tanvi", "Doctor": "Dr. Raj Kanna", "Status": "Scheduled"}
    ]
    records = get_generic_records(db, "doctor_appointments", defaults)
    if doctor_name:
        doc_lower = doctor_name.strip().lower()
        records = [r for r in records if doc_lower in (r.get("Doctor") or r.get("Doctor Name") or "").lower()]
    return records

@router.post("/appointments")
def create_appointment(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "doctor_appointments", payload)

@router.delete("/appointments/{record_id}")
def delete_appointment(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "doctor_appointments", record_id)


# 2. Patient History
@router.get("/patient-history")
def get_patient_history(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Date": "2026-08-13", "Patient Name": "Aarav Kumar", "Diagnosis": "Hypertension Stage 1", "Notes": "Prescribed Telmisartan 40mg once daily."}
    ]
    return get_generic_records(db, "doctor_history", defaults)

@router.post("/patient-history")
def create_patient_history(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "doctor_history", payload)

@router.delete("/patient-history/{record_id}")
def delete_patient_history(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "doctor_history", record_id)


# 3. Diagnosis
@router.get("/diagnosis")
def get_diagnosis(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "ICD Code": "I10", "Description": "Essential hypertension", "Severity": "Moderate"}
    ]
    return get_generic_records(db, "doctor_diagnosis", defaults)

@router.post("/diagnosis")
def create_diagnosis(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "doctor_diagnosis", payload)

@router.delete("/diagnosis/{record_id}")
def delete_diagnosis(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "doctor_diagnosis", record_id)


# 4. Prescription
@router.get("/prescriptions")
def get_prescriptions(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Doctor": "Dr. Priya Nair", "Medicines": "Paracetamol 650mg, Amoxicillin 500mg", "Duration": "5 Days", "Date": "2026-08-13"}
    ]
    return get_generic_records(db, "doctor_prescriptions", defaults)

@router.post("/prescriptions")
def create_prescription(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "doctor_prescriptions", payload)

@router.delete("/prescriptions/{record_id}")
def delete_prescription(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "doctor_prescriptions", record_id)


# 5. Lab Test Request
@router.get("/lab-test-request")
def get_lab_test_requests(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Test Name": "CBC Blood Profile", "Priority": "Normal", "Status": "Requested"}
    ]
    return get_generic_records(db, "doctor_lab_requests", defaults)

@router.post("/lab-test-request")
def create_lab_test_request(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "doctor_lab_requests", payload)

@router.delete("/lab-test-request/{record_id}")
def delete_lab_test_request(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "doctor_lab_requests", record_id)


# 6. Follow-up Schedule
@router.get("/follow-up")
def get_followups(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Doctor": "Dr. Priya Nair", "Next Visit Date": "2026-08-27", "Reason": "BP Re-assessment", "Status": "Scheduled"}
    ]
    return get_generic_records(db, "doctor_followup", defaults)

@router.post("/follow-up")
def create_followup(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "doctor_followup", payload)

@router.delete("/follow-up/{record_id}")
def delete_followup(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "doctor_followup", record_id)
