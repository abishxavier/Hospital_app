from pydantic import BaseModel
from typing import Optional


class PrescriptionBase(BaseModel):
    patient_name: str
    doctor_name: str
    medicines: str
    duration: str = "5 Days"
    status: str = "Prescribed"


class PrescriptionCreate(PrescriptionBase):
    pass


class PrescriptionResponse(PrescriptionBase):
    id: int

    class Config:
        from_attributes = True
