# SafeBrowse AI - Online Safety Guardian for Children

**Hack2Skill Ranchi Hackathon 2026 Submission**

An AI-powered browser extension and monitoring system that protects children from harmful online content through real-time risk assessment, behavioral analysis, and parent dashboards.

## Problem Statement
**SafeBrowse (Wipro)** - The AI toolkit to keep your young ones safe online.

## Key Features

### 1. Real-Time Content Analysis
- Analyzes webpage text in real-time using AI-driven risk detection
- Identifies harmful content categories:
  - Self-harm and suicide-related content
  - Sexual and explicit material
  - Cyberbullying and abusive language
  - Grooming patterns and predatory behavior
  - Scams and fraudulent content

### 2. Risk Scoring Engine
- 0-100 risk score for every page visited
- Color-coded alerts (green/yellow/red) based on risk level
- Non-intrusive banner notifications on risky pages

### 3. Parent Dashboard
- Real-time monitoring of child's browsing activity
- Statistics on high-risk, medium-risk, and low-risk events
- Timeline view of all browsing sessions
- Addiction score based on usage patterns
- Emotional state indicators derived from browsing behavior

### 4. Behavioral Insights
- Screen time tracking
- Usage pattern analysis
- Addiction risk assessment
- Emotional state detection (stressed/neutral based on content exposure)

## Technical Architecture

### Backend (FastAPI)
- **Language**: Python 3
- **Framework**: FastAPI
- **Database**: JSON file-based storage (easily upgradable to MongoDB/PostgreSQL)
- **AI/ML**: Rule-based NLP with pattern matching for harmful content detection

### Chrome Extension
- **Manifest V3** compliant
- Content scripts for page text extraction
- Real-time communication with backend
- Visual notifications for users

### Dashboard
- **Tech**: Vanilla HTML/CSS/JavaScript
- Real-time data fetching via REST API
- Responsive design
- Auto-refresh every 10 seconds

## Project Structure
```
safebrowse-ai/
├── backend/
│   ├── main.py              # FastAPI backend with risk detection logic
│   ├── requirements.txt     # Python dependencies
│   └── db.json             # Auto-generated event database
├── extension/
│   ├── manifest.json        # Extension configuration
│   ├── content.js          # Page analysis script
│   └── popup.html          # Extension popup UI
├── dashboard/
│   └── index.html          # Parent dashboard
└── README.md
```

## Setup Instructions

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the FastAPI server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

### Chrome Extension Installation

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" (toggle in top-right)
3. Click "Load unpacked"
4. Select the `extension/` folder from this project
5. The SafeBrowse AI extension should now appear in your browser

### Accessing the Dashboard

Once the backend is running:
- Open `dashboard/index.html` in your browser, OR
- Navigate to `http://localhost:8000` and click dashboard link

## API Endpoints

### POST /analyze
Analyzes webpage content and returns risk assessment
```json
{
  "url": "https://example.com",
  "text": "page content...",
  "user_id": "demo_child"
}
```

Response:
```json
{
  "risk_score": 75,
  "category": "bullying",
  "explanation": "Bullying language detected",
  "timestamp": "2025-12-21T22:00:00"
}
```

### GET /events
Retrieve recent browsing events

### GET /stats
Get aggregated statistics (high/medium/low risk counts, addiction score, emotional state)

## How It Works

1. **User browses the web** → Extension monitors all pages
2. **Content extraction** → Content script extracts visible text from page
3. **AI Analysis** → Text sent to backend for risk assessment
4. **Risk Detection** → Pattern matching identifies harmful content
5. **User Notification** → Banner shows risk level on page
6. **Event Logging** → All events stored in database
7. **Parent Dashboard** → Real-time view of child's activity

## Safety Categories Detected

| Category | Risk Indicators | Examples |
|----------|----------------|----------|
| **Self-Harm** | Suicide keywords, self-harm phrases | "want to die", "kill myself" |
| **Sexual Content** | Explicit keywords | "porn", "nude", "xxx" |
| **Cyberbullying** | Abusive language | "kill yourself", "loser", "worthless" |
| **Grooming** | Predatory patterns | "don't tell your parents", "send pic" |
| **Scams** | Fraud indicators | "click to win", "claim your prize" |

## UN SDG Alignment

✅ **SDG 3**: Good Health and Well-Being  
✅ **SDG 4**: Quality Education  
✅ **SDG 16**: Peace, Justice, and Strong Institutions

This project directly contributes to child safety, mental health protection, and preventing online abuse.

## Innovation Highlights

1. **Psychological Approach**: Goes beyond URL blocking to analyze actual content and behavior
2. **Proactive Protection**: Detects grooming patterns before harm occurs
3. **Non-Invasive**: Works quietly in background without disrupting normal browsing
4. **Parent Empowerment**: Dashboard provides actionable insights
5. **Scalable Architecture**: Easy to add ML models (BERT, toxicity classifiers) in future

## Future Enhancements

- [ ] Webcam-based emotion detection using computer vision
- [ ] Integration with OpenAI/HuggingFace for advanced NLP
- [ ] NSFW image detection
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Real-time parent alerts via SMS/Email
- [ ] Machine learning model training on labeled dataset
- [ ] Browser history analysis for pattern detection

## Demo Video
[Link to demo video will be added]

## Team
- Solo Developer: Kavi-n-alt
- Institution: [Your Institution]
- Hackathon: Hack2Skill Ranchi 2026

## License
MIT License - Open source for educational and safety purposes

## Acknowledgments
- Hack2Skill for organizing the hackathon
- Wipro for the problem statement
- CyberPeace Foundation for online safety advocacy

---

**Built with ❤️ for child safety and digital well-being**
