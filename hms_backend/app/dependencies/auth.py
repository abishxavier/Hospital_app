from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.core.security import decode_access_token
from hms_backend.app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """Decodes JWT token and retrieves the current authenticated user."""
    if not token:
        # Demo fallback user for ease of frontend testing
        demo_user = db.query(User).filter(User.email == "admin@hospital.com").first()
        if demo_user:
            return demo_user
        return User(id=1, full_name="Demo Admin", email="admin@hospital.com", role="admin")

    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.query(User).filter(User.email == payload["sub"]).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user


def require_role(required_role: str):
    """Enforces role-based access control."""
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != "admin" and current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Operation not permitted for role: {current_user.role}",
            )
        return current_user
    return role_checker
