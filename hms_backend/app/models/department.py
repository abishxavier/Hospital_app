from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship

from hms_backend.app.core.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)

    users = relationship("User", back_populates="department")
    appointments = relationship("Appointment", back_populates="department")
