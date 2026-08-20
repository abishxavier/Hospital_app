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
    doctors_list = [
        "Dr. Madhavan",
        "Dr. S. Karthikeyan",
        "Dr. Murugan Jeyaraman",
        "Dr. Raj Kanna",
        "Dr. Priya Nair"
    ]
    for idx, p in enumerate(patients):
        doc_assigned = doctors_list[idx % len(doctors_list)]
        result.append({
            "id": p.id,
            "Patient ID": p.patient_id or p.patient_code or f"PAT-{p.id:04d}",
            "Name": p.full_name,
            "Doctor": doc_assigned,
            "Disease": p.disease or "General Consultation",
            "Pain Level": f"{p.pain_scale or 3}/10",
            "Phone": p.phone,
            "Registered Date": str(p.created_at.date()) if p.created_at else "2026-08-20",
            "Status": p.status or "Active"
        })
    return result


@router.post("")
def register_patient(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Name") or payload.get("full_name") or "New Patient"
    phone = payload.get("Phone") or payload.get("phone") or "+91 99999 00000"
    email = payload.get("Email") or payload.get("email")
    pid = payload.get("Patient ID") or payload.get("patient_id") or payload.get("patient_code") or f"PAT-{2000 + db.query(Patient).count() + 1}"
    disease = payload.get("Disease") or payload.get("disease") or "General Consultation"
    doctor = payload.get("Doctor") or payload.get("doctor") or "Dr. Madhavan"
    
    pain_val = payload.get("Pain Level") or payload.get("Pain Scale") or payload.get("pain_scale") or payload.get("pain")
    pain = 3
    if pain_val is not None:
        import re
        m = re.search(r'\d+', str(pain_val))
        if m:
            pain = int(m.group(0))
            if pain > 10: pain = 10
            if pain < 0: pain = 0

    existing = db.query(Patient).filter((Patient.patient_id == pid) | (Patient.patient_code == pid)).first()
    if existing:
        pid = f"PAT-{2000 + db.query(Patient).count() + 100}"

    patient = Patient(
        patient_id=pid,
        patient_code=pid,
        full_name=name,
        phone=phone,
        email=email,
        disease=disease,
        pain_scale=pain,
        status="Active"
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)

    # Save appointment & notification in DB for selected doctor
    from hms_backend.app.utils.generic_crud import create_generic_record
    from datetime import datetime
    time_str = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
    create_generic_record(db, "doctor_appointments", {
        "Time": time_str,
        "Patient Name": name,
        "Doctor": doctor,
        "Status": "Scheduled",
        "Notes": f"Newly registered patient ({disease})"
    })
    
    create_generic_record(db, "doctor_notifications", {
        "Doctor": doctor,
        "Patient": name,
        "Message": f"🔔 New Patient Assigned: {name} registered by Receptionist and assigned to {doctor}.",
        "Status": "Unread"
    })

    return {
        "id": patient.id,
        "Patient ID": patient.patient_id,
        "Name": patient.full_name,
        "Doctor": doctor,
        "Disease": patient.disease,
        "Pain Level": f"{patient.pain_scale}/10",
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
