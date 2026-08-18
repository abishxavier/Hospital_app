from fastapi import APIRouter

router = APIRouter(prefix="/ambulance", tags=["ambulance"])


@router.get("/fleet")
def get_ambulance_fleet():
    return [
        {"id": 1, "Vehicle Number": "AMB-101", "Driver Name": "Ramesh Kumar", "Phone": "+91 98989 11223", "Status": "Available"},
        {"id": 2, "Vehicle Number": "AMB-102", "Driver Name": "Suresh Patel", "Phone": "+91 98989 44556", "Status": "On Call"},
    ]


@router.get("/bookings")
def get_emergency_bookings():
    return [
        {"id": 1, "Patient": "Emergency Call #901", "Pickup Location": "MG Road Crossing, Block B", "Ambulance": "AMB-102", "Status": "Dispatched"},
    ]
