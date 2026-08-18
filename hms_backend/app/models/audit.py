from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from hms_backend.app.core.database import Base


class DeletedRecord(Base):
    __tablename__ = "deleted_records"

    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String(100), nullable=False)
    entity_id = Column(Integer, nullable=True)
    deleted_data = Column(Text, nullable=False)
    deleted_at = Column(DateTime, default=datetime.utcnow)
