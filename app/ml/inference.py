import numpy as np
from app.ml.model_loader import ModelRegistry

def run_inference(feature_dict: dict) -> float:
    ordered = [feature_dict[f] for f in ModelRegistry.features]
    X = ModelRegistry.scaler.transform([ordered])
    score = ModelRegistry.model.decision_function(X)[0]
    return score
