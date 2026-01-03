from fastapi import FastAPI
from app.api.analyze import router as analyze_router
from app.ml.model_loader import load_model

app = FastAPI(title="SafeBrowse AI")

@app.on_event("startup")
def startup_event():
    print("Starting SafeBrowse AI...", flush=True)
    load_model()
    print("Model loaded. API ready.", flush=True)


@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(analyze_router, prefix="/api/v1")
