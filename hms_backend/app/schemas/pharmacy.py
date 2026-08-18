from pydantic import BaseModel
from typing import Optional
from datetime import date


class MedicineBase(BaseModel):
    name: str
    batch_no: str
    expiry_date: Optional[date] = None
    stock_qty: int = 0
    unit_price: float = 0.0
    status: str = "Available"


class MedicineCreate(MedicineBase):
    pass


class MedicineResponse(MedicineBase):
    id: int

    class Config:
        from_attributes = True


class StockTransactionCreate(BaseModel):
    medicine_name: str
    change_qty: int
    transaction_type: str = "Deduction"
    reason: Optional[str] = None
