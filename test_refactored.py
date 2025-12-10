#!/usr/bin/env python3
"""
Quick test script to verify the refactored code works as expected
"""
import os
import sys
import tempfile
from pathlib import Path

# Add workspace to path
sys.path.insert(0, str(Path(__file__).parent))

def test_api_module():
    """Test the API module functionality"""
    print("Testing API module...")
    from api.tts_api import generate_tts
    
    # Test basic TTS generation
    try:
        audio_data = generate_tts("Hello, this is a test.", "en", slow=False)
        assert len(audio_data) > 0, "Generated audio should not be empty"
        print("✅ API module test passed")
        return True
    except Exception as e:
        print(f"❌ API module test failed: {e}")
        return False


def test_config_module():
    """Test the configuration module"""
    print("Testing configuration module...")
    from config.settings import settings
    
    # Test basic settings
    assert settings.API_PORT == 8000, f"Expected API_PORT to be 8000, got {settings.API_PORT}"
    assert settings.FRONTEND_PORT == 8501, f"Expected FRONTEND_PORT to be 8501, got {settings.FRONTEND_PORT}"
    assert "en" in settings.SUPPORTED_LANGUAGES, "English should be in supported languages"
    
    print("✅ Configuration module test passed")
    return True


def test_helpers_module():
    """Test the helpers module"""
    print("Testing helpers module...")
    from utils.helpers import validate_text, validate_language, generate_tts_audio, sanitize_filename
    
    # Test text validation
    assert validate_text("Hello world") == True, "Valid text should pass validation"
    assert validate_text("") == False, "Empty text should fail validation"
    assert validate_text("   ") == False, "Whitespace-only text should fail validation"
    
    # Test language validation
    from config.settings import settings
    assert validate_language("en", settings.SUPPORTED_LANGUAGES) == True, "English should be valid language"
    assert validate_language("invalid", settings.SUPPORTED_LANGUAGES) == False, "Invalid language should fail"
    
    # Test filename sanitization
    assert sanitize_filename("Hello World") == "Hello World", "Simple text should be preserved"
    assert sanitize_filename("Hello/World!") == "HelloWorld", "Invalid characters should be removed"
    
    print("✅ Helpers module test passed")
    return True


def test_frontend_import():
    """Test that frontend module can be imported without errors"""
    print("Testing frontend module import...")
    try:
        from frontend.tts_frontend import web_interface
        print("✅ Frontend module import test passed")
        return True
    except ImportError as e:
        print(f"❌ Frontend module import test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("🧪 Running tests on refactored code...")
    print()
    
    tests = [
        test_api_module,
        test_config_module,
        test_helpers_module,
        test_frontend_import,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The refactored code is working correctly.")
        return True
    else:
        print("❌ Some tests failed.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)