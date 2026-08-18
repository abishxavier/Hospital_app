from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from hms_backend.app.core.database import Base


class Ward(Base):
    __tablename__ = "wards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    ward_type = Column(String(50), default="General")
    total_beds = Column(Integer, default=10)
    occupied_beds = Column(Integer, default=0)
    nurse_in_charge = Column(String(120), nullable=True)

    beds = relationship("Bed", back_populates="ward")


class Bed(Base):
    __tablename__ = "beds"

    id = Column(Integer, primary_key=True, index=True)
    bed_number = Column(String(50), nullable=False)
    ward_id = Column(Integer, ForeignKey("wards.id"), nullable=False)
    status = Column(String(50), default="Available")

    ward = relationship("Ward", back_populates="beds")
    admissions = relationship("Admission", back_populates="bed")


class Admission(Base):
    __tablename__ = "admissions"

    id = Column(Integer, primary_key=True, index=True)
    admission_code = Column(String(50), unique=True, index=True, nullable=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    bed_id = Column(Integer, ForeignKey("beds.id"), nullable=True)
    attending_doctor = Column(String(120), nullable=True)
    admitted_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    discharge_date = Column(DateTime, nullable=True)
    status = Column(String(50), default="Admitted")

    patient = relationship("Patient", back_populates="admissions")
    bed = relationship("Bed", back_populates="admissions")
