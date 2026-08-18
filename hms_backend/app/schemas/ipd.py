from pydantic import BaseModel
from typing import Optional


class WardBase(BaseModel):
    name: str
    ward_type: str = "General"
    total_beds: int = 10
    occupied_beds: int = 0
    nurse_in_charge: Optional[str] = None


class WardResponse(WardBase):
    id: int

    class Config:
        from_attributes = True


class BedBase(BaseModel):
    bed_number: str
    ward_id: int
    status: str = "Available"


class BedResponse(BedBase):
    id: int

    class Config:
        from_attributes = True


class AdmissionBase(BaseModel):
    patient_id: int
    bed_id: Optional[int] = None
    attending_doctor: Optional[str] = None
    status: str = "Admitted"


class AdmissionResponse(AdmissionBase):
    id: int
    admission_code: Optional[str] = None

    class Config:
        from_attributes = True
