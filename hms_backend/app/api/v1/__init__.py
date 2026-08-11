from .auth import router as auth_router
from .appointments import router as appointments_router
from .patients import router as patients_router

__all__ = ["auth_router", "appointments_router", "patients_router"]
