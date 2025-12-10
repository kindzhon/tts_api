"""
Script to run only the frontend server
"""
from config.settings import settings
import subprocess
import sys


if __name__ == "__main__":
    print(f"🎨 Starting TTS Frontend Server...")
    print(f"🌐 Frontend running on: http://{settings.FRONTEND_HOST}:{settings.FRONTEND_PORT}")
    
    # Run streamlit app using subprocess
    cmd = [
        sys.executable, "-m", "streamlit", "run", 
        "frontend/tts_frontend.py",
        "--server.address", settings.FRONTEND_HOST,
        "--server.port", str(settings.FRONTEND_PORT),
        "--server.headless", "true"  # Don't automatically open browser
    ]
    
    subprocess.run(cmd)