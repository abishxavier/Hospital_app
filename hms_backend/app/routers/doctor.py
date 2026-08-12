from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from hms_backend.app.core.database import get_db

router = APIRouter(prefix="/api/doctor", tags=["doctor"])

@router.get("/appointments")
def get_doctor_appointments(db: Session = Depends(get_db)):
    return [
        {"id": 1, "patient_name": "Aarav Kumar", "time": "10:00 AM", "status": "waiting"},
        {"id": 3, "patient_name": "Rohan Patel", "time": "11:30 AM", "status": "scheduled"},
    ]

@router.post("/consultation/{appointment_id}/diagnosis")
def add_diagnosis(appointment_id: int, db: Session = Depends(get_db)):
    # Mocking diagnosis creation
    return {"status": "success", "message": "Diagnosis saved."}

@router.post("/consultation/{appointment_id}/prescription")
def add_prescription(appointment_id: int, db: Session = Depends(get_db)):
    # Mocking prescription creation
    return {"status": "success", "message": "Prescription added."}

@router.post("/consultation/{appointment_id}/lab-test")
def order_lab_test(appointment_id: int, db: Session = Depends(get_db)):
    # Mocking lab test request
    return {"status": "success", "message": "Lab test ordered."}
