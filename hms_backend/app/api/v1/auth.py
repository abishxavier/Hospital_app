from fastapi import APIRouter, HTTPException, status

from hms_backend.app.core.security import create_access_token
from hms_backend.app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    email = payload.email.lower()
    password = payload.password

    if email == "admin@hospital.app" and password == "admin123":
        token = create_access_token("admin", role="admin", name="Demo Admin")
        return TokenResponse(token=token, role="admin", name="Demo Admin")

    if email == "reception@hospital.app" and password == "reception123":
        token = create_access_token("reception", role="reception", name="Demo Reception")
        return TokenResponse(token=token, role="reception", name="Demo Reception")

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password",
    )
