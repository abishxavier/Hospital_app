def generate_pdf_report(title: str, content: str) -> dict:
    """Generates PDF report metadata or stream."""
    return {
        "status": "generated",
        "title": title,
        "file_name": f"{title.lower().replace(' ', '_')}.pdf",
        "download_url": f"/api/v1/reports/download/{title.lower().replace(' ', '_')}.pdf"
    }
