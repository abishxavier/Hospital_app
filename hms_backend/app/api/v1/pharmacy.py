from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.models.pharmacy import Medicine
from hms_backend.app.utils.audit import log_deleted_record
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(prefix="/pharmacy", tags=["pharmacy"])


# 1. Medicine Inventory
@router.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    meds = db.query(Medicine).filter(Medicine.status != "Deleted").all()
    res = []
    for m in meds:
        res.append({
            "id": m.id,
            "Medicine Name": m.name,
            "Batch No": m.batch_no,
            "Expiry Date": str(m.expiry_date) if m.expiry_date else "2027-11-30",
            "Stock Qty": f"{m.stock_qty} Units",
            "Status": m.status or "Available"
        })
    return res


@router.post("/inventory")
def create_medicine(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Medicine Name") or payload.get("name") or "New Medicine"
    batch = payload.get("Batch No") or f"BAT-2026-{db.query(Medicine).count()+1}"
    
    med = Medicine(name=name, batch_no=batch, stock_qty=500, unit_price=2.5, status="Available")
    db.add(med)
    db.commit()
    db.refresh(med)
    return {
        "id": med.id,
        "Medicine Name": med.name,
        "Batch No": med.batch_no,
        "Expiry Date": "2027-11-30",
        "Stock Qty": f"{med.stock_qty} Units",
        "Status": med.status
    }


@router.delete("/inventory/{med_id}")
def delete_medicine(med_id: int, db: Session = Depends(get_db)):
    m = db.query(Medicine).filter(Medicine.id == med_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Medicine not found")
    
    deleted_info = {
        "id": m.id,
        "name": m.name,
        "batch_no": m.batch_no,
        "status": "Deleted"
    }
    log_deleted_record(db, "Medicine", m.id, deleted_info)
    m.status = "Deleted"
    db.commit()
    return {"status": "success", "message": f"Medicine #{med_id} marked as deleted in DB and logged in deleted_records table."}


# 2. Prescription Processing
@router.get("/prescription-processing")
@router.get("/prescriptions")
def get_prescription_processing(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Prescription ID": "RX-501", "Patient": "Aarav Kumar", "Doctor": "Dr. Priya Nair", "Status": "Ready for Dispense"}
    ]
    return get_generic_records(db, "pharmacy_rx_processing", defaults)

@router.post("/prescription-processing")
def create_prescription_processing(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "pharmacy_rx_processing", payload)

@router.delete("/prescription-processing/{record_id}")
def delete_prescription_processing(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "pharmacy_rx_processing", record_id)


# 3. Medicine Billing
@router.get("/medicine-billing")
@router.get("/bills")
def get_medicine_billing(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Bill ID": "PH-901", "Patient": "Aarav Kumar", "Total Amount": "$24.50", "Payment Status": "Paid"}
    ]
    return get_generic_records(db, "pharmacy_billing", defaults)

@router.post("/medicine-billing")
def create_medicine_billing(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "pharmacy_billing", payload)

@router.delete("/medicine-billing/{record_id}")
def delete_medicine_billing(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "pharmacy_billing", record_id)


# 4. Stock Alerts
@router.get("/stock-alerts")
@router.get("/alerts")
def get_stock_alerts(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Medicine Name": "Pantoprazole 40mg", "Alert Type": "Low Stock", "Current Stock": "80 Tabs", "Action Required": "Re-order 500 Tabs"}
    ]
    return get_generic_records(db, "pharmacy_alerts", defaults)

@router.post("/stock-alerts")
def create_stock_alert(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "pharmacy_alerts", payload)

@router.delete("/stock-alerts/{record_id}")
def delete_stock_alert(record_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "pharmacy_alerts", record_id)
