"""
Script to run only the API server
"""
from config.settings import settings
import uvicorn


if __name__ == "__main__":
    from api.tts_api import app
    
    print(f"🚀 Starting TTS API Server...")
    print(f"🌍 API Server running on: {settings.api_url}")
    
    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level="info" if settings.DEBUG else "warning"
    )