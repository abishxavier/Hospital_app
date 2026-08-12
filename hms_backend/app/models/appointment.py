from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from hms_backend.app.core.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    doctor_name = Column(String(120), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    status = Column(String(30), default="scheduled")
    queue_number = Column(Integer, nullable=True)
    is_opd = Column(Boolean, default=True)

    patient = relationship("Patient", back_populates="appointments")
    department = relationship("Department", back_populates="appointments")
