## 🏥 Hospital Management System (HMS) — Overview
This project is a full-stack, enterprise-grade Hospital Management System (HMS) built with a modern React (Vite + TailwindCSS) frontend and a high-performance FastAPI (Python + SQLAlchemy ORM) backend.

### 🏗️ Architecture & Technology Stack
Frontend: Built with React (Vite), TailwindCSS, Lucide Icons, and React Router DOM. Features interactive data tables, custom date/time pickers, dynamic pagination, and responsive mobile drawers.
Backend: Powered by FastAPI, SQLite (via SQLAlchemy 2.0 ORM), and Pydantic v2 validation schemas. Includes JWT bearer security, bcrypt password hashing, and generic audit log tracking.
Repository: Hosted on GitHub at https://github.com/abishxavier/Hospital_app.git.
 🔑 5 Role Personas & Security Access (RBAC)
### Access control is enforced both on the client side (route guards & sidebar filtering) and on the backend API layer:

Role Persona	Quick Demo Username	Demo Password	Scope & Module Permissions	Default Landing Page
#### 🛡️ Admin	admin@hospital.com	admin	All 9 Modules: System-wide control, users, doctors, departments, audit logs & settings	/admin/dashboard
#### 🩺 Doctor	doctor@hospital.com	doctor	Doctor Module Only: Appointments, Patient EMR History, ICD Diagnosis, Prescriptions, Lab Test Requests	/doctor/appointments
#### 🩺 Nurse	nurse@hospital.com	nurse	Nurse Module Only: Patient Vitals (BP, HR, Temp, Pain Scale 0-10, RBS, SpO2), Ward Management, Medication Admin	/nurse/patient-vitals
#### 📋 Hospital Receptionist	reception@hospital.com	reception	Reception & Billing: Patient Check-In, Appointment Booking, Queue Token Tracking, Consultation Charges & Invoices	/reception/patient-registration
#### 🧪 Laboratory	lab@hospital.com	lab	Laboratory Module Only: Test Requests, Barcoded Sample Collection, Report Entry & PDF Upload	/laboratory/test-request
## 🚀 Key Modules & Capabilities
Admin Module (

Dashboard.jsx
)
Live metrics (Patients, Doctors, Revenue, Occupancy), User & Staff Management, Department Wings, System Settings, and Deleted Records Audit Log.
Reception Module
Outpatient Check-In & Demographic Registration, Appointment Booking, Real-time Queue Token tracking (TK-01), and OP/IP status switching.
Doctor Module
Today's Clinical Schedule, Patient History (EMR), ICD Diagnoses, Digital Prescription Writer (with medicine drop-down selector), Lab Test Requests, and Follow-up Scheduler.
Nurse Module
Bedside Vitals (BP, Heart Rate, Temperature, Pain Scale 0-10, RBS, SpO2), Ward Bed Occupancy Tracking, Bedside Dose Administration, and Daily Nursing Observation Notes.
Laboratory Module
Incoming Doctor Test Requests, Barcoded Sample Collection, Diagnostic Finding Entry, and PDF Scanned Report Upload.
Pharmacy Module
Medicine Inventory (Batch & Expiry tracking), Prescription Dispensing, Medicine Billing, and Low Stock Alerts.
Inpatient (IP) Module
Deluxe/Private Room Allocation, IP Admissions, Post-op Treatment Records, Daily Progress Notes, and Discharge Summaries.
Billing Module
Itemized Consultation Charges, Lab & Pharmacy Charges, Room Charges, Payment Gateway log (TXN-9901), and Consolidated Invoice Generation.
Patient Portal
Portal Account Access, Online Appointment Booking, Prescription View, PDF Lab Report Downloads, and Medical History EMR logs.
🧪 Automated Testing & Reliability
The codebase features a 23-test automated test suite in 

tests/
 covering 8 dimensions:

Unit Tests (

test_unit.py
): Password hashing, JWT encoding, invoice calculation, low stock alerts, bed allocation.
Integration Tests (

test_integration.py
): FastAPI TestClient CRUD operations for Patients, Doctors, and Health check.
End-to-End Tests (

test_e2e.py
): Validates 27 API endpoints across all 9 modules.
Functional Workflow (

test_functional.py
): Full patient clinical lifecycle (Registration ➔ Appointment ➔ Diagnosis ➔ Prescription ➔ Billing).
Security Tests (

test_security.py
): Login validation, invalid token rejection, bcrypt strength, CORS header validation.
Performance Tests (

test_performance.py
): Latency benchmarking & batch throughput.
Database Audit & Deletion (

test_database_persistence_and_deletion.py
): Soft deletion logging & persistence in deleted_records.
💻 How to Run locally
bash
# 1. Start FastAPI Backend (Port 8000)
.\.venv\Scripts\python.exe -m uvicorn hms_backend.app.main:app --host 127.0.0.1 --port 8000
# 2. Start React Frontend (Port 5173)
npm.cmd --prefix hms-frontend run dev
Frontend App: http://localhost:5173/
Backend Swagger Docs: http://127.0.0.1:8000/docs
