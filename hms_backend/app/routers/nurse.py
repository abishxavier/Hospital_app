from fastapi import APIRouter

router = APIRouter(prefix="/api/nurse", tags=["nurse"])

@router.get("/vitals")
def get_vitals():
    return {"message": "Nurse vitals endpoint"}
