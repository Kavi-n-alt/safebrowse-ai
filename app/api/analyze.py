from fastapi import APIRouter, HTTPException
from app.schemas.request import AnalyzeRequest
from app.schemas.response import AnalyzeResponse
from app.ml.inference import run_inference
from app.ml.risk import calculate_risk

router = APIRouter()

def extract_signals(features: dict):
    signals = {}

    if features["num_redirects"] > 3:
        signals["redirects"] = "excessive"
    if features["url_entropy"] > 4.0:
        signals["url_entropy"] = "high"
    if features["script_density"] > 0.6:
        signals["script_density"] = "abnormal"

    return signals

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    try:
        features = req.dict()
        anomaly_score = run_inference(features)
        risk_score, level = calculate_risk(anomaly_score)

        return {
            "risk_score": risk_score,
            "risk_level": level,
            "signals": extract_signals(features)
        }

    except Exception:
        raise HTTPException(status_code=500, detail="Analysis failed")
