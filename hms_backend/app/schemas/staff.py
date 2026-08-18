from pydantic import BaseModel
from typing import Optional


class StaffBase(BaseModel):
    full_name: str
    role: str
    shift: str = "Morning Shift"
    department_id: Optional[int] = None
    phone: Optional[str] = None
    status: str = "Active"


class StaffCreate(StaffBase):
    pass


class StaffResponse(StaffBase):
    id: int

    class Config:
        from_attributes = True
