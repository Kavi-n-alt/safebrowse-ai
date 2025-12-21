from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
from typing import List
import json
import os

app = FastAPI(title="SafeBrowse AI Backend")

# CORS for extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "db.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {"events": []}

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

class AnalyzeRequest(BaseModel):
    url: str
    text: str
    user_id: str = "demo"

class AnalyzeResponse(BaseModel):
    risk_score: int
    category: str
    explanation: str
    timestamp: str

class Event(BaseModel):
    url: str
    risk_score: int
    category: str
    timestamp: str
    user_id: str

# Risk detection - human style logic
def detect_risk(text: str):
    text_lower = text.lower()
    score = 0
    category = "safe"
    reasons = []
    
    # Self-harm detection
    suicide_words = ["suicide", "kill myself", "end my life", "want to die", "better off dead"]
    if any(word in text_lower for word in suicide_words):
        score += 70
        category = "self-harm"
        reasons.append("Self-harm language detected")
    
    # Sexual content
    sexual_words = ["sex", "porn", "nude", "naked", "xxx"]
    sexual_count = sum(1 for word in sexual_words if word in text_lower)
    if sexual_count >= 2:
        score += 60
        category = "sexual" if category == "safe" else category
        reasons.append("Sexual content detected")
    
    # Cyberbullying
    bully_words = ["kill yourself", "loser", "idiot", "stupid", "ugly", "fat", "worthless", "hate you"]
    bully_count = sum(1 for word in bully_words if word in text_lower)
    if bully_count >= 2:
        score += 50
        category = "bullying" if category == "safe" else category
        reasons.append("Bullying language detected")
    
    # Grooming patterns
    grooming_phrases = ["don't tell your parents", "keep this secret", "send me a photo", "send pic", 
                        "meet in person", "come over", "are you alone"]
    if any(phrase in text_lower for phrase in grooming_phrases):
        score += 80
        category = "grooming"
        reasons.append("Potential grooming behavior detected")
    
    # Scam/fraud
    scam_words = ["click here to win", "congratulations you won", "claim your prize", "send money", "wire transfer"]
    if any(word in text_lower for word in scam_words):
        score += 40
        category = "scam" if category == "safe" else category
        reasons.append("Potential scam detected")
    
    if score == 0:
        score = 10
        reasons.append("No red flags detected")
    else:
        score = min(score, 100)
    
    explanation = "; ".join(reasons)
    return score, category, explanation

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_content(req: AnalyzeRequest):
    score, category, explanation = detect_risk(req.text)
    timestamp = datetime.utcnow().isoformat()
    
    # Save to DB
    db = load_db()
    db["events"].append({
        "url": req.url,
        "risk_score": score,
        "category": category,
        "timestamp": timestamp,
        "user_id": req.user_id
    })
    db["events"] = db["events"][-100:]  # Keep last 100
    save_db(db)
    
    return AnalyzeResponse(
        risk_score=score,
        category=category,
        explanation=explanation,
        timestamp=timestamp
    )

@app.get("/events", response_model=List[Event])
def get_events(limit: int = 50):
    db = load_db()
    events = db["events"][-limit:]
    events.reverse()
    return events

@app.get("/stats")
def get_stats():
    db = load_db()
    events = db["events"]
    
    total = len(events)
    high_risk = len([e for e in events if e["risk_score"] >= 70])
    medium_risk = len([e for e in events if 40 <= e["risk_score"] < 70])
    low_risk = len([e for e in events if e["risk_score"] < 40])
    
    recent = events[-20:]
    addiction_score = min(len(recent) * 5, 100)
    
    avg_risk = sum(e["risk_score"] for e in recent) // len(recent) if recent else 0
    emotion = "Stressed" if avg_risk > 60 else "Neutral"
    
    return {
        "total_events": total,
        "high_risk": high_risk,
        "medium_risk": medium_risk,
        "low_risk": low_risk,
        "addiction_score": addiction_score,
        "emotional_state": emotion
    }

@app.get("/")
def root():
    return {"message": "SafeBrowse AI Backend is running", "status": "active"}
