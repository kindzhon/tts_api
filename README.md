# Text-to-Speech (TTS) Service

A web-based Text-to-Speech application that converts text input into audio using Google's Text-to-Speech API. The application features a Streamlit frontend with a FastAPI backend.

## Features

- Convert text to speech in multiple languages
- Support for different speech speeds (normal and slow)
- Web-based interface for easy use
- Audio download functionality
- Responsive UI with real-time feedback

## Supported Languages

- English (`en`)
- Chinese Simplified (`zh-CN`)
- Spanish (`es`)
- French (`fr`)
- Japanese (`ja`)
- Korean (`ko`)

## Installation

1. Clone the repository (or navigate to the project directory)
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main application:

```bash
python main.py
```

This will start both the FastAPI backend server (on port 8000) and the Streamlit frontend (on port 8501). The application will be accessible through your web browser.

## Architecture

The application consists of two main components:

1. **FastAPI Backend** - Provides a REST API endpoint (`/api/tts`) for text-to-speech conversion
2. **Streamlit Frontend** - Web interface that allows users to input text, select language and speed options, and interact with the TTS service

## API Endpoint

- **POST** `/api/tts`
  - Request body: `{"text": string, "lang": string, "slow": boolean}`
  - Response: Audio file in MP3 format

## Dependencies

- `streamlit` - For the web interface
- `fastapi` - For the API backend
- `uvicorn` - ASGI server for FastAPI
- `gtts` - Google Text-to-Speech library
- `requests` - For HTTP requests between frontend and backend
- `python-multipart` - For handling multipart data

## License

This project is open source and available under the MIT License.