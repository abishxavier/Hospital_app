from fastapi import APIRouter

from hms_backend.app.api.v1.auth import router as auth_router
from hms_backend.app.api.v1.appointments import router as appointments_router
from hms_backend.app.api.v1.patients import router as patients_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(patients_router)
api_router.include_router(appointments_router)
