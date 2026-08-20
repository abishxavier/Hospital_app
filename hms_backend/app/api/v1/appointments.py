from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.models.appointment import Appointment
from hms_backend.app.utils.audit import log_deleted_record

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.get("")
def list_appointments(doctor_name: str = None, db: Session = Depends(get_db)):
    appts = db.query(Appointment).filter(Appointment.status != "Deleted").all()
    result = []
    for a in appts:
        patient_name = a.patient.full_name if a.patient else f"Patient #{a.patient_id}"
        doctor_name_val = a.doctor.full_name if a.doctor else f"Doctor #{a.doctor_id}"
        result.append({
            "id": a.id,
            "Appointment ID": a.appointment_code or f"APT-{a.id:03d}",
            "Patient": patient_name,
            "Doctor": doctor_name_val,
            "Date & Time": str(a.appointment_date.strftime("%Y-%m-%d %H:%M")) if a.appointment_date else "2026-08-13 10:00",
            "Status": a.status or "Scheduled"
        })
    if doctor_name:
        doc_lower = doctor_name.strip().lower()
        result = [r for r in result if doc_lower in (r.get("Doctor") or "").lower()]
    return result


@router.post("")
def book_appointment(payload: dict, db: Session = Depends(get_db)):
    code = payload.get("Appointment ID") or f"APT-{800 + db.query(Appointment).count() + 1}"
    patient = payload.get("Patient") or "Aarav Kumar"
    doctor = payload.get("Doctor") or "Dr. Priya Nair"
    date_str = payload.get("Date & Time") or "2026-08-13 10:30 AM"
    status = payload.get("Status") or "Scheduled"

    appt = Appointment(
        appointment_code=code,
        patient_id=1,
        doctor_id=1,
        status=status,
        notes=f"Booked for {patient} with {doctor} on {date_str}"
    )
    db.add(appt)
    db.commit()
    db.refresh(appt)

    return {
        "id": appt.id,
        "Appointment ID": appt.appointment_code,
        "Patient": patient,
        "Doctor": doctor,
        "Date & Time": date_str,
        "Status": appt.status
    }


@router.delete("/{appt_id}")
def delete_appointment(appt_id: int, db: Session = Depends(get_db)):
    a = db.query(Appointment).filter(Appointment.id == appt_id).first()
    if not a:
        raise HTTPException(status_code=404, detail="Appointment not found")

    deleted_info = {
        "id": a.id,
        "appointment_code": a.appointment_code,
        "status": "Deleted",
        "notes": a.notes
    }
    log_deleted_record(db, "Appointment", a.id, deleted_info)

    a.status = "Deleted"
    db.commit()
    return {"status": "success", "message": f"Appointment #{appt_id} marked as deleted in DB and saved in deleted_records table."}
