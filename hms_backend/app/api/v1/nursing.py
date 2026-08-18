from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(tags=["nurse"])


# 1. Patient Vitals
@router.get("/nurse/patient-vitals")
@router.get("/nurse/vitals")
@router.get("/nursing/vitals")
def get_patient_vitals(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "BP": "120/80 mmHg", "Heart Rate": "72 bpm", "Temp": "98.6 °F", "Pain Scale": "2/10 (Mild)", "RBS": "110 mg/dL", "SpO2": "98%", "Recorded At": "09:00 AM"}
    ]
    return get_generic_records(db, "nurse_vitals", defaults)

@router.post("/nurse/patient-vitals")
@router.post("/nursing/vitals")
def create_patient_vitals(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "nurse_vitals", payload)

@router.delete("/nurse/patient-vitals/{record_id}")
@router.delete("/nursing/vitals/{record_id}")
def delete_patient_vitals(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "nurse_vitals", record_id)


# 2. Ward Management
@router.get("/nurse/ward-management")
@router.get("/nursing/ward-management")
def get_ward_management(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Ward Name": "ICU Block A", "Total Beds": "10 Beds", "Occupied": "8 Occupied", "Nurse In-charge": "Sunita Rao"}
    ]
    return get_generic_records(db, "nurse_wards", defaults)

@router.post("/nurse/ward-management")
@router.post("/nursing/ward-management")
def create_ward_management(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "nurse_wards", payload)

@router.delete("/nurse/ward-management/{record_id}")
@router.delete("/nursing/ward-management/{record_id}")
def delete_ward_management(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "nurse_wards", record_id)


# 3. Medication Admin
@router.get("/nurse/medication-admin")
@router.get("/nurse/medications")
@router.get("/nursing/medications")
def get_medication_admin(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Siddharth Roy", "Medicine": "IV Ceftriaxone 1g", "Dosage": "1 Vial", "Administered By": "Sunita Rao", "Time": "08:00 AM"}
    ]
    return get_generic_records(db, "nurse_med_admin", defaults)

@router.post("/nurse/medication-admin")
@router.post("/nursing/medications")
def create_medication_admin(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "nurse_med_admin", payload)

@router.delete("/nurse/medication-admin/{record_id}")
@router.delete("/nursing/medications/{record_id}")
def delete_medication_admin(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "nurse_med_admin", record_id)


# 4. Nursing Notes
@router.get("/nurse/nursing-notes")
@router.get("/nurse/notes")
@router.get("/nursing/notes")
def get_nursing_notes(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Siddharth Roy", "Notes": "Patient reports mild incision pain. Vitals stable.", "Added By": "Sunita Rao", "Date": "2026-08-13"}
    ]
    return get_generic_records(db, "nurse_notes", defaults)

@router.post("/nurse/nursing-notes")
@router.post("/nursing/notes")
def create_nursing_notes(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "nurse_notes", payload)

@router.delete("/nurse/nursing-notes/{record_id}")
@router.delete("/nursing/notes/{record_id}")
def delete_nursing_notes(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "nurse_notes", record_id)
