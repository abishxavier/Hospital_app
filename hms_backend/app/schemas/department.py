from pydantic import BaseModel
from typing import Optional


class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None
    head_of_dept: Optional[str] = None
    total_staff: int = 0
    status: str = "Active"


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True
