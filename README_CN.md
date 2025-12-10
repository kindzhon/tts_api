# 文字转语音 (TTS) 服务

一个基于Web的文字转语音应用程序，使用Google文字转语音API将文本输入转换为音频。该应用程序具有带有FastAPI后端的Streamlit前端。

## 功能特点

- 将文本转换为多种语言的语音
- 支持不同的语音速度（正常和慢速）
- 基于Web的界面，易于使用
- 音频下载功能
- 具有实时反馈的响应式用户界面

## 支持的语言

- 英语 (`en`)
- 简体中文 (`zh-CN`)
- 西班牙语 (`es`)
- 法语 (`fr`)
- 日语 (`ja`)
- 韩语 (`ko`)

## 安装

1. 克隆仓库（或导航到项目目录）
2. 安装所需依赖项：

```bash
pip install -r requirements.txt
```

## 使用方法

运行主应用程序：

```bash
python main.py
```

这将启动FastAPI后端服务器（端口8000）和Streamlit前端（端口8501）。可以通过网络浏览器访问应用程序。

## 架构

该应用程序由两个主要组件组成：

1. **FastAPI后端** - 提供用于文字转语音转换的REST API端点（`/api/tts`）
2. **Streamlit前端** - Web界面，允许用户输入文本、选择语言和速度选项，并与TTS服务交互

## API端点

- **POST** `/api/tts`
  - 请求体：`{"text": string, "lang": string, "slow": boolean}`
  - 响应：MP3格式的音频文件

## 依赖项

- `streamlit` - 用于Web界面
- `fastapi` - 用于API后端
- `uvicorn` - FastAPI的ASGI服务器
- `gtts` - Google文字转语音库
- `requests` - 用于前端和后端之间的HTTP请求
- `python-multipart` - 用于处理多部分数据

## 许可证

该项目是开源的，根据MIT许可证提供。