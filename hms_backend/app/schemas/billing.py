from pydantic import BaseModel
from typing import Optional


class InvoiceBase(BaseModel):
    invoice_code: str
    patient_name: str
    total_amount: float = 0.0
    due_date: Optional[str] = None
    status: str = "Pending"


class InvoiceResponse(InvoiceBase):
    id: int

    class Config:
        from_attributes = True


class PaymentBase(BaseModel):
    transaction_code: str
    patient_name: str
    amount: float = 0.0
    method: str = "Cash"
    status: str = "Completed"


class PaymentResponse(PaymentBase):
    id: int

    class Config:
        from_attributes = True
