#!/usr/bin/env python
"""
测试运行脚本
用于运行项目的所有单元测试
"""

import unittest
import sys
import os

if __name__ == '__main__':
    # 添加项目根目录到Python路径
    sys.path.insert(0, os.path.dirname(__file__))
    
    # 自动发现并运行所有测试
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 根据测试结果设置退出码
    sys.exit(0 if result.wasSuccessful() else 1)