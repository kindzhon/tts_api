"""
Main application entry point
This file provides a unified way to start both the API and frontend services.
"""
import uvicorn
import streamlit.web.bootstrap
import streamlit.web.cli
import multiprocessing
import time
import sys
import os
from pathlib import Path


def run_api_server():
    """Run the FastAPI server"""
    from config.settings import settings
    
    uvicorn.run(
        "api.tts_api:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        log_level="info" if settings.DEBUG else "warning"
    )


def run_frontend_server():
    """Run the Streamlit frontend"""
    from config.settings import settings
    import subprocess
    import sys
    
    # Run streamlit app using subprocess
    cmd = [
        sys.executable, "-m", "streamlit", "run", 
        "frontend/tts_frontend.py",
        "--server.address", settings.FRONTEND_HOST,
        "--server.port", str(settings.FRONTEND_PORT),
        "--server.headless", "true"  # Don't automatically open browser
    ]
    
    subprocess.run(cmd)


def main():
    """Main entry point to start both services"""
    from config.settings import settings
    
    print(f"🚀 Starting {settings.APP_NAME}")
    print(f"🌍 API Server will run on: {settings.api_url}")
    print(f"🌐 Frontend will run on: http://{settings.FRONTEND_HOST}:{settings.FRONTEND_PORT}")
    
    # Start API server process
    api_process = multiprocessing.Process(target=run_api_server, name="api_server")
    api_process.start()
    
    # Wait a moment for the API server to start
    time.sleep(2)
    
    # Check if API server started successfully
    if api_process.is_alive():
        print("✅ API server started successfully")
    else:
        print("❌ Failed to start API server")
        sys.exit(1)
    
    try:
        # Start frontend server in current process (since Streamlit handles its own process management)
        print("🎨 Starting frontend server...")
        run_frontend_server()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
    finally:
        # Terminate the API process
        api_process.terminate()
        api_process.join(timeout=5)
        if api_process.is_alive():
            api_process.kill()
        print("👋 TTS Service stopped")


if __name__ == "__main__":
    main()