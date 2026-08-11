# Hospital Management System

This workspace includes a working FastAPI backend and a React dashboard foundation for an HMS application.

## Run the backend

```bash
python -m pip install -r requirements.txt
uvicorn hms_backend.app.main:app --reload --port 8000
```

## Run the frontend

```bash
cd hms-frontend
npm install
npm run dev
```

The frontend expects the backend at http://127.0.0.1:8000.

## Environment variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Example values:

```env
APP_NAME=Hospital Management API
DATABASE_URL=sqlite:///./hms.db
SECRET_KEY=change-me
```

## API overview

- `GET /` — health welcome endpoint
- `GET /health` — database connectivity check
- `POST /api/v1/auth/login` — admin/reception login demo endpoint
- `GET /api/v1/patients/` — list patients
- `GET /api/v1/appointments/` — list appointments
- `GET /api/dashboard` — mock dashboard summary

## Status

The project is currently at the foundation stage with the backend scaffolding, data models, and a dashboard shell in place. The next layer is module-by-module business logic for staff, billing, lab, pharmacy, and inpatient workflows.

## License

MIT
