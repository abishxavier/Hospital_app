from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from datetime import datetime, timezone
from hms_backend.app.core.database import Base


class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(120), nullable=False)
    doctor_name = Column(String(120), nullable=False)
    medicines = Column(Text, nullable=False)
    duration = Column(String(50), default="5 Days")
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    status = Column(String(50), default="Prescribed")
