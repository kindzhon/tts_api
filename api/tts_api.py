"""
TTS API Module
This module contains the FastAPI application for the Text-to-Speech service.
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from gtts import gTTS
from io import BytesIO


class TTSPayload(BaseModel):
    text: str
    lang: str = "en"
    slow: bool = False


def generate_tts(text: str, lang: str, slow: bool) -> bytes:
    """
    Generate TTS audio from text
    :param text: Input text
    :param lang: Language code
    :param slow: Whether to use slow speed
    :return: Audio bytes
    """
    try:
        tts = gTTS(text=text, lang=lang, slow=slow, timeout=10)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.getvalue()
    except Exception as e:
        raise ValueError(f"Error generating TTS: {str(e)}")


def create_api_app():
    """Create and configure the FastAPI application"""
    api_app = FastAPI(title="TTS API", description="Text-to-Speech API Service")
    
    @api_app.post("/api/tts", response_class=Response)
    async def tts_endpoint(payload: TTSPayload):
        try:
            audio = generate_tts(payload.text, payload.lang, payload.slow)
            return Response(content=audio, media_type="audio/mpeg")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    return api_app


# Create the API application instance
app = create_api_app()