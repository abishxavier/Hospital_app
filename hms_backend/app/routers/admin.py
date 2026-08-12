from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from hms_backend.app.core.database import get_db

router = APIRouter(prefix="/api/admin", tags=["admin"])

@router.get("/dashboard")
def get_dashboard(db: Session = Depends(get_db)):
    # Mocking real DB queries for now
    return {
        "patients": 150,
        "appointments": 45,
        "revenue": 21500,
        "occupancy": 72,
    }

@router.get("/departments")
def get_departments(db: Session = Depends(get_db)):
    # Query departments
    # Mock for now
    return [
        {"id": 1, "name": "Cardiology"},
        {"id": 2, "name": "Neurology"},
        {"id": 3, "name": "Pediatrics"},
    ]

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return [
        {"id": 1, "full_name": "Admin User", "role": "admin", "email": "admin@hospital.com"},
        {"id": 2, "full_name": "Reception User", "role": "reception", "email": "reception@hospital.com"},
    ]
