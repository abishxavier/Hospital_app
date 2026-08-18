from pydantic import BaseModel
from typing import Optional


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    status: str = "Scheduled"
    appointment_type: str = "Routine Consultation"
    notes: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    appointment_code: Optional[str] = None
    queue_number: Optional[int] = None

    class Config:
        from_attributes = True
