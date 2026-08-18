from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from hms_backend.app.core.database import Base


class OPDVisit(Base):
    __tablename__ = "opd_visits"

    id = Column(Integer, primary_key=True, index=True)
    token_no = Column(String(50), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=True)
    estimated_time = Column(String(50), nullable=True)
    status = Column(String(50), default="Waiting")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    patient = relationship("Patient", back_populates="opd_visits")
