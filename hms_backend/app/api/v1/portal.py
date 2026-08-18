from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(prefix="/portal", tags=["portal"])


# 1. Portal Login Settings
@router.get("/login-settings")
def get_login_settings(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient User": "aarav.kumar@email.com", "Last Login": "Today 09:15 AM", "Account Status": "Active"}
    ]
    return get_generic_records(db, "portal_login", defaults)

@router.post("/login-settings")
def create_login_setting(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "portal_login", payload)

@router.delete("/login-settings/{record_id}")
def delete_login_setting(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "portal_login", record_id)


# 2. Book Appointment
@router.get("/book-appointment")
def get_portal_appointments(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Meera Shah", "Doctor": "Dr. Robert Chen", "Requested Date": "2026-08-14", "Status": "Confirmed"}
    ]
    return get_generic_records(db, "portal_book_appt", defaults)

@router.post("/book-appointment")
def create_portal_appointment(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "portal_book_appt", payload)

@router.delete("/book-appointment/{record_id}")
def delete_portal_appointment(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "portal_book_appt", record_id)


# 3. View Prescriptions
@router.get("/view-prescriptions")
def get_portal_prescriptions(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Doctor": "Dr. Priya Nair", "Prescription Date": "2026-08-13", "Medicines": "Paracetamol 650mg", "Status": "Active"}
    ]
    return get_generic_records(db, "portal_prescriptions", defaults)

@router.post("/view-prescriptions")
def create_portal_prescription(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "portal_prescriptions", payload)

@router.delete("/view-prescriptions/{record_id}")
def delete_portal_prescription(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "portal_prescriptions", record_id)


# 4. Download Lab Reports
@router.get("/download-reports")
def get_portal_reports(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Report Name": "CBC_Blood_Report", "Download Date": "2026-08-13", "Status": "Downloaded"}
    ]
    return get_generic_records(db, "portal_reports", defaults)

@router.post("/download-reports")
def create_portal_report(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "portal_reports", payload)

@router.delete("/download-reports/{record_id}")
def delete_portal_report(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "portal_reports", record_id)


# 5. Online Payment
@router.get("/online-payment")
def get_portal_payments(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Amount": "$109.50", "Date": "2026-08-13", "Reference ID": "PAY-88219", "Status": "Successful"}
    ]
    return get_generic_records(db, "portal_payments", defaults)

@router.post("/online-payment")
def create_portal_payment(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "portal_payments", payload)

@router.delete("/online-payment/{record_id}")
def delete_portal_payment(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "portal_payments", record_id)


# 6. Medical History
@router.get("/medical-history")
def get_portal_medical_history(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Accessed Data": "Immunization & EMR Logs", "Date": "2026-08-13", "Status": "Verified"}
    ]
    return get_generic_records(db, "portal_med_history", defaults)

@router.post("/medical-history")
def create_portal_medical_history(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "portal_med_history", payload)

@router.delete("/medical-history/{record_id}")
def delete_portal_medical_history(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "portal_med_history", record_id)
