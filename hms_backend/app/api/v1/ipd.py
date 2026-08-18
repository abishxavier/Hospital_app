from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(tags=["inpatient"])


# 1. Room Allocation
@router.get("/inpatient/room-allocation")
@router.get("/inpatient/rooms")
@router.get("/ipd/rooms")
@router.get("/ipd/room-allocation")
def get_room_allocations(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Room No": "Room 101", "Ward Type": "Deluxe Private", "Patient": "Siddharth Roy", "Status": "Occupied"}
    ]
    return get_generic_records(db, "ipd_rooms", defaults)

@router.post("/inpatient/room-allocation")
@router.post("/ipd/room-allocation")
def create_room_allocation(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "ipd_rooms", payload)

@router.delete("/inpatient/room-allocation/{record_id}")
@router.delete("/ipd/room-allocation/{record_id}")
def delete_room_allocation(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "ipd_rooms", record_id)


# 2. Admission
@router.get("/inpatient/admissions")
@router.get("/ipd/admissions")
def get_admissions(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Admission ID": "IPD-301", "Patient": "Siddharth Roy", "Admitted Date": "2026-08-10", "Attending Doctor": "Dr. Vikram Malhotra", "Status": "Admitted"}
    ]
    return get_generic_records(db, "ipd_admissions", defaults)

@router.post("/inpatient/admissions")
@router.post("/ipd/admissions")
def create_admission(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "ipd_admissions", payload)

@router.delete("/inpatient/admissions/{record_id}")
@router.delete("/ipd/admissions/{record_id}")
def delete_admission(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "ipd_admissions", record_id)


# 3. Treatment Records
@router.get("/inpatient/treatment-records")
@router.get("/ipd/treatment-records")
def get_treatment_records(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Siddharth Roy", "Treatment Details": "Knee Surgery", "Date": "2026-08-11", "Doctor": "Dr. Vikram Malhotra"}
    ]
    return get_generic_records(db, "ipd_treatments", defaults)

@router.post("/inpatient/treatment-records")
@router.post("/ipd/treatment-records")
def create_treatment_record(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "ipd_treatments", payload)

@router.delete("/inpatient/treatment-records/{record_id}")
@router.delete("/ipd/treatment-records/{record_id}")
def delete_treatment_record(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "ipd_treatments", record_id)


# 4. Daily Progress
@router.get("/inpatient/daily-progress")
@router.get("/ipd/daily-progress")
def get_daily_progress(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Siddharth Roy", "Progress Note": "Post-op Day 1: Wound clean, active motion exercises started.", "Added By": "Dr. Vikram Malhotra", "Date": "2026-08-13"}
    ]
    return get_generic_records(db, "ipd_progress", defaults)

@router.post("/inpatient/daily-progress")
@router.post("/ipd/daily-progress")
def create_daily_progress(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "ipd_progress", payload)

@router.delete("/inpatient/daily-progress/{record_id}")
@router.delete("/ipd/daily-progress/{record_id}")
def delete_daily_progress(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "ipd_progress", record_id)


# 5. Discharge Summary
@router.get("/inpatient/discharge-summary")
@router.get("/ipd/discharge-summary")
def get_discharge_summaries(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Karan Malhotra", "Discharge Date": "2026-08-13", "Summary Status": "Completed", "Prepared By": "Dr. Robert Chen"}
    ]
    return get_generic_records(db, "ipd_discharge", defaults)

@router.post("/inpatient/discharge-summary")
@router.post("/ipd/discharge-summary")
def create_discharge_summary(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "ipd_discharge", payload)

@router.delete("/inpatient/discharge-summary/{record_id}")
@router.delete("/ipd/discharge-summary/{record_id}")
def delete_discharge_summary(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "ipd_discharge", record_id)
