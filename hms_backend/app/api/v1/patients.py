from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.models.patient import Patient
from hms_backend.app.utils.audit import log_deleted_record

router = APIRouter(prefix="/patients", tags=["patients"])


@router.get("")
def list_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).filter(Patient.status != "Deleted").all()
    result = []
    for p in patients:
        result.append({
            "id": p.id,
            "Patient ID": p.patient_code or f"PAT-{p.id:04d}",
            "Name": p.full_name,
            "Phone": p.phone,
            "Registered Date": str(p.created_at.date()) if p.created_at else "2026-08-13",
            "Status": p.status or "Active"
        })
    return result


@router.post("")
def register_patient(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Name") or payload.get("full_name") or "New Patient"
    phone = payload.get("Phone") or payload.get("phone") or "+91 99999 00000"
    email = payload.get("Email") or payload.get("email")
    code = payload.get("Patient ID") or payload.get("patient_code") or f"PAT-{1000 + db.query(Patient).count() + 1}"
    
    existing = db.query(Patient).filter(Patient.patient_code == code).first()
    if existing:
        code = f"PAT-{1000 + db.query(Patient).count() + int(datetime.now().timestamp()) % 10000}"

    patient = Patient(
        patient_code=code,
        full_name=name,
        phone=phone,
        email=email,
        status="Active"
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return {
        "id": patient.id,
        "Patient ID": patient.patient_code,
        "Name": patient.full_name,
        "Phone": patient.phone,
        "Registered Date": str(patient.created_at.date()) if patient.created_at else "2026-08-13",
        "Status": patient.status
    }


@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    p = db.query(Patient).filter(Patient.id == patient_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    deleted_info = {
        "id": p.id,
        "patient_code": p.patient_code,
        "name": p.full_name,
        "phone": p.phone,
        "status": "Deleted"
    }
    log_deleted_record(db, "Patient", p.id, deleted_info)

    p.status = "Deleted"
    db.commit()
    return {"status": "success", "message": f"Patient #{patient_id} marked as deleted in DB and archived in deleted_records table."}
