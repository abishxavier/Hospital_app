from datetime import datetime

from pydantic import BaseModel, Field


class AppointmentRead(BaseModel):
    id: int
    patient_id: int
    doctor_name: str = Field(..., min_length=2)
    appointment_date: datetime
    status: str = "scheduled"

    class Config:
        from_attributes = True
