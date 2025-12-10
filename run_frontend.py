"""
Script to run only the frontend server
"""
from config.settings import settings
import streamlit.web.bootstrap
import streamlit.web.cli
import sys
import os


if __name__ == "__main__":
    print(f"🎨 Starting TTS Frontend Server...")
    print(f"🌐 Frontend running on: http://{settings.FRONTEND_HOST}:{settings.FRONTEND_PORT}")
    
    # Set environment variables for streamlit
    os.environ['STREAMLIT_SERVER_PORT'] = str(settings.FRONTEND_PORT)
    
    # Run streamlit app
    sys.argv = [
        "streamlit", "run", 
        "frontend/tts_frontend.py",
        "--server.address", settings.FRONTEND_HOST,
        "--server.port", str(settings.FRONTEND_PORT),
        "--server.headless", "true"  # Don't automatically open browser
    ]
    
    streamlit.web.cli.main()