from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from hms_backend.app.core.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(120), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(120), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)

    appointments = relationship("Appointment", back_populates="patient")
