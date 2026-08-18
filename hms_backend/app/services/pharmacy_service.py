def check_low_stock_alerts(medicines: list) -> list:
    """Returns alert items for low stock medicines."""
    alerts = []
    for med in medicines:
        stock = getattr(med, "stock_qty", 0)
        if stock < 100:
            alerts.append({
                "id": getattr(med, "id", 0),
                "Medicine Name": getattr(med, "name", "Medicine"),
                "Alert Type": "Low Stock",
                "Current Stock": f"{stock} Units",
                "Action Required": "Re-order Stock"
            })
    return alerts
