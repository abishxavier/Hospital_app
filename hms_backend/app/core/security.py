from datetime import datetime, timedelta
from typing import Any

import jwt

from hms_backend.app.core.config import settings


ALGORITHM = "HS256"


def create_access_token(
    subject: str | Any,
    expires_minutes: int = 60,
    *,
    role: str | None = None,
    name: str | None = None,
) -> str:
    expiry = datetime.utcnow() + timedelta(minutes=expires_minutes)
    payload: dict[str, Any] = {"sub": str(subject), "exp": expiry}
    if role is not None:
        payload["role"] = role
    if name is not None:
        payload["name"] = name
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def verify_token(token: str) -> dict[str, Any]:
    return jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
