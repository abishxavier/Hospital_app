from pydantic import BaseModel
from typing import Optional


class AmbulanceBase(BaseModel):
    vehicle_number: str
    driver_name: str
    driver_phone: str
    status: str = "Available"


class AmbulanceResponse(AmbulanceBase):
    id: int

    class Config:
        from_attributes = True


class EmergencyBookingBase(BaseModel):
    patient_name: str
    pickup_location: str
    ambulance_vehicle: Optional[str] = None
    status: str = "Dispatched"


class EmergencyBookingResponse(EmergencyBookingBase):
    id: int

    class Config:
        from_attributes = True
