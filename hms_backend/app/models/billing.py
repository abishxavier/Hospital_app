from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone
from hms_backend.app.core.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_code = Column(String(50), unique=True, index=True, nullable=False)
    patient_name = Column(String(120), nullable=False)
    total_amount = Column(Float, default=0.0)
    due_date = Column(String(50), nullable=True)
    status = Column(String(50), default="Pending")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    transaction_code = Column(String(50), unique=True, index=True, nullable=False)
    patient_name = Column(String(120), nullable=False)
    amount = Column(Float, default=0.0)
    method = Column(String(50), default="Cash")
    status = Column(String(50), default="Completed")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
