from fastapi import APIRouter

router = APIRouter(prefix="/api/billing", tags=["billing"])

@router.get("/invoices")
def get_invoices():
    return {"message": "Billing invoices endpoint"}
