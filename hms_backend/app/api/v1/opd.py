from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import get_generic_records

router = APIRouter(prefix="/opd", tags=["opd"])


@router.get("/queue")
def get_opd_queue(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Token No": "TK-01", "Patient": "Aarav Kumar", "Doctor": "Dr. Priya Nair", "Est. Time": "10:30 AM", "Status": "In Consultation"},
        {"id": 2, "Token No": "TK-02", "Patient": "Meera Shah", "Doctor": "Dr. Priya Nair", "Est. Time": "10:45 AM", "Status": "Waiting"},
    ]
    return get_generic_records(db, "reception_queue", defaults)
