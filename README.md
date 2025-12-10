# Text-to-Speech (TTS) Service

A web-based Text-to-Speech application that converts text input into audio using Google's Text-to-Speech API. The application features a Streamlit frontend with a FastAPI backend. This refactored version includes improved architecture, configuration management, and deployment options.

## Features

- Convert text to speech in multiple languages
- Support for different speech speeds (normal and slow)
- Web-based interface for easy use
- Audio download functionality
- Responsive UI with real-time feedback
- Modular architecture with separate API and frontend services
- Configuration management
- Docker support for easy deployment

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

### Running the Full Application

To start both the API and frontend servers:

```bash
python app.py
```

This will start the FastAPI backend server (on port 8000) and the Streamlit frontend (on port 8501).

### Running Services Separately

To run only the API server:

```bash
python run_api.py
```

To run only the frontend server:

```bash
python run_frontend.py
```

### Using Docker

Build and run with Docker Compose:

```bash
docker-compose up --build
```

Or run individual services:

```bash
# Build the image
docker build -t tts-service .

# Run the full application
docker run -p 8000:8000 -p 8501:8501 tts-service
```

## Architecture

The refactored application follows a modular architecture:

- **`api/`** - Contains the FastAPI backend implementation
- **`frontend/`** - Contains the Streamlit frontend implementation
- **`config/`** - Contains configuration settings and environment management
- **`utils/`** - Contains utility functions and helpers
- **`app.py`** - Main entry point to start both services
- **`run_api.py`** - Entry point for API-only mode
- **`run_frontend.py`** - Entry point for frontend-only mode

### API Endpoints

- **POST** `/api/tts`
  - Request body: `{"text": string, "lang": string, "slow": boolean}`
  - Response: Audio file in MP3 format

## Configuration

The application uses a configuration system that supports environment variables:

- `API_HOST`: Host for the API server (default: "0.0.0.0")
- `API_PORT`: Port for the API server (default: 8000)
- `FRONTEND_HOST`: Host for the frontend server (default: "0.0.0.0")
- `FRONTEND_PORT`: Port for the frontend server (default: 8501)
- `DEBUG`: Enable debug mode (default: false)
- `GTTS_TIMEOUT`: Timeout for TTS generation (default: 10)

## Dependencies

- `streamlit` - For the web interface
- `fastapi` - For the API backend
- `uvicorn[standard]` - ASGI server for FastAPI with standard extras
- `gtts` - Google Text-to-Speech library
- `requests` - For HTTP requests between frontend and backend
- `python-multipart` - For handling multipart data
- `pydantic` - Data validation and settings management

## Project Structure

```
/workspace/
├── api/                    # FastAPI backend
│   └── tts_api.py          # API endpoints and logic
├── frontend/               # Streamlit frontend
│   └── tts_frontend.py     # Web interface
├── config/                 # Configuration
│   └── settings.py         # Application settings
├── utils/                  # Utility functions
│   └── helpers.py          # Helper functions
├── app.py                  # Main application entry point
├── run_api.py              # API-only startup script
├── run_frontend.py         # Frontend-only startup script
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Multi-container orchestration
└── README.md              # Documentation
```

## License

This project is open source and available under the MIT License.