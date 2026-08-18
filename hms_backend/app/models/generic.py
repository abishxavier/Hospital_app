from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from datetime import datetime, timezone
from hms_backend.app.core.database import Base


class GenericRecord(Base):
    __tablename__ = "generic_records"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), index=True, nullable=False)
    data = Column(Text, nullable=False)  # JSON formatted key-value map
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
