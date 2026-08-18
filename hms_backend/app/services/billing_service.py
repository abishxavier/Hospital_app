def calculate_invoice_total(items: list) -> float:
    """Calculates total invoice amount from item list."""
    total = 0.0
    for item in items:
        price = float(item.get("price", 0.0))
        qty = int(item.get("qty", 1))
        total += price * qty
    return round(total, 2)
