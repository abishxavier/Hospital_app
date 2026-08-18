def allocate_bed(ward_id: int, bed_number: str) -> dict:
    """Allocates a bed for IPD patient admission."""
    return {
        "status": "success",
        "ward_id": ward_id,
        "bed_number": bed_number,
        "message": f"Bed {bed_number} successfully allocated in Ward #{ward_id}."
    }
