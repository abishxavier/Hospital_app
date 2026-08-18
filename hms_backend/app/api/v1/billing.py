from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(prefix="/billing", tags=["billing"])


# 1. Consultation Charges
@router.get("/consultation-charges")
@router.get("/charges/consultation")
def get_consultation_charges(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Doctor": "Dr. Priya Nair", "Amount": "$50.00", "Date": "2026-08-13", "Status": "Paid"}
    ]
    return get_generic_records(db, "billing_consultation", defaults)

@router.post("/consultation-charges")
def create_consultation_charge(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "billing_consultation", payload)

@router.delete("/consultation-charges/{record_id}")
def delete_consultation_charge(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "billing_consultation", record_id)


# 2. Lab Charges
@router.get("/lab-charges")
def get_lab_charges(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Test Name": "CBC Blood Profile", "Amount": "$35.00", "Status": "Paid"}
    ]
    return get_generic_records(db, "billing_lab", defaults)

@router.post("/lab-charges")
def create_lab_charge(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "billing_lab", payload)

@router.delete("/lab-charges/{record_id}")
def delete_lab_charge(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "billing_lab", record_id)


# 3. Pharmacy Charges
@router.get("/pharmacy-charges")
def get_pharmacy_charges(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Aarav Kumar", "Bill ID": "PH-901", "Amount": "$24.50", "Date": "2026-08-13", "Status": "Paid"}
    ]
    return get_generic_records(db, "billing_pharmacy", defaults)

@router.post("/pharmacy-charges")
def create_pharmacy_charge(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "billing_pharmacy", payload)

@router.delete("/pharmacy-charges/{record_id}")
def delete_pharmacy_charge(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "billing_pharmacy", record_id)


# 4. Room Charges
@router.get("/room-charges")
def get_room_charges(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Patient": "Siddharth Roy", "Days Stayed": "2 Days", "Total Amount": "$400.00", "Status": "Pending"}
    ]
    return get_generic_records(db, "billing_room", defaults)

@router.post("/room-charges")
def create_room_charge(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "billing_room", payload)

@router.delete("/room-charges/{record_id}")
def delete_room_charge(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "billing_room", record_id)


# 5. Payment Gateway
@router.get("/payment-gateway")
@router.get("/payments")
def get_payment_gateway_logs(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Transaction ID": "TXN-9901", "Patient": "Aarav Kumar", "Amount": "$109.50", "Method": "Credit Card", "Status": "Completed"}
    ]
    return get_generic_records(db, "billing_gateway", defaults)

@router.post("/payment-gateway")
def create_payment_gateway_log(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "billing_gateway", payload)

@router.delete("/payment-gateway/{record_id}")
def delete_payment_gateway_log(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "billing_gateway", record_id)


# 6. Invoice Generation
@router.get("/invoices")
def get_invoices(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Invoice ID": "INV-2026-01", "Patient": "Aarav Kumar", "Total Amount": "$109.50", "Due Date": "2026-08-13", "Status": "Paid"}
    ]
    return get_generic_records(db, "billing_invoices", defaults)

@router.post("/invoices")
def create_invoice(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "billing_invoices", payload)

@router.delete("/invoices/{record_id}")
def delete_invoice(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "billing_invoices", record_id)
