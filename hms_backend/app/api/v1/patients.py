from fastapi import APIRouter, Depends

from hms_backend.app.dependencies.auth import require_role
from hms_backend.app.schemas.patient import PatientCreate, PatientRead

router = APIRouter(prefix="/patients", tags=["patients"])


mock_patients = [
    {
        "id": 1,
        "full_name": "Aarav Kumar",
        "phone": "+91 9876543210",
        "email": "aarav@example.com",
        "date_of_birth": "1998-04-12",
        "gender": "Male",
        "address": "Koramangala, Bengaluru",
    },
    {
        "id": 2,
        "full_name": "Meera Shah",
        "phone": "+91 9123456780",
        "email": "meera@example.com",
        "date_of_birth": "1989-08-03",
        "gender": "Female",
        "address": "Banjara Hills, Hyderabad",
    },
]


@router.get(
    "/",
    response_model=list[PatientRead],
    dependencies=[Depends(require_role("admin", "reception", "doctor"))],
)
def list_patients():
    return mock_patients


@router.post(
    "/",
    response_model=PatientRead,
    dependencies=[Depends(require_role("admin", "reception"))],
)
def create_patient(payload: PatientCreate):
    patient = {**payload.model_dump(), "id": len(mock_patients) + 1}
    mock_patients.append(patient)
    return patient
