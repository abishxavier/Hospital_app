def send_notification(recipient: str, message: str, type: str = "info") -> dict:
    """Dispatches system notifications."""
    return {
        "status": "sent",
        "recipient": recipient,
        "type": type,
        "message": message
    }
