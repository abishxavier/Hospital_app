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
        "admin@hospital.com": {"name": "Dr. Sarah Johnson", "role": "admin", "password": "admin123"},
        "admin": {"name": "Dr. Sarah Johnson", "role": "admin", "password": "admin123"},
        
        # 5 Doctors
        "madhavan@hospital.org": {"name": "Dr. Madhavan", "role": "doctor", "password": "doctor123"},
        "doctor@hospital.com": {"name": "Dr. Madhavan", "role": "doctor", "password": "doctor123"},
        "doctor": {"name": "Dr. Madhavan", "role": "doctor", "password": "doctor123"},
        "karthikeyan@hospital.org": {"name": "Dr. S. Karthikeyan", "role": "doctor", "password": "doctor123"},
        "murugan@hospital.org": {"name": "Dr. Murugan Jeyaraman", "role": "doctor", "password": "doctor123"},
        "rajkanna@hospital.org": {"name": "Dr. Raj Kanna", "role": "doctor", "password": "doctor123"},
        "priyanair@hospital.org": {"name": "Dr. Priya Nair", "role": "doctor", "password": "doctor123"},

        # 5 Nurses
        "nurse@hospital.com": {"name": "Selvi. V. Mary", "role": "nurse", "password": "nurse123"},
        "nurse": {"name": "Selvi. V. Mary", "role": "nurse", "password": "nurse123"},
        "selvi.mary@hospital.org": {"name": "Selvi. V. Mary", "role": "nurse", "password": "nurse123"},
        "kavitha.r@hospital.org": {"name": "Kavitha. R.", "role": "nurse", "password": "nurse123"},
        "lakshmi.p@hospital.org": {"name": "Lakshmi. P", "role": "nurse", "password": "nurse123"},
        "priya.s@hospital.org": {"name": "Priya. S", "role": "nurse", "password": "nurse123"},
        "anandhi.k@hospital.org": {"name": "Anandhi. K", "role": "nurse", "password": "nurse123"},

        # 2 Receptionists
        "reception@hospital.com": {"name": "Rajesh", "role": "receptionist", "password": "reception123"},
        "reception": {"name": "Rajesh", "role": "receptionist", "password": "reception123"},
        "rajesh@hospital.org": {"name": "Rajesh", "role": "receptionist", "password": "reception123"},
        "pooja.v@hospital.org": {"name": "Pooja Venkatesh", "role": "receptionist", "password": "reception123"},

        # Lab Tech & Pharmacist
        "lab@hospital.com": {"name": "Anil Mehta", "role": "laboratory", "password": "lab123"},
        "lab": {"name": "Anil Mehta", "role": "laboratory", "password": "lab123"},
        "pharmacy123@hospital.org": {"name": "Vikram Singh", "role": "pharmacy", "password": "pharmacy123"}
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
        if request.password in [demo["password"], f"{demo['password']}123", "doctor123", "doctor", "admin123", "admin", "nurse123", "reception123", "demo"]:
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

