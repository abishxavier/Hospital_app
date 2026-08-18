import json
from sqlalchemy.orm import Session
from hms_backend.app.models.generic import GenericRecord
from hms_backend.app.utils.audit import log_deleted_record


def get_generic_records(db: Session, category: str, default_data: list = None):
    records = db.query(GenericRecord).filter(
        GenericRecord.category == category,
        GenericRecord.is_deleted == False
    ).order_by(GenericRecord.id.desc()).all()

    if not records and default_data:
        for item in default_data:
            data_copy = {k: v for k, v in item.items() if k != "id"}
            rec = GenericRecord(category=category, data=json.dumps(data_copy), is_deleted=False)
            db.add(rec)
        db.commit()

        records = db.query(GenericRecord).filter(
            GenericRecord.category == category,
            GenericRecord.is_deleted == False
        ).order_by(GenericRecord.id.desc()).all()

    res = []
    for r in records:
        try:
            item_data = json.loads(r.data)
        except Exception:
            item_data = {}
        item_data["id"] = r.id
        res.append(item_data)
    return res


def create_generic_record(db: Session, category: str, payload: dict):
    clean_payload = {k: v for k, v in payload.items() if k != "id"}
    rec = GenericRecord(category=category, data=json.dumps(clean_payload), is_deleted=False)
    db.add(rec)
    db.commit()
    db.refresh(rec)

    item_data = clean_payload.copy()
    item_data["id"] = rec.id
    return item_data


def delete_generic_record(db: Session, category: str, record_id: int):
    rec = db.query(GenericRecord).filter(
        GenericRecord.id == record_id,
        GenericRecord.category == category
    ).first()

    if not rec:
        rec = db.query(GenericRecord).filter(GenericRecord.id == record_id).first()

    if not rec:
        return {"status": "error", "message": "Record not found"}

    try:
        data_snapshot = json.loads(rec.data)
    except Exception:
        data_snapshot = {"id": rec.id}
    data_snapshot["id"] = rec.id

    rec.is_deleted = True
    log_deleted_record(db, category.replace("_", " ").title(), rec.id, data_snapshot)
    db.commit()

    return {"status": "success", "message": f"Record #{record_id} marked as deleted in database and saved in deleted_records table."}
