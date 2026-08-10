# Hospital Management System

This workspace now includes a working FastAPI backend and a React dashboard shell for the HMS foundation.

## Run the backend

```bash
python -m pip install -r requirement.txt
uvicorn hms_backend.app.main:app --reload --port 8000
```

## Run the frontend

```bash
cd hms-frontend
npm install
npm run dev
```

The frontend expects the backend at http://127.0.0.1:8000.
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the app**

   Open your browser and navigate to: `http://localhost:5000`

---

## Environment Variables

For this demo, only basic variables are needed:

| Variable        | Description                       | Example                                      |
| --------------- | --------------------------------- | -------------------------------------------- |
| `SECRET_KEY`    | Flask secret key for sessions     | `demo-secret-key`                            |
| `DATABASE_URL`  | Database connection string        | `mysql://root:password@localhost/hospital_db` |
| `DEBUG`         | Enable/disable debug mode         | `True`                                       |

---

## Sample API Endpoints (Planned)

| Method | Endpoint                     | Description                   | Role      |
| ------ | ---------------------------- | ----------------------------- | --------- |
| POST   | `/api/auth/login`            | User login                    | All       |
| GET    | `/api/patients`              | List all patients             | Staff     |
| POST   | `/api/patients`              | Register a new patient        | Reception |
| GET    | `/api/appointments`          | List appointments             | Staff     |
| POST   | `/api/appointments`          | Book an appointment           | All       |
| GET    | `/api/pharmacy/inventory`    | View medicine inventory       | Pharmacy  |
| POST   | `/api/billing/invoice`       | Generate an invoice           | Billing   |
| GET    | `/api/lab/reports/:id`       | Download a lab report         | Staff     |

---

## Status

This project is currently in the **demo / prototype** stage. The modules listed above represent the planned scope. Implementation is in progress.

| Module           | Status       |
| ---------------- | ------------ |
| Admin            | 🔲 Planned   |
| Reception        | 🔲 Planned   |
| Doctor           | 🔲 Planned   |
| Nurse            | 🔲 Planned   |
| Laboratory       | 🔲 Planned   |
| Pharmacy         | 🔲 Planned   |
| Inpatient (IP)   | 🔲 Planned   |
| Billing          | 🔲 Planned   |
| Patient Portal   | 🔲 Planned   |

---

## License

This project is licensed under the **MIT License**.

---

<p align="center">
  🏥 Demo Project — Built for Review & Evaluation
</p>
