import json
from sqlalchemy.orm import Session
from hms_backend.app.models.audit import DeletedRecord


def log_deleted_record(db: Session, entity_type: str, entity_id: int, data: dict):
    """
    Saves a snapshot of deleted items into the deleted_records audit table in SQLite hms.db
    """
    try:
        data_str = json.dumps(data, default=str)
    except Exception:
        data_str = str(data)

    record = DeletedRecord(
        entity_type=entity_type,
        entity_id=entity_id,
        deleted_data=data_str
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
