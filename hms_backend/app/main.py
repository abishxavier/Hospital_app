from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from hms_backend.app.core.database import Base, engine
from hms_backend.app.models.appointment import Appointment
from hms_backend.app.models.patient import Patient
from hms_backend.app.models.user import User
from hms_backend.app.models.department import Department
from hms_backend.app.models.consultation import Diagnosis, Prescription, LabTestRequest

from hms_backend.app.routers import (
    admin, reception, doctor, nurse, laboratory, pharmacy, inpatient, billing, portal
)

app = FastAPI(title="Hospital Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router)
app.include_router(reception.router)
app.include_router(doctor.router)
app.include_router(nurse.router)
app.include_router(laboratory.router)
app.include_router(pharmacy.router)
app.include_router(inpatient.router)
app.include_router(billing.router)
app.include_router(portal.router)


@app.get("/")
def read_root():
    return {"message": "Hospital Management API is running"}


@app.get("/health")
def health_check():
    with engine.begin() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok"}


@app.post("/api/auth/login")
def login():
    return {"token": "demo-token", "role": "admin", "name": "Demo Admin"}


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
