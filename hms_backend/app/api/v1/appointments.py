from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.models.appointment import Appointment
from hms_backend.app.utils.audit import log_deleted_record

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.get("")
def list_appointments(doctor_name: str = None, db: Session = Depends(get_db)):
    from hms_backend.app.api.v1.doctor import INITIAL_APPOINTMENTS, filter_by_doctor
    from hms_backend.app.utils.generic_crud import get_generic_records
    records = get_generic_records(db, "doctor_appointments", INITIAL_APPOINTMENTS)
    
    # Normalize keys for display across both Receptionist and Doctor portals
    for r in records:
        if not r.get("Patient") and r.get("Patient Name"):
            r["Patient"] = r["Patient Name"]
        if not r.get("Patient Name") and r.get("Patient"):
            r["Patient Name"] = r["Patient"]
        if not r.get("Date & Time") and r.get("Time"):
            r["Date & Time"] = r["Time"]
        if not r.get("Time") and r.get("Date & Time"):
            r["Time"] = r["Date & Time"]
        if not r.get("Appointment ID"):
            r["Appointment ID"] = f"APT-{r.get('id', 100):03d}"

    return filter_by_doctor(records, doctor_name)


@router.post("")
def book_appointment(payload: dict, db: Session = Depends(get_db)):
    code = payload.get("Appointment ID")
    if not code:
        code = f"APT-{800 + db.query(Appointment).count() + 1}"
    
    # Ensure code is unique in Appointment table
    existing = db.query(Appointment).filter(Appointment.appointment_code == code).first()
    if existing:
        import time
        code = f"APT-{int(time.time() * 1000) % 100000}"

    patient = payload.get("Patient") or payload.get("Patient Name") or "Aarav Kumar"
    doctor = payload.get("Doctor") or "Dr. Madhavan"
    date_str = payload.get("Date & Time") or payload.get("Time") or "2026-08-20 10:30 AM"
    status = payload.get("Status") or "Scheduled"

    appt = Appointment(
        appointment_code=code,
        patient_id=1,
        doctor_id=1,
        status=status,
        notes=f"Booked for {patient} with {doctor} on {date_str}"
    )
    db.add(appt)
    try:
        db.commit()
        db.refresh(appt)
    except Exception:
        db.rollback()

    # Sync to doctor_appointments in DB so Doctor portal receives it instantly
    from hms_backend.app.utils.generic_crud import create_generic_record
    doc_appt_payload = {
        "Time": date_str,
        "Date & Time": date_str,
        "Patient Name": patient,
        "Patient": patient,
        "Doctor": doctor,
        "Status": status,
        "Appointment ID": code,
        "Notes": f"Booked via Receptionist for {doctor}"
    }
    rec = create_generic_record(db, "doctor_appointments", doc_appt_payload)

    # Notify doctor in doctor_notifications DB table
    notif_data = {
        "Doctor": doctor,
        "Patient": patient,
        "Message": f"🔔 New Appointment Booked: {patient} scheduled with {doctor} for {date_str}.",
        "Status": "Unread"
    }
    create_generic_record(db, "doctor_notifications", notif_data)

    return rec


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
