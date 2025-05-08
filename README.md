# Voice Assistant Web App

A browser-based voice assistant that understands your speech and responds with intelligent actions using a Python-powered backend.

## Features

- Voice input using Web Speech API (frontend)
- Natural language processing and response generation (backend)
- Text-to-speech response using `pyttsx3`
- Supports basic tasks like:
  - Searching the web
  - Opening apps (Windows)
  - Fetching time/date
  - Reading/writing files
  - Wikipedia summaries

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice_assistant.git
cd voice_assistant
```

### 2. Setup Backend

cd backend
npm install

Make sure Python is installed and required Python packages are set up. If not, run this command:

pip install speechrecognition pyttsx3 nltk wikipedia

### 3. Setup Frontend

cd ../frontend
npm install
npm start

### 4. Run the Backend

In a separate terminal:

cd backend
node server.js

### Notes

This version works best on Windows

For Linux/macOS, system commands in voice_assistant.py need to be adapted

The assistant speaks from the server machine, not client browser (for now)
