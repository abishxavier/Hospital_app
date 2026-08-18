from sqlalchemy.orm import Session
from hms_backend.app.models.user import User
from hms_backend.app.models.department import Department
from hms_backend.app.models.doctor import Doctor
from hms_backend.app.models.staff import Staff
from hms_backend.app.models.patient import Patient
from hms_backend.app.models.appointment import Appointment
from hms_backend.app.models.opd import OPDVisit
from hms_backend.app.models.ipd import Ward, Bed, Admission
from hms_backend.app.models.prescription import Prescription
from hms_backend.app.models.lab import TestRequest, LabReport
from hms_backend.app.models.pharmacy import Medicine, StockTransaction
from hms_backend.app.models.billing import Invoice, Payment
from hms_backend.app.models.ambulance import Ambulance, EmergencyBooking
from hms_backend.app.core.security import hash_password


def seed_database(db: Session):
    """Populates initial database records if empty."""
    
    # 1. Departments
    if db.query(Department).count() == 0:
        depts = [
            Department(name="Cardiology", head_of_dept="Dr. Priya Nair", total_staff=18, status="Active"),
            Department(name="Neurology", head_of_dept="Dr. Robert Chen", total_staff=12, status="Active"),
            Department(name="Pediatrics", head_of_dept="Dr. Anita Desai", total_staff=15, status="Active"),
            Department(name="Orthopedics", head_of_dept="Dr. Vikram Malhotra", total_staff=14, status="Active"),
            Department(name="Emergency & ICU", head_of_dept="Dr. Sarah Johnson", total_staff=30, status="Active"),
        ]
        db.add_all(depts)
        db.commit()

    # 2. Users
    if db.query(User).count() == 0:
        users = [
            User(full_name="Dr. Sarah Johnson", email="admin@hospital.com", password_hash=hash_password("admin123"), role="admin"),
            User(full_name="Dr. Priya Nair", email="priya.n@hospital.org", password_hash=hash_password("doctor123"), role="doctor"),
            User(full_name="Rajesh Sharma", email="rajesh.s@hospital.org", password_hash=hash_password("reception123"), role="reception"),
            User(full_name="Sunita Rao", email="sunita.r@hospital.org", password_hash=hash_password("nurse123"), role="nurse"),
            User(full_name="Anil Mehta", email="anil.m@hospital.org", password_hash=hash_password("lab123"), role="laboratory"),
            User(full_name="Vikram Singh", email="vikram.s@hospital.org", password_hash=hash_password("pharmacy123"), role="pharmacy"),
        ]
        db.add_all(users)
        db.commit()

    # 3. Doctors
    if db.query(Doctor).count() == 0:
        cardio = db.query(Department).filter(Department.name == "Cardiology").first()
        neuro = db.query(Department).filter(Department.name == "Neurology").first()
        pedia = db.query(Department).filter(Department.name == "Pediatrics").first()

        doctors = [
            Doctor(full_name="Dr. Priya Nair", specialization="Cardiology", phone="+91 98765 12345", availability="Available", department_id=cardio.id if cardio else None),
            Doctor(full_name="Dr. Robert Chen", specialization="Neurology", phone="+91 98765 67890", availability="On Leave", department_id=neuro.id if neuro else None),
            Doctor(full_name="Dr. Anita Desai", specialization="Pediatrics", phone="+91 98765 23456", availability="Available", department_id=pedia.id if pedia else None),
        ]
        db.add_all(doctors)
        db.commit()

    # 4. Staff
    if db.query(Staff).count() == 0:
        staff_list = [
            Staff(full_name="Sunita Rao", role="Head Nurse", shift="Morning Shift", phone="+91 91111 22222", status="Active"),
            Staff(full_name="Anil Mehta", role="Senior Lab Tech", shift="Day Shift", phone="+91 93333 44444", status="Active"),
            Staff(full_name="Pooja Verma", role="Reception Officer", shift="Morning Shift", phone="+91 95555 66666", status="Active"),
        ]
        db.add_all(staff_list)
        db.commit()

    # 5. Patients
    if db.query(Patient).count() == 0:
        patients = [
            Patient(patient_code="PAT-1001", full_name="Aarav Kumar", phone="+91 98765 43210", email="aarav.kumar@email.com", gender="Male", blood_group="O+", status="Active"),
            Patient(patient_code="PAT-1002", full_name="Meera Shah", phone="+91 91234 56780", email="meera.shah@email.com", gender="Female", blood_group="A+", status="Active"),
            Patient(patient_code="PAT-1003", full_name="Kavita Patel", phone="+91 98111 22233", email="kavita.patel@email.com", gender="Female", blood_group="B+", status="Active"),
            Patient(patient_code="PAT-1004", full_name="Siddharth Roy", phone="+91 97444 55566", email="siddharth.roy@email.com", gender="Male", blood_group="AB+", status="Active"),
        ]
        db.add_all(patients)
        db.commit()

    # 6. Appointments
    if db.query(Appointment).count() == 0:
        p1 = db.query(Patient).first()
        d1 = db.query(Doctor).first()
        if p1 and d1:
            appts = [
                Appointment(appointment_code="APT-801", patient_id=p1.id, doctor_id=d1.id, status="Checked In", appointment_type="Follow-up", queue_number=1),
                Appointment(appointment_code="APT-802", patient_id=p1.id, doctor_id=d1.id, status="Scheduled", appointment_type="Routine Consultation", queue_number=2),
            ]
            db.add_all(appts)
            db.commit()

    # 7. OPD Visits
    if db.query(OPDVisit).count() == 0:
        p1 = db.query(Patient).first()
        if p1:
            visits = [
                OPDVisit(token_no="TK-01", patient_id=p1.id, estimated_time="10:30 AM", status="In Consultation"),
                OPDVisit(token_no="TK-02", patient_id=p1.id, estimated_time="10:45 AM", status="Waiting"),
            ]
            db.add_all(visits)
            db.commit()

    # 8. IPD (Wards, Beds, Admissions)
    if db.query(Ward).count() == 0:
        ward1 = Ward(name="ICU Block A", ward_type="Intensive Care Unit", total_beds=10, occupied_beds=2, nurse_in_charge="Sunita Rao")
        ward2 = Ward(name="Deluxe Private Wing", ward_type="Deluxe Private", total_beds=8, occupied_beds=1, nurse_in_charge="Sunita Rao")
        db.add_all([ward1, ward2])
        db.commit()

        b1 = Bed(bed_number="Bed ICU-01", ward_id=ward1.id, status="Occupied")
        b2 = Bed(bed_number="Bed ICU-02", ward_id=ward1.id, status="Available")
        b3 = Bed(bed_number="Room 101", ward_id=ward2.id, status="Occupied")
        db.add_all([b1, b2, b3])
        db.commit()

        p1 = db.query(Patient).filter(Patient.full_name == "Siddharth Roy").first()
        if p1:
            adm = Admission(admission_code="IPD-301", patient_id=p1.id, bed_id=b3.id, attending_doctor="Dr. Vikram Malhotra", status="Admitted")
            db.add(adm)
            db.commit()

    # 9. Prescriptions
    if db.query(Prescription).count() == 0:
        rx = [
            Prescription(patient_name="Aarav Kumar", doctor_name="Dr. Priya Nair", medicines="Amoxicillin 500mg, Paracetamol 650mg", duration="5 Days", status="Prescribed"),
            Prescription(patient_name="Meera Shah", doctor_name="Dr. Robert Chen", medicines="Naproxen 250mg, Pantoprazole 40mg", duration="7 Days", status="Prescribed"),
        ]
        db.add_all(rx)
        db.commit()

    # 10. Laboratory
    if db.query(TestRequest).count() == 0:
        lab_reqs = [
            TestRequest(req_code="LAB-401", patient_name="Aarav Kumar", test_type="CBC Blood Profile", priority="Normal", requested_by="Dr. Priya Nair", status="Requested"),
            TestRequest(req_code="LAB-402", patient_name="Siddharth Roy", test_type="Knee MRI Scan", priority="Urgent", requested_by="Dr. Vikram Malhotra", status="In Progress"),
        ]
        db.add_all(lab_reqs)
        db.commit()

        lab_rep = LabReport(test_id=1, patient_name="Aarav Kumar", result_summary="Hemoglobin 14.2 g/dL (Normal)", verified_by="Anil Mehta", status="Verified")
        db.add(lab_rep)
        db.commit()

    # 11. Pharmacy
    if db.query(Medicine).count() == 0:
        meds = [
            Medicine(name="Paracetamol 650mg", batch_no="BAT-2024-X", stock_qty=1200, unit_price=1.5, status="Available"),
            Medicine(name="Amoxicillin 500mg", batch_no="BAT-2025-A", stock_qty=450, unit_price=4.0, status="Available"),
            Medicine(name="Pantoprazole 40mg", batch_no="BAT-2024-P", stock_qty=80, unit_price=3.0, status="Low Stock"),
        ]
        db.add_all(meds)
        db.commit()

    # 12. Billing
    if db.query(Invoice).count() == 0:
        invoices = [
            Invoice(invoice_code="INV-2026-01", patient_name="Aarav Kumar", total_amount=109.50, due_date="2026-08-12", status="Paid"),
            Invoice(invoice_code="INV-2026-02", patient_name="Siddharth Roy", total_amount=720.00, due_date="2026-08-16", status="Pending"),
        ]
        db.add_all(invoices)
        db.commit()

        pmts = [
            Payment(transaction_code="TXN-9901", patient_name="Aarav Kumar", amount=109.50, method="Credit Card", status="Completed"),
        ]
        db.add_all(pmts)
        db.commit()

    # 13. Ambulance
    if db.query(Ambulance).count() == 0:
        ambs = [
            Ambulance(vehicle_number="AMB-101", driver_name="Ramesh Kumar", driver_phone="+91 98989 11223", status="Available"),
            Ambulance(vehicle_number="AMB-102", driver_name="Suresh Patel", driver_phone="+91 98989 44556", status="On Call"),
        ]
        db.add_all(ambs)
        db.commit()

        bk = EmergencyBooking(patient_name="Emergency Call #901", pickup_location="MG Road Crossing", ambulance_vehicle="AMB-102", status="Dispatched")
        db.add(bk)
        db.commit()
