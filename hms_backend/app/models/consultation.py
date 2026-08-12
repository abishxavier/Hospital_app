from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from hms_backend.app.core.database import Base


class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    appointment = relationship("Appointment")
    doctor = relationship("User")


class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)
    medicine_name = Column(String(255), nullable=False)
    dosage = Column(String(100), nullable=False)
    duration = Column(String(100), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    appointment = relationship("Appointment")


class LabTestRequest(Base):
    __tablename__ = "lab_test_requests"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)
    test_name = Column(String(255), nullable=False)
    status = Column(String(50), default="pending")  # pending, collected, completed
    created_at = Column(DateTime, default=datetime.utcnow)

    appointment = relationship("Appointment")
