from fastapi import APIRouter

router = APIRouter(prefix="/api/portal", tags=["portal"])

@router.get("/profile")
def get_portal_profile():
    return {"message": "Patient portal profile endpoint"}
