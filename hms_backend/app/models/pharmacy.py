from sqlalchemy import Column, Integer, String, Float, Date
from hms_backend.app.core.database import Base


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    batch_no = Column(String(50), nullable=False)
    expiry_date = Column(Date, nullable=True)
    stock_qty = Column(Integer, default=0)
    unit_price = Column(Float, default=0.0)
    status = Column(String(50), default="Available")


class StockTransaction(Base):
    __tablename__ = "stock_transactions"

    id = Column(Integer, primary_key=True, index=True)
    medicine_name = Column(String(120), nullable=False)
    change_qty = Column(Integer, nullable=False)
    transaction_type = Column(String(50), default="Deduction")
    reason = Column(String(255), nullable=True)
