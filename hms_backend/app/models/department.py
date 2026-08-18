from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from hms_backend.app.core.database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    head_of_dept = Column(String(120), nullable=True)
    total_staff = Column(Integer, default=0)
    status = Column(String(50), default="Active")

    users = relationship("User", back_populates="department")
    doctors = relationship("Doctor", back_populates="department")
    staff = relationship("Staff", back_populates="department")
