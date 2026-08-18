from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from hms_backend.app.core.database import Base


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    full_name = Column(String(120), nullable=False)
    role = Column(String(50), nullable=False)
    shift = Column(String(50), default="Morning Shift")
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    phone = Column(String(20), nullable=True)
    status = Column(String(50), default="Active")

    department = relationship("Department", back_populates="staff")
