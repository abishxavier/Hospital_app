from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from hms_backend.app.core.database import Base


class Ambulance(Base):
    __tablename__ = "ambulances"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_number = Column(String(50), unique=True, nullable=False)
    driver_name = Column(String(120), nullable=False)
    driver_phone = Column(String(20), nullable=False)
    status = Column(String(50), default="Available")


class EmergencyBooking(Base):
    __tablename__ = "emergency_bookings"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(120), nullable=False)
    pickup_location = Column(String(255), nullable=False)
    ambulance_vehicle = Column(String(50), nullable=True)
    status = Column(String(50), default="Dispatched")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
