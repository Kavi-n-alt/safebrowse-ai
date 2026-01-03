
import os
import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

print("Starting model training...", flush=True)

# Path to dataset
DATA_PATH = "data/synthetic_sessions.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

# Load dataset
df = pd.read_csv(DATA_PATH)
print("Data loaded:", df.shape, flush=True)

# Feature list
FEATURES = df.columns.tolist()

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Train Isolation Forest
model = IsolationForest(
    n_estimators=200,
    contamination=0.12,
    random_state=42
)
model.fit(X_scaled)

# Save artifacts
os.makedirs("ml/artifacts", exist_ok=True)
joblib.dump(model, "ml/artifacts/model.pkl")
joblib.dump(scaler, "ml/artifacts/scaler.pkl")
joblib.dump(FEATURES, "ml/artifacts/features.pkl")

print("Model trained and artifacts saved successfully.", flush=True)
