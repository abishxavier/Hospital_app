from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime, timezone
from hms_backend.app.core.database import Base


class TestRequest(Base):
    __tablename__ = "test_requests"

    id = Column(Integer, primary_key=True, index=True)
    req_code = Column(String(50), nullable=False)
    patient_name = Column(String(120), nullable=False)
    test_type = Column(String(100), nullable=False)
    priority = Column(String(50), default="Normal")
    requested_by = Column(String(120), nullable=True)
    status = Column(String(50), default="Requested")


class LabReport(Base):
    __tablename__ = "lab_reports"

    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, nullable=False)
    patient_name = Column(String(120), nullable=False)
    result_summary = Column(Text, nullable=False)
    verified_by = Column(String(120), nullable=True)
    status = Column(String(50), default="Verified")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
