from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(prefix="/reception", tags=["reception"])


# 1. Queue Management
@router.get("/queue")
def get_queue(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Token No": "TK-01", "Patient": "Aarav Kumar", "Doctor": "Dr. Priya Nair", "Est. Time": "10:30 AM", "Status": "In Consultation"}
    ]
    return get_generic_records(db, "reception_queue", defaults)


@router.post("/queue")
def create_queue(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "reception_queue", payload)


@router.delete("/queue/{queue_id}")
def delete_queue(queue_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "reception_queue", queue_id)


# 2. OP/IP Registration
@router.get("/op-ip")
def get_op_ip(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient Name": "Aarav Kumar", "Type": "Outpatient (OP)", "Department": "Cardiology", "Status": "Checked In"}
    ]
    return get_generic_records(db, "reception_op_ip", defaults)


@router.post("/op-ip")
def create_op_ip(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "reception_op_ip", payload)


@router.delete("/op-ip/{op_ip_id}")
def delete_op_ip(op_ip_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "reception_op_ip", op_ip_id)
