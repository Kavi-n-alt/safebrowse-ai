# SafeBrowse AI - Quick Setup Guide

## ✅ Environment Already Set Up!

Your virtual environment is ready and all dependencies are installed.

## 🚀 How to Run the Project

### Method 1: Using the Start Script (Easiest)

```bash
./start.sh
```

This will:
- Activate the virtual environment automatically
- Install/update dependencies if needed
- Start the FastAPI backend server on http://localhost:8000

### Method 2: Manual Start

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Navigate to backend
cd backend

# 3. Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 Accessing the Application

Once the server is running:

1. **API Documentation**: http://localhost:8000/docs
2. **Parent Dashboard**: Open `dashboard/index.html` in your browser
3. **Chrome Extension**: Load the `extension/` folder in Chrome

## 🔧 Installing Chrome Extension

1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" (toggle in top-right)
3. Click "Load unpacked"
4. Select the `extension/` folder from this project
5. The SafeBrowse AI extension will appear in your browser toolbar

## ✨ Testing the System

1. Start the backend server (using either method above)
2. Load the Chrome extension
3. Visit any website
4. The extension will automatically analyze the page content
5. Check the Parent Dashboard to see logged events

## 📊 API Endpoints

- `GET /` - Server health check
- `POST /analyze` - Analyze webpage content
- `GET /events` - Get browsing history
- `GET /stats` - Get statistics (risk counts, addiction score)

## 🛑 Stopping the Server

Press `CTRL+C` in the terminal

## 🎯 For Hackathon Submission

### What's Been Done:

✅ Python 3.12.1 installed
✅ Virtual environment created (`venv/`)
✅ All dependencies installed (FastAPI, Uvicorn, Pydantic)
✅ Backend tested and working
✅ Zero errors, production-ready
✅ Easy one-command startup

### Repository:
https://github.com/Kavi-n-alt/safebrowse-ai

---
**Good luck with your hackathon! ��**
