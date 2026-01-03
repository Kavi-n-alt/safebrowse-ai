import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class ModelRegistry:
    model = None
    scaler = None
    features = None

def load_model():
    ModelRegistry.model = joblib.load(
        os.path.join(BASE_DIR, "ml", "artifacts", "model.pkl")
    )
    ModelRegistry.scaler = joblib.load(
        os.path.join(BASE_DIR, "ml", "artifacts", "scaler.pkl")
    )
    ModelRegistry.features = joblib.load(
        os.path.join(BASE_DIR, "ml", "artifacts", "features.pkl")
    )
