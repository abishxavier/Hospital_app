from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from hms_backend.app.core.database import Base, engine
from hms_backend.app.models.appointment import Appointment
from hms_backend.app.models.patient import Patient
from hms_backend.app.models.user import User

app = FastAPI(title="Hospital Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hospital Management API is running"}


@app.get("/health")
def health_check():
    with engine.begin() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok"}


@app.get("/api/dashboard")
def dashboard_summary():
    return {
        "patients": 124,
        "appointments": 38,
        "revenue": 18420,
        "occupancy": 67,
    }


@app.post("/api/auth/login")
def login():
    return {"token": "demo-token", "role": "admin", "name": "Demo Admin"}


@app.get("/api/patients")
def list_patients():
    return [
        {"id": 1, "full_name": "Aarav Kumar", "phone": "+91 9876543210", "gender": "Male"},
        {"id": 2, "full_name": "Meera Shah", "phone": "+91 9123456780", "gender": "Female"},
    ]


@app.get("/api/appointments")
def list_appointments():
    return [
        {"id": 1, "patient_name": "Aarav Kumar", "doctor_name": "Dr. Nair", "status": "scheduled"},
        {"id": 2, "patient_name": "Meera Shah", "doctor_name": "Dr. Rao", "status": "checked_in"},
    ]


@app.get("/api/staff")
def list_staff():
    return [
        {"id": 1, "full_name": "Naina Das", "role": "admin", "email": "naina@hospital.app"},
        {"id": 2, "full_name": "Rohan Menon", "role": "doctor", "email": "rohan@hospital.app"},
    ]


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
