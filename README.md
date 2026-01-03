# SafeBrowse AI  
## AI-Powered Web Threat & Anomaly Detection Backend

---

## Overview

SafeBrowse AI is an **AI-driven backend security service** that detects unsafe and anomalous web browsing behavior using **unsupervised anomaly detection**.

Traditional web security solutions rely heavily on static blacklists and predefined rules, which often fail to detect newly emerging or zero-day threats. SafeBrowse AI addresses this limitation by learning **normal browsing behavior** and identifying **deviations that may indicate malicious or risky activity**.

The system is designed as a **stateless ML microservice**, making it suitable for integration with browser extensions, enterprise security tools, or monitoring platforms.

---

## Problem Statement

Modern internet users are exposed to phishing websites, scam pages, malicious redirects, and unsafe browsing behavior.  
Most existing browser security mechanisms are reactive and depend on known attack signatures or URL blacklists, which are ineffective against previously unseen threats.

There is a need for a system that can **proactively identify unsafe browsing behavior**, even when the website has never been reported before.

---

## Solution Approach

SafeBrowse AI uses **anomaly detection** to model normal web browsing patterns and flag abnormal behavior that may indicate security risks.

Instead of binary “safe/unsafe” decisions, the system produces **risk-based assessments** with explainable signals, allowing for better security decision-making.

---

## Key Features

- Unsupervised anomaly detection using Isolation Forest  
- Real-time risk scoring (LOW / MEDIUM / HIGH)  
- Explainable risk signals (redirect patterns, URL entropy, script behavior)  
- Production-style FastAPI backend  
- Stateless, API-first architecture  
- Swagger (OpenAPI) documentation for easy testing  

---

## System Architecture

Client / Tool / Extension
↓
FastAPI Backend (Stateless)
↓
Feature Engineering
↓
Anomaly Detection Model
↓
Risk Scoring & Signals
↓
JSON API Response

yaml
Copy code

---

## Machine Learning Design

- **Model:** Isolation Forest  
- **Learning Type:** Unsupervised  
- **Training Data:** Synthetic browsing telemetry (privacy-safe)  
- **Why Anomaly Detection:**  
  - Web security data is largely unlabeled  
  - Zero-day threats cannot be captured by rule-based systems  
  - Anomaly detection enables early discovery of unseen threats  

---

## Technology Stack

- **Programming Language:** Python  
- **Backend Framework:** FastAPI  
- **Machine Learning:** Scikit-learn (Isolation Forest)  
- **Data Processing:** Pandas, NumPy  
- **Model Persistence:** Joblib  
- **API Documentation:** Swagger (OpenAPI)  

---

## API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/health` | Service health check |
| POST | `/api/v1/analyze` | Analyze browsing session and return risk assessment |

---

## Example API Response

```json
{
  "risk_score": 82,
  "risk_level": "HIGH",
  "signals": {
    "redirects": "excessive",
    "url_entropy": "high",
    "script_density": "abnormal"
  }
}
Design Decisions & Justification
No frontend:
The project is designed as a backend intelligence service intended to be consumed by other systems. Swagger UI is sufficient for interaction and testing.

No heavy database:
Real-time inference does not require persistence. Optional lightweight logging can be added without altering the core design.

Feature-based analysis:
Behavioral features are used instead of deep content scraping to ensure performance and deployability.

Future Enhancements
Browser extension integration

Security dashboards and analytics

Persistent audit logging

Continuous model retraining

Enterprise policy enforcement

Project Status
✔ Dataset generated
✔ ML model trained
✔ Backend API implemented
✔ End-to-end testing completed
✔ Ready for integration and extension

Author
SafeBrowse AI — Designed and implemented as an industry-aligned AI backend security system for real-world applicability.

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


    ## Team
        - Solo Developer: Kavi-n-alt
        - Institution: Chennai Institute of Technology

    ## License
        MIT License - Open source for educational and safety purposes

   ## Acknowledgments
        - Hack2Skill for organizing the hackathon
        - Wipro for the problem statement
        - CyberPeace Foundation for online safety advocacy
                

        **Built with ❤️ for child safety and digital well-being**