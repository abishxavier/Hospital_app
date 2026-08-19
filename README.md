# 🏥 HMS — Enterprise Hospital Management System

A full-stack, enterprise-grade **Hospital Management System (HMS)** built with a modern **React (Vite + TailwindCSS)** frontend and a high-performance **FastAPI (Python + SQLAlchemy ORM)** backend.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.3-61DAFB?style=flat&logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-5.4-646CFF?style=flat&logo=vite)](https://vitejs.dev/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.4-38B2AC?style=flat&logo=tailwindcss)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python)](https://python.org)
[![Pytest](https://img.shields.io/badge/Pytest-23%20Passed-brightgreen?style=flat&logo=pytest)](https://docs.pytest.org/)

---

## 🌟 Key Features

- **Split-Screen HMS Login Portal**: High-aesthetic HIMS/HMS login UI with a doctor backdrop, HIMS logo branding, and dynamic **Role Select Dropdown**.
- **Role-Based Access Control (RBAC)**: Client & server-enforced role restrictions across 5 key healthcare personas (**Admin**, **Doctor**, **Nurse**, **Receptionist**, **Laboratory**).
- **Comprehensive Clinical & Bedside Vitals**: Track blood pressure, heart rate, temperature, **Pain Scale (0–10)**, **RBS (Random Blood Sugar)**, and **SpO2 (Oxygen Saturation)**.
- **9 Operational Modules**: Full hospital workflow coverage from front desk registration to IP bed management and consolidated billing.
- **Audit Logging & Soft Deletion**: Generic audit records table tracking all deleted data snapshots.
- **8-Dimensional Automated Testing**: 23/23 unit, integration, E2E, security, performance, and regression tests.

---

## 🔑 Role Personas & Demo Credentials

Access the application at **[http://localhost:5173/login](http://localhost:5173/login)**. Use either the credentials below or click the 1-click **Quick Demo Login** buttons:

| Persona Role | Demo Username / Email | Demo Password | Module Access Scope | Default Landing Page |
| :--- | :--- | :--- | :--- | :--- |
| 🛡️ **Admin** | `admin@hospital.com` | `admin` | **All 9 Modules**: System-wide control, users, doctors, departments, audit logs & settings | `/admin/dashboard` |
| 🩺 **Doctor** | `doctor@hospital.com` | `doctor` | **Doctor Module Only**: Appointments, Patient EMR History, ICD Diagnosis, Prescriptions, Lab Test Requests | `/doctor/appointments` |
| 🩺 **Nurse** | `nurse@hospital.com` | `nurse` | **Nurse Module Only**: Patient Vitals (BP, HR, Temp, Pain Scale, RBS, SpO2), Ward Bed Occupancy, Med Admin | `/nurse/patient-vitals` |
| 📋 **Hospital Receptionist** | `reception@hospital.com` | `reception` | **Reception & Billing**: Patient Check-In, Appointment Booking, Queue Token Tracking, Consultation Charges & Invoices | `/reception/patient-registration` |
| 🧪 **Laboratory** | `lab@hospital.com` | `lab` | **Laboratory Module Only**: Test Requests, Barcoded Sample Collection, Report Entry & PDF Upload | `/laboratory/test-request` |

---

## 🏥 Hospital System Modules (9 Modules)

1. **Admin Module**
   - Live KPI dashboard (Patients, Doctors, Revenue, Bed Occupancy), User & Staff Management, Department Wings, Master System Settings, and Deleted Records Audit Log.
2. **Reception Module**
   - Outpatient Check-In & Demographic Registration, Appointment Scheduling (Book, Reschedule, Cancel), Real-Time Queue Token tracking (`TK-01`), and OP/IP status switching.
3. **Doctor Module**
   - Daily Appointment Schedule, EMR History, ICD-10 Diagnoses, Digital Prescription Writer (with medicine drop-down selector), Lab Test Requests, and Follow-up Scheduler.
4. **Nurse Module**
   - Bedside Vitals (**BP**, **Heart Rate**, **Temp**, **Pain Scale 0–10**, **RBS**, **SpO2**), Ward Bed Occupancy & In-charge tracking, Bedside Medication Admin, and Daily Nursing Notes.
5. **Laboratory Module**
   - Incoming Doctor Test Requests, Barcoded Sample Collection, Diagnostic Result Entry, and PDF Diagnostic Report Upload.
6. **Pharmacy Module**
   - Medicine Inventory (Batch & Expiry tracking), Prescription Dispensing, Medicine Billing, and Low Stock Alerts.
7. **Inpatient (IP) Module**
   - Deluxe/Private Room Allocation, IP Admissions, Post-Op Treatment Records, Daily Clinical Progress Notes, and Discharge Summaries.
8. **Billing Module**
   - Consultation Charges, Lab Charges, Pharmacy Charges, Room Charges, Online Payment Gateway transaction log (`TXN-9901`), and Consolidated Invoice Generation.
9. **Patient Portal**
   - Portal Login Settings, Online Appointment Booking, Prescription View, PDF Lab Report Downloads, Online Payments, and Medical History EMR logs.

---

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI (Python 3.10+)
- **Database**: SQLite with SQLAlchemy 2.0 ORM
- **Validation**: Pydantic v2
- **Security**: PyJWT, passlib / bcrypt
- **Testing**: Pytest & FastAPI TestClient

### Frontend
- **Framework**: React 18 (Vite)
- **Styling**: TailwindCSS
- **Icons**: Lucide React
- **Routing**: React Router DOM v7

---

## 💻 Installation & Quick Start

### Prerequisites
- **Python 3.10+**
- **Node.js 18+** & `npm`

### 1. Backend Setup

```bash
# Navigate to project folder
cd Hospital_app

# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Start FastAPI server
python -m uvicorn hms_backend.app.main:app --host 127.0.0.1 --port 8000
```
Backend API will be running at `http://127.0.0.1:8000`  
Swagger API Docs available at `http://127.0.0.1:8000/docs`

### 2. Frontend Setup

```bash
# Navigate to frontend folder
cd Hospital_app/hms-frontend

# Install dependencies
npm install

# Start Vite development server
npm run dev
```
Frontend Web App will be running at `http://localhost:5173/`

---

## 🧪 Running Automated Tests

Run the full 8-dimensional test suite (23 test cases):

```bash
# Run pytest with verbose output
.\.venv\Scripts\python.exe -m pytest -v
```

### Test Coverage Summary:
- **Unit Tests** (`test_unit.py`): Password hashing, JWT token validation, invoice calculations, stock alerts, bed allocations.
- **Integration Tests** (`test_integration.py`): CRUD operations for Patients, Doctors, and System Health Check.
- **End-to-End Tests** (`test_e2e.py`): 27 API endpoints across all 9 modules.
- **Functional Tests** (`test_functional.py`): Full clinical patient journey (Registration ➔ Appointment ➔ Diagnosis ➔ Prescription ➔ Billing).
- **Security Tests** (`test_security.py`): Login validation, invalid token rejection, password hash strength, CORS headers.
- **Performance Tests** (`test_performance.py`): Latency benchmarking & batch throughput.
- **Database Audit Tests** (`test_database_persistence_and_deletion.py`): Soft deletion logging & persistence in `deleted_records`.
- **Compatibility Tests** (`test_compatibility.py`): OpenAPI schema & legacy route alias verification.

---

## 📂 Project Repository

- **Git Remote**: `https://github.com/abishxavier/Hospital_app.git`
- **Active Branches**: `main`, `bharath`

---

## 📄 License

This project is licensed under the **MIT License**.
