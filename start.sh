#!/bin/bash
echo "SafeBrowse AI - Starting Backend Server"
echo "=========================================="

# Activate virtual environment
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r backend/requirements.txt > /dev/null 2>&1

echo "Starting FastAPI server on http://localhost:8000"
echo "Press CTRL+C to stop the server"
echo ""

# Start server
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
