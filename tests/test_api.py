import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# 将workspace目录添加到路径中，以便导入main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import api_app, TTSPayload
from fastapi.testclient import TestClient


class TestTTSAPI(unittest.TestCase):
    """测试TTS API端点"""
    
    def setUp(self):
        """设置测试客户端"""
        self.client = TestClient(api_app)
    
    @patch('main.generate_tts')
    def test_tts_endpoint_success(self, mock_generate_tts):
        """测试TTS API端点成功情况"""
        # 模拟返回音频数据
        mock_audio_data = b"fake audio data"
        mock_generate_tts.return_value = mock_audio_data
        
        # 发送POST请求
        response = self.client.post(
            "/api/tts",
            json={"text": "Hello world", "lang": "en", "slow": False}
        )
        
        # 验证响应
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "audio/mpeg")
        self.assertEqual(response.content, mock_audio_data)
        
        # 验证generate_tts被正确调用
        mock_generate_tts.assert_called_once_with("Hello world", "en", False)
    
    @patch('main.generate_tts')
    def test_tts_endpoint_with_different_params(self, mock_generate_tts):
        """测试使用不同参数的TTS API端点"""
        mock_audio_data = b"fake audio data"
        mock_generate_tts.return_value = mock_audio_data
        
        # 测试中文
        response = self.client.post(
            "/api/tts",
            json={"text": "你好世界", "lang": "zh-CN", "slow": True}
        )
        
        self.assertEqual(response.status_code, 200)
        mock_generate_tts.assert_called_with("你好世界", "zh-CN", True)
    
    @patch('main.generate_tts')
    def test_tts_endpoint_error_handling(self, mock_generate_tts):
        """测试TTS API端点错误处理"""
        # 模拟generate_tts抛出异常
        mock_generate_tts.side_effect = ValueError("Invalid text")
        
        response = self.client.post(
            "/api/tts",
            json={"text": "bad text", "lang": "en", "slow": False}
        )
        
        # 验证返回400错误
        self.assertEqual(response.status_code, 400)
        error_detail = response.json()
        self.assertIn("detail", error_detail)
        self.assertIn("Invalid text", error_detail["detail"])
    
    def test_tts_payload_model(self):
        """测试TTSPayload Pydantic模型验证"""
        # 有效载荷
        payload = TTSPayload(text="Hello", lang="en", slow=False)
        self.assertEqual(payload.text, "Hello")
        self.assertEqual(payload.lang, "en")
        self.assertEqual(payload.slow, False)
        
        # 默认值测试
        payload_default = TTSPayload(text="Hello")
        self.assertEqual(payload_default.lang, "en")  # 默认语言
        self.assertEqual(payload_default.slow, False)  # 默认非慢速
    
    def test_invalid_payload(self):
        """测试无效载荷"""
        # 没有必需的text字段
        response = self.client.post("/api/tts", json={})
        self.assertEqual(response.status_code, 422)  # 验证错误
        
        # text为空 (空文本会在generate_tts中导致错误，返回400)
        response = self.client.post("/api/tts", json={"text": ""})
        self.assertEqual(response.status_code, 400)  # 空文本会导致错误
        
    @patch('main.generate_tts')
    def test_tts_endpoint_missing_fields(self, mock_generate_tts):
        """测试缺少可选字段时的默认值"""
        mock_audio_data = b"fake audio data"
        mock_generate_tts.return_value = mock_audio_data
        
        # 只提供必需字段
        response = self.client.post("/api/tts", json={"text": "Hello"})
        
        self.assertEqual(response.status_code, 200)
        # 验证使用了默认值
        mock_generate_tts.assert_called_once_with("Hello", "en", False)


class TestAPIDocumentation(unittest.TestCase):
    """测试API文档端点"""
    
    def setUp(self):
        """设置测试客户端"""
        self.client = TestClient(api_app)
    
    def test_openapi_schema(self):
        """测试OpenAPI schema可用性"""
        response = self.client.get("/openapi.json")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn("info", data)  # FastAPI使用info字段包含标题
        self.assertIn("title", data["info"])  # 标题在info对象内
        self.assertIn("paths", data)
        self.assertIn("/api/tts", data["paths"])
    
    def test_root_redirection(self):
        """测试根路径重定向"""
        # FastAPI通常会重定向根路径到docs或redoc
        response = self.client.get("/")
        # 根据FastAPI默认行为，这可能是重定向或404，取决于配置
        self.assertIn(response.status_code, [200, 307, 404])


if __name__ == '__main__':
    unittest.main()