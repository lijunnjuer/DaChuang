def calculate_risk_level(value: float) -> str:
    if value <= 0.1:
        return "LOW"
    if value <= 0.3:
        return "MEDIUM"
    return "HIGH"
