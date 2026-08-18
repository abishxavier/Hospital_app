from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.models.doctor import Doctor

router = APIRouter(prefix="/doctors", tags=["doctors"])


@router.get("")
def list_doctors(db: Session = Depends(get_db)):
    doctors = db.query(Doctor).all()
    result = []
    for d in doctors:
        dept_name = d.department.name if d.department else "General"
        result.append({
            "id": d.id,
            "Doctor Name": d.full_name,
            "Department": d.specialization or dept_name,
            "Phone": d.phone or "+91 98765 00000",
            "Availability": d.availability or "Available"
        })
    return result


@router.post("")
def create_doctor(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Doctor Name") or payload.get("full_name") or "Dr. New Doctor"
    dept = payload.get("Department") or payload.get("specialization") or "General Medicine"
    phone = payload.get("Phone") or payload.get("phone") or "+91 98765 00000"
    
    doc = Doctor(
        full_name=name,
        specialization=dept,
        phone=phone,
        availability="Available"
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return {
        "id": doc.id,
        "Doctor Name": doc.full_name,
        "Department": doc.specialization,
        "Phone": doc.phone,
        "Availability": doc.availability
    }


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    d = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not d:
        raise HTTPException(status_code=404, detail="Doctor not found")
    db.delete(d)
    db.commit()
    return {"status": "success", "message": f"Doctor #{doctor_id} deleted."}
