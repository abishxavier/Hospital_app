from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from hms_backend.app.core.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_name = Column(String(120), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    status = Column(String(30), default="scheduled")

    patient = relationship("Patient", back_populates="appointments")
