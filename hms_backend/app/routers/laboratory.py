from fastapi import APIRouter

router = APIRouter(prefix="/api/laboratory", tags=["laboratory"])

@router.get("/tests")
def get_lab_tests():
    return {"message": "Laboratory tests endpoint"}
