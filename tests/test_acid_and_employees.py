import pytest
from sqlalchemy.exc import IntegrityError
from hms_backend.app.core.database import SessionLocal, engine, Base
from hms_backend.app.models.user import User
from hms_backend.app.models.doctor import Doctor
from hms_backend.app.models.staff import Staff
from hms_backend.app.models.patient import Patient
from hms_backend.app.models.appointment import Appointment
from hms_backend.app.core.seeder import seed_database
from hms_backend.app.core.security import hash_password


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    seed_database(db)
    yield db
    db.close()


def test_unique_employee_id_constraint(setup_db):
    db = setup_db
    # Attempt duplicate employee_id insertion
    duplicate_user = User(
        employee_id="EMP-1001", # Existing Doctor Dr. Madhavan
        full_name="Duplicate Doctor",
        email="duplicate.doc@hospital.org",
        password_hash=hash_password("pass123"),
        role="doctor"
    )
    db.add(duplicate_user)
    with pytest.raises(IntegrityError):
        db.commit()
    db.rollback()


def test_unique_patient_id_constraint(setup_db):
    db = setup_db
    # Attempt duplicate patient_id insertion
    duplicate_patient = Patient(
        patient_id="PAT-2001", # Existing Patient Aarav
        patient_code="PAT-2001",
        full_name="Duplicate Patient",
        phone="+91 90000 00000",
        disease="Migraine",
        pain_scale=8
    )
    db.add(duplicate_patient)
    with pytest.raises(IntegrityError):
        db.commit()
    db.rollback()


def test_acid_atomicity_rollback(setup_db):
    db = setup_db
    # Atomicity: If transaction fails mid-way, all changes rollback
    count_before = db.query(User).count()
    try:
        user1 = User(employee_id="EMP-9999", full_name="Valid User", email="valid.u@hospital.org", password_hash="pass", role="staff")
        db.add(user1)
        db.flush()

        user2 = User(employee_id="EMP-1001", full_name="Invalid Duplicate ID User", email="invalid.u@hospital.org", password_hash="pass", role="staff")
        db.add(user2)
        db.commit()
    except Exception:
        db.rollback()

    count_after = db.query(User).count()
    assert count_before == count_after, "Atomicity failed: Partial commit occurred during rollback."


def test_acid_consistency_foreign_key(setup_db):
    db = setup_db
    # Consistency: Cannot create appointment for non-existent doctor
    invalid_appt = Appointment(
        appointment_code="APT-9999",
        patient_id=1,
        doctor_id=99999, # Non-existent Doctor ID
        status="Scheduled"
    )
    db.add(invalid_appt)
    with pytest.raises(IntegrityError):
        db.commit()
    db.rollback()


def test_seeded_personnel_counts(setup_db):
    db = setup_db
    # 4 Doctors
    doctors = db.query(Doctor).all()
    assert len(doctors) == 4, f"Expected 4 doctors, found {len(doctors)}"
    doc_ids = {d.employee_id for d in doctors}
    assert doc_ids == {"EMP-1001", "EMP-1002", "EMP-1003", "EMP-1004"}

    # 5 Nurses
    nurses = db.query(Staff).filter(Staff.role.like("%Nurse%")).all()
    assert len(nurses) == 5, f"Expected 5 nurses, found {len(nurses)}"
    nurse_ids = {n.employee_id for n in nurses}
    assert nurse_ids == {"EMP-1005", "EMP-1006", "EMP-1007", "EMP-1008", "EMP-1009"}

    # 2 Receptionists
    receptionists = db.query(Staff).filter(Staff.role.like("%Reception%")).all()
    assert len(receptionists) == 2, f"Expected 2 receptionists, found {len(receptionists)}"
    rec_ids = {r.employee_id for r in receptionists}
    assert rec_ids == {"EMP-1010", "EMP-1011"}

    # 8 Patients
    patients = db.query(Patient).all()
    assert len(patients) == 8, f"Expected 8 patients, found {len(patients)}"
    pat_ids = {p.patient_id for p in patients}
    assert pat_ids == {"PAT-2001", "PAT-2002", "PAT-2003", "PAT-2004", "PAT-2005", "PAT-2006", "PAT-2007", "PAT-2008"}


def test_patient_diseases_and_pain_levels(setup_db):
    db = setup_db
    p1 = db.query(Patient).filter(Patient.patient_id == "PAT-2001").first()
    assert p1.disease == "Diabetes"
    assert p1.pain_scale == 3

    p4 = db.query(Patient).filter(Patient.patient_id == "PAT-2004").first()
    assert p4.disease == "Pneumonia"
    assert p4.pain_scale == 7

    p7 = db.query(Patient).filter(Patient.patient_id == "PAT-2007").first()
    assert p7.disease == "Dengue"
    assert p7.pain_scale == 7
