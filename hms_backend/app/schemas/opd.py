from pydantic import BaseModel
from typing import Optional


class OPDVisitBase(BaseModel):
    token_no: str
    patient_id: int
    doctor_id: Optional[int] = None
    estimated_time: Optional[str] = None
    status: str = "Waiting"


class OPDVisitCreate(OPDVisitBase):
    pass


class OPDVisitResponse(OPDVisitBase):
    id: int

    class Config:
        from_attributes = True
