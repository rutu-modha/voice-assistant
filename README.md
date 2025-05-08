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
git clone https://github.com/rutu-modha/voice-assistant.git
cd voice-assistant
```

### 2. Setup Backend

```bash
cd backend
npm install
```

Run following command to install the required Python packages:

```bash
pip install speechrecognition pyttsx3 nltk wikipedia
```

### 3. Setup Frontend

```bash
cd ../frontend
npm install
npm start
```

### 4. Run the Backend

In a separate terminal:

```bash
cd backend
node server.js
```

### Notes

This version works best on Windows

For Linux/macOS, system commands in voice_assistant.py need to be adapted

The assistant speaks from the server machine, not client browser (for now)
