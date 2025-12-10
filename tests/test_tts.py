import unittest
from unittest.mock import patch, MagicMock
from io import BytesIO
import sys
import os

# 将workspace目录添加到路径中，以便导入main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import generate_tts, TTSPayload


class TestTTSFunctions(unittest.TestCase):
    
    def test_tts_payload_creation(self):
        """测试TTSPayload模型的创建"""
        payload = TTSPayload(text="Hello world", lang="en", slow=False)
        self.assertEqual(payload.text, "Hello world")
        self.assertEqual(payload.lang, "en")
        self.assertEqual(payload.slow, False)
        
        # 测试默认值
        payload_default = TTSPayload(text="Hello world")
        self.assertEqual(payload_default.lang, "en")
        self.assertEqual(payload_default.slow, False)
    
    @patch('main.gTTS')
    def test_generate_tts_success(self, mock_gtts):
        """测试generate_tts函数成功生成音频"""
        # 模拟gTTS对象
        mock_tts_instance = MagicMock()
        mock_tts_instance.write_to_fp = MagicMock()
        mock_gtts.return_value = mock_tts_instance
        
        # 测试基本文本转语音
        text = "Hello world"
        lang = "en"
        slow = False
        
        result = generate_tts(text, lang, slow)
        
        # 验证gTTS被正确调用
        mock_gtts.assert_called_once_with(text=text, lang=lang, slow=slow)
        # 验证write_to_fp被调用
        mock_tts_instance.write_to_fp.assert_called_once()
        # 结果应该是一个字节串
        self.assertIsInstance(result, bytes)
    
    @patch('main.gTTS')
    def test_generate_tts_with_different_params(self, mock_gtts):
        """测试不同参数的generate_tts函数"""
        mock_tts_instance = MagicMock()
        mock_tts_instance.write_to_fp = MagicMock()
        mock_gtts.return_value = mock_tts_instance
        
        # 测试中文
        result = generate_tts("你好世界", "zh-CN", False)
        mock_gtts.assert_called_with(text="你好世界", lang="zh-CN", slow=False)
        
        # 测试慢速模式
        result = generate_tts("Hello", "en", True)
        mock_gtts.assert_called_with(text="Hello", lang="en", slow=True)
    
    @patch('main.gTTS')
    def test_generate_tts_exception_handling(self, mock_gtts):
        """测试generate_tts函数异常处理"""
        # 模拟gTTS抛出异常
        mock_gtts.side_effect = Exception("Invalid input")
        
        with self.assertRaises(ValueError) as context:
            generate_tts("test", "en", False)
        
        self.assertIn("Invalid input", str(context.exception))
    
    def test_generate_tts_empty_text(self):
        """测试空文本的处理"""
        with self.assertRaises(ValueError):
            generate_tts("", "en", False)


class TestAPIStructure(unittest.TestCase):
    """测试API相关结构"""
    
    def test_tts_payload_validation(self):
        """测试TTSPayload验证"""
        # 有效的载荷
        valid_payload = TTSPayload(text="test text")
        self.assertEqual(valid_payload.text, "test text")
        
        # 验证必须字段
        with self.assertRaises(ValueError):
            TTSPayload()  # 没有必需的text字段


if __name__ == '__main__':
    unittest.main()