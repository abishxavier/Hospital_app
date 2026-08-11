from fastapi import APIRouter, Depends, HTTPException, status

from hms_backend.app.dependencies.auth import require_role
from hms_backend.app.schemas.appointment import AppointmentRead

router = APIRouter(prefix="/appointments", tags=["appointments"])


mock_appointments = [
    {
        "id": 1,
        "patient_id": 1,
        "doctor_name": "Dr. Nair",
        "appointment_date": "2026-08-10T09:30:00",
        "status": "scheduled",
    },
    {
        "id": 2,
        "patient_id": 2,
        "doctor_name": "Dr. Rao",
        "appointment_date": "2026-08-10T11:00:00",
        "status": "checked_in",
    },
]


@router.get(
    "/",
    response_model=list[AppointmentRead],
    dependencies=[Depends(require_role("admin", "reception", "doctor", "nurse"))],
)
def list_appointments():
    return mock_appointments


@router.get(
    "/{appointment_id}",
    response_model=AppointmentRead,
    dependencies=[Depends(require_role("admin", "reception", "doctor", "nurse"))],
)
def get_appointment(appointment_id: int):
    for appointment in mock_appointments:
        if appointment["id"] == appointment_id:
            return appointment
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Appointment {appointment_id} not found",
    )
