from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from hms_backend.app.core.database import get_db
from hms_backend.app.models.user import User
from hms_backend.app.models.department import Department
from hms_backend.app.models.staff import Staff
from hms_backend.app.models.doctor import Doctor
from hms_backend.app.models.audit import DeletedRecord
from hms_backend.app.core.security import hash_password
from hms_backend.app.utils.audit import log_deleted_record
from hms_backend.app.utils.generic_crud import (
    get_generic_records, create_generic_record, delete_generic_record
)

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/dashboard")
def get_dashboard_overview(db: Session = Depends(get_db)):
    return {
        "patients": 1248,
        "occupancy": 84,
        "appointments": 342,
        "revenue": 45210,
        "patient_flow": [
            {"name": "Mon", "patients": 120, "opd": 80, "ipd": 40},
            {"name": "Tue", "patients": 145, "opd": 95, "ipd": 50},
            {"name": "Wed", "patients": 130, "opd": 85, "ipd": 45},
            {"name": "Thu", "patients": 165, "opd": 110, "ipd": 55},
            {"name": "Fri", "patients": 180, "opd": 120, "ipd": 60},
            {"name": "Sat", "patients": 90, "opd": 60, "ipd": 30},
            {"name": "Sun", "patients": 70, "opd": 45, "ipd": 25},
        ],
        "recent_activity": [
            {"title": "New patient registered", "subtitle": "John Doe • Cardiology", "time": "10 mins ago"},
            {"title": "Surgery completed", "subtitle": "Dr. Smith • OT Room 2", "time": "45 mins ago"},
            {"title": "Shift Change", "subtitle": "Nursing Staff • ICU Ward", "time": "2 hours ago"}
        ]
    }


# 1. Users
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.is_active == True).all()
    res = []
    for u in users:
        res.append({
            "id": u.id,
            "Name": u.full_name,
            "Role": u.role,
            "Email": u.email,
            "Status": "Active"
        })
    return res


@router.post("/users")
def create_user(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Name") or payload.get("full_name") or "New User"
    email = payload.get("Email") or payload.get("email") or f"user{db.query(User).count()+1}@hospital.com"
    role = payload.get("Role") or payload.get("role") or "staff"
    
    user = User(
        full_name=name,
        email=email,
        password_hash=hash_password("user123"),
        role=role,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "id": user.id,
        "Name": user.full_name,
        "Role": user.role,
        "Email": user.email,
        "Status": "Active"
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    u = db.query(User).filter(User.id == user_id).first()
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    
    log_deleted_record(db, "User", u.id, {"id": u.id, "name": u.full_name, "email": u.email, "role": u.role})
    u.is_active = False
    db.commit()
    return {"status": "success", "message": f"User #{user_id} soft-deleted and archived in deleted_records."}


# 2. Departments
@router.get("/departments")
def get_departments(db: Session = Depends(get_db)):
    depts = db.query(Department).filter(Department.status != "Deleted").all()
    res = []
    for d in depts:
        res.append({
            "id": d.id,
            "Dept Name": d.name,
            "Head of Dept": d.head_of_dept or "Dr. Unassigned",
            "Total Staff": f"{d.total_staff or 10} Staff",
            "Status": d.status or "Active"
        })
    return res


@router.post("/departments")
def create_department(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Dept Name") or payload.get("name") or "New Department"
    hod = payload.get("Head of Dept") or payload.get("head_of_dept") or "Dr. Unassigned"
    
    dept = Department(name=name, head_of_dept=hod, total_staff=10, status="Active")
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return {
        "id": dept.id,
        "Dept Name": dept.name,
        "Head of Dept": dept.head_of_dept,
        "Total Staff": "10 Staff",
        "Status": dept.status
    }


@router.delete("/departments/{dept_id}")
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    d = db.query(Department).filter(Department.id == dept_id).first()
    if not d:
        raise HTTPException(status_code=404, detail="Department not found")
    
    log_deleted_record(db, "Department", d.id, {"id": d.id, "name": d.name, "head_of_dept": d.head_of_dept})
    d.status = "Deleted"
    db.commit()
    return {"status": "success", "message": f"Department #{dept_id} deleted."}


# 3. Doctors
@router.get("/doctors")
def get_admin_doctors(db: Session = Depends(get_db)):
    doctors = db.query(Doctor).filter(Doctor.availability != "Deleted").all()
    res = []
    for doc in doctors:
        res.append({
            "id": doc.id,
            "Doctor Name": doc.full_name,
            "Department": doc.specialization,
            "Phone": doc.phone or "+91 98765 00000",
            "Availability": doc.availability or "Available"
        })
    return res


@router.post("/doctors")
def create_doctor(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Doctor Name") or payload.get("full_name") or "Dr. New Doctor"
    dept = payload.get("Department") or "Cardiology"
    phone = payload.get("Phone") or "+91 98765 00000"
    
    doc = Doctor(full_name=name, specialization=dept, phone=phone, availability="Available")
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


@router.delete("/doctors/{doc_id}")
def delete_doctor(doc_id: int, db: Session = Depends(get_db)):
    d = db.query(Doctor).filter(Doctor.id == doc_id).first()
    if not d:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    log_deleted_record(db, "Doctor", d.id, {"id": d.id, "name": d.full_name, "department": d.specialization})
    d.availability = "Deleted"
    db.commit()
    return {"status": "success", "message": f"Doctor #{doc_id} deleted."}


# 4. Staff
@router.get("/staff")
def get_staff(db: Session = Depends(get_db)):
    staff_list = db.query(Staff).filter(Staff.status != "Deleted").all()
    res = []
    for s in staff_list:
        res.append({
            "id": s.id,
            "Staff Name": s.full_name,
            "Role": s.role,
            "Department": s.department.name if s.department else "General",
            "Shift": s.shift or "Morning Shift"
        })
    return res


@router.post("/staff")
def create_staff(payload: dict, db: Session = Depends(get_db)):
    name = payload.get("Staff Name") or payload.get("full_name") or "New Staff"
    role = payload.get("Role") or payload.get("role") or "Nurse"
    shift = payload.get("Shift") or payload.get("shift") or "Morning Shift"
    
    st = Staff(full_name=name, role=role, shift=shift, status="Active")
    db.add(st)
    db.commit()
    db.refresh(st)
    return {
        "id": st.id,
        "Staff Name": st.full_name,
        "Role": st.role,
        "Department": "General",
        "Shift": st.shift
    }


@router.delete("/staff/{staff_id}")
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    st = db.query(Staff).filter(Staff.id == staff_id).first()
    if not st:
        raise HTTPException(status_code=404, detail="Staff not found")
    
    log_deleted_record(db, "Staff", st.id, {"id": st.id, "name": st.full_name, "role": st.role})
    st.status = "Deleted"
    db.commit()
    return {"status": "success", "message": f"Staff #{staff_id} deleted."}


# 5. Reports & Analytics
@router.get("/reports")
def get_reports(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Report Name": "Monthly Patient Flow Analysis", "Generated By": "Admin Bot", "Date": "2026-08-13", "Type": "Operational"}
    ]
    return get_generic_records(db, "admin_reports", defaults)


@router.post("/reports")
def create_report(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "admin_reports", payload)


@router.delete("/reports/{report_id}")
def delete_report(report_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "admin_reports", report_id)


# 6. System Settings
@router.get("/settings")
def get_settings(db: Session = Depends(get_db)):
    defaults = [
        {"id": 1, "Setting Key": "Hospital Name", "Value": "City Care General Hospital", "Last Updated": "2026-08-13", "Status": "Active"},
        {"id": 2, "Setting Key": "Emergency Contact Number", "Value": "+91 1800-200-9999", "Last Updated": "2026-08-13", "Status": "Active"}
    ]
    return get_generic_records(db, "admin_settings", defaults)


@router.post("/settings")
def create_setting(payload: dict, db: Session = Depends(get_db)):
    return create_generic_record(db, "admin_settings", payload)


@router.delete("/settings/{setting_id}")
def delete_setting(setting_id: int, db: Session = Depends(get_db)):
    return delete_generic_record(db, "admin_settings", setting_id)


# 7. Deleted Records Audit Log
@router.get("/deleted-records")
def get_deleted_records(db: Session = Depends(get_db)):
    deleted_list = db.query(DeletedRecord).order_by(DeletedRecord.deleted_at.desc()).all()
    res = []
    for d in deleted_list:
        res.append({
            "id": d.id,
            "Category": d.entity_type,
            "Record ID": f"REC-{d.entity_id or d.id}",
            "Deleted Data Snapshot": d.deleted_data,
            "Deleted Timestamp": str(d.deleted_at.strftime("%Y-%m-%d %H:%M")) if d.deleted_at else "2026-08-13",
            "Status": "Archived in DB"
        })
    return res
