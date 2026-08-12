from fastapi import APIRouter

router = APIRouter(prefix="/api/inpatient", tags=["inpatient"])

@router.get("/wards")
def get_wards():
    return {"message": "Inpatient wards endpoint"}
