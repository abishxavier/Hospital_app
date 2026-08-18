from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from hms_backend.app.core.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    full_name = Column(String(120), nullable=False)
    specialization = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    availability = Column(String(50), default="Available")
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

    department = relationship("Department", back_populates="doctors")
    appointments = relationship("Appointment", back_populates="doctor")
