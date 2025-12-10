"""
Utility functions for the TTS application
"""
import os
from typing import Dict, Any
from gtts import gTTS
from io import BytesIO


def validate_text(text: str, max_length: int = 5000) -> bool:
    """
    Validate the input text
    :param text: Input text to validate
    :param max_length: Maximum allowed length
    :return: True if valid, False otherwise
    """
    if not text or not text.strip():
        return False
    if len(text.strip()) > max_length:
        return False
    return True


def validate_language(lang: str, supported_languages: Dict[str, str]) -> bool:
    """
    Validate the language code
    :param lang: Language code to validate
    :param supported_languages: Dictionary of supported languages
    :return: True if valid, False otherwise
    """
    return lang in supported_languages


def generate_tts_audio(text: str, lang: str = "en", slow: bool = False, timeout: int = 10) -> bytes:
    """
    Generate TTS audio from text
    :param text: Input text
    :param lang: Language code
    :param slow: Whether to use slow speed
    :param timeout: Request timeout
    :return: Audio bytes
    """
    try:
        tts = gTTS(text=text, lang=lang, slow=slow, timeout=timeout)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.getvalue()
    except Exception as e:
        raise ValueError(f"Error generating TTS: {str(e)}")


def sanitize_filename(text: str, max_length: int = 20) -> str:
    """
    Sanitize text to create a valid filename
    :param text: Input text
    :param max_length: Maximum length for filename
    :return: Sanitized filename
    """
    # Remove invalid characters for filenames
    sanitized = "".join(c for c in text[:max_length] if c.isalnum() or c in (' ', '-', '_')).rstrip()
    return sanitized if sanitized else "tts_output"


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human readable format
    :param size_bytes: Size in bytes
    :return: Formatted size string
    """
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"