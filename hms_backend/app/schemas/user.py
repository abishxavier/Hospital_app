from pydantic import BaseModel, EmailStr, Field


class UserRead(BaseModel):
    id: int
    full_name: str = Field(..., min_length=2)
    email: EmailStr
    role: str
    is_active: bool = True

    class Config:
        from_attributes = True
