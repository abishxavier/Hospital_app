from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(prefix="/laboratory", tags=["laboratory"])


# 1. Test Request
@router.get("/test-request")
@router.get("/requests")
def get_test_requests(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Req ID": "LAB-401", "Patient": "Aarav Kumar", "Test Type": "CBC Blood Profile", "Priority": "Normal", "Requested By": "Dr. Priya Nair"}
    ]
    return get_generic_records(db, "lab_requests", defaults)

@router.post("/test-request")
def create_test_request(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "lab_requests", payload)

@router.delete("/test-request/{record_id}")
def delete_test_request(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "lab_requests", record_id)


# 2. Sample Collection
@router.get("/sample-collection")
@router.get("/samples")
def get_sample_collections(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Sample ID": "SMP-991", "Patient": "Aarav Kumar", "Test Name": "CBC Blood Sample", "Collected By": "Anil Mehta", "Status": "Collected"}
    ]
    return get_generic_records(db, "lab_samples", defaults)

@router.post("/sample-collection")
def create_sample_collection(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "lab_samples", payload)

@router.delete("/sample-collection/{record_id}")
def delete_sample_collection(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "lab_samples", record_id)


# 3. Report Entry
@router.get("/report-entry")
@router.get("/reports")
def get_report_entries(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Test ID": "LAB-401", "Patient": "Aarav Kumar", "Result Summary": "Hemoglobin 14.2 g/dL (Normal)", "Verified By": "Anil Mehta", "Status": "Verified"}
    ]
    return get_generic_records(db, "lab_report_entries", defaults)

@router.post("/report-entry")
def create_report_entry(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "lab_report_entries", payload)

@router.delete("/report-entry/{record_id}")
def delete_report_entry(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "lab_report_entries", record_id)


# 4. Report Upload
@router.get("/report-upload")
def get_report_uploads(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Document ID": "DOC-201", "Patient": "Siddharth Roy", "File Name": "Knee_MRI_Scan.pdf", "Upload Date": "2026-08-13", "Status": "Completed"}
    ]
    return get_generic_records(db, "lab_report_uploads", defaults)

@router.post("/report-upload")
def create_report_upload(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "lab_report_uploads", payload)

@router.delete("/report-upload/{record_id}")
def delete_report_upload(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "lab_report_uploads", record_id)
