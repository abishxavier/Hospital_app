from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.core.security import create_access_token, verify_password, hash_password
from hms_backend.app.models.user import User
from hms_backend.app.schemas.user import LoginRequest, Token, UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    DEMO_USERS = {
        "admin@hospital.com": {"name": "Dr. Sarah Johnson", "role": "admin", "password": "admin"},
        "admin": {"name": "Dr. Sarah Johnson", "role": "admin", "password": "admin"},
        "doctor@hospital.com": {"name": "Dr. Priya Nair", "role": "doctor", "password": "doctor"},
        "doctor": {"name": "Dr. Priya Nair", "role": "doctor", "password": "doctor"},
        "reception@hospital.com": {"name": "Sunita Sharma", "role": "receptionist", "password": "reception"},
        "reception": {"name": "Sunita Sharma", "role": "receptionist", "password": "reception"},
        "receptionist@hospital.com": {"name": "Sunita Sharma", "role": "receptionist", "password": "reception"},
        "lab@hospital.com": {"name": "Anil Mehta", "role": "laboratory", "password": "lab"},
        "lab": {"name": "Anil Mehta", "role": "laboratory", "password": "lab"},
        "laboratory@hospital.com": {"name": "Anil Mehta", "role": "laboratory", "password": "lab"},
        "nurse@hospital.com": {"name": "Nurse Sunita Rao", "role": "nurse", "password": "nurse"},
        "nurse": {"name": "Nurse Sunita Rao", "role": "nurse", "password": "nurse"}
    }

    user = db.query(User).filter(User.email == request.username).first()
    
    if not user and request.username in DEMO_USERS:
        demo = DEMO_USERS[request.username]
        user = User(
            full_name=demo["name"],
            email=request.username if "@" in request.username else f"{request.username}@hospital.com",
            password_hash=hash_password(demo["password"]),
            role=demo["role"]
        )
        db.add(user)
        try:
            db.commit()
            db.refresh(user)
        except Exception:
            db.rollback()

    if user and verify_password(request.password, user.password_hash):
        token = create_access_token({"sub": user.email, "role": user.role})
        return Token(access_token=token, role=user.role, name=user.full_name)

    # Demo fallback authentication
    if request.username in DEMO_USERS:
        demo = DEMO_USERS[request.username]
        if request.password in [demo["password"], f"{demo['password']}123", "admin", "demo"]:
            token = create_access_token({"sub": request.username, "role": demo["role"]})
            return Token(access_token=token, role=demo["role"], name=demo["name"])

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
    )


@router.get("/me")
def get_me():
    return {
        "id": 1,
        "full_name": "Dr. Sarah Johnson",
        "email": "sarah.johnson@hospital.org",
        "role": "admin",
        "department": "Cardiology",
        "status": "Active"
    }

