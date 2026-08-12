from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from hms_backend.app.core.database import get_db

router = APIRouter(prefix="/api/reception", tags=["reception"])

@router.get("/patients")
def get_patients(db: Session = Depends(get_db)):
    return [
        {"id": 1, "full_name": "Aarav Kumar", "phone": "+91 9876543210", "gender": "Male"},
        {"id": 2, "full_name": "Meera Shah", "phone": "+91 9123456780", "gender": "Female"},
    ]

@router.post("/patients")
def register_patient(db: Session = Depends(get_db)):
    # Mocking patient registration
    return {"status": "success", "message": "Patient registered successfully."}

@router.get("/appointments")
def get_appointments(db: Session = Depends(get_db)):
    return [
        {"id": 1, "patient_name": "Aarav Kumar", "doctor_name": "Dr. Nair", "status": "scheduled", "queue_number": 1},
        {"id": 2, "patient_name": "Meera Shah", "doctor_name": "Dr. Rao", "status": "checked_in", "queue_number": 2},
    ]

@router.post("/appointments")
def book_appointment(db: Session = Depends(get_db)):
    # Mocking appointment booking
    return {"status": "success", "message": "Appointment booked successfully."}
