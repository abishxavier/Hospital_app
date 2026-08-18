from pydantic import BaseModel
from typing import Optional


class TestRequestBase(BaseModel):
    req_code: str
    patient_name: str
    test_type: str
    priority: str = "Normal"
    requested_by: Optional[str] = None
    status: str = "Requested"


class TestRequestResponse(TestRequestBase):
    id: int

    class Config:
        from_attributes = True


class LabReportBase(BaseModel):
    test_id: int
    patient_name: str
    result_summary: str
    verified_by: Optional[str] = None
    status: str = "Verified"


class LabReportResponse(LabReportBase):
    id: int

    class Config:
        from_attributes = True
