def calculate_risk(anomaly_score: float):
    risk_score = int((1 - anomaly_score) * 100)

    if risk_score <= 30:
        level = "LOW"
    elif risk_score <= 60:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return risk_score, level
