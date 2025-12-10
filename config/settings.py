"""
Configuration settings for the TTS application
"""
import os
from typing import Optional


class Settings:
    # API Server settings
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # Frontend settings
    FRONTEND_HOST: str = os.getenv("FRONTEND_HOST", "0.0.0.0")
    FRONTEND_PORT: int = int(os.getenv("FRONTEND_PORT", "8501"))
    
    # Application settings
    APP_NAME: str = "TTS Service"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Supported languages
    SUPPORTED_LANGUAGES: dict = {
        "en": "English",
        "zh-CN": "Chinese Simplified", 
        "es": "Spanish",
        "fr": "French",
        "ja": "Japanese",
        "ko": "Korean"
    }
    
    # GTTS settings
    GTTS_TIMEOUT: int = int(os.getenv("GTTS_TIMEOUT", "10"))
    
    @property
    def api_url(self) -> str:
        return f"http://{self.API_HOST}:{self.API_PORT}"


# Create a settings instance
settings = Settings()