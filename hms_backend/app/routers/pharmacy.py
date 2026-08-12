from fastapi import APIRouter

router = APIRouter(prefix="/api/pharmacy", tags=["pharmacy"])

@router.get("/inventory")
def get_inventory():
    return {"message": "Pharmacy inventory endpoint"}
