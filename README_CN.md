# 文字转语音 (TTS) 服务

一个基于Web的文字转语音应用程序，使用Google文字转语音API将文本输入转换为音频。该应用程序具有带有FastAPI后端的Streamlit前端。这个重构版本包括改进的架构、配置管理和部署选项。

## 功能特点

- 将文本转换为多种语言的语音
- 支持不同的语音速度（正常和慢速）
- 基于Web的界面，易于使用
- 音频下载功能
- 具有实时反馈的响应式用户界面
- 模块化架构，分离API和前端服务
- 配置管理
- Docker支持，便于部署

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

### 运行完整应用程序

启动API和前端服务器：

```bash
python app.py
```

这将启动FastAPI后端服务器（端口8000）和Streamlit前端（端口8501）。

### 单独运行服务

仅运行API服务器：

```bash
python run_api.py
```

仅运行前端服务器：

```bash
python run_frontend.py
```

### 使用Docker

使用Docker Compose构建和运行：

```bash
docker-compose up --build
```

或运行单个服务：

```bash
# 构建镜像
docker build -t tts-service .

# 运行完整应用程序
docker run -p 8000:8000 -p 8501:8501 tts-service
```

## 架构

重构后的应用程序遵循模块化架构：

- **`api/`** - 包含FastAPI后端实现
- **`frontend/`** - 包含Streamlit前端实现
- **`config/`** - 包含配置设置和环境管理
- **`utils/`** - 包含实用函数
- **`app.py`** - 启动两个服务的主要入口点
- **`run_api.py`** - 仅API模式的入口点
- **`run_frontend.py`** - 仅前端模式的入口点

### API端点

- **POST** `/api/tts`
  - 请求体：`{"text": string, "lang": string, "slow": boolean}`
  - 响应：MP3格式的音频文件

## 配置

应用程序使用支持环境变量的配置系统：

- `API_HOST`: API服务器主机（默认："0.0.0.0"）
- `API_PORT`: API服务器端口（默认：8000）
- `FRONTEND_HOST`: 前端服务器主机（默认："0.0.0.0"）
- `FRONTEND_PORT`: 前端服务器端口（默认：8501）
- `DEBUG`: 启用调试模式（默认：false）
- `GTTS_TIMEOUT`: TTS生成超时（默认：10）

## 依赖项

- `streamlit` - 用于Web界面
- `fastapi` - 用于API后端
- `uvicorn[standard]` - FastAPI的ASGI服务器（包含标准扩展）
- `gtts` - Google文字转语音库
- `requests` - 用于前端和后端之间的HTTP请求
- `python-multipart` - 用于处理多部分数据
- `pydantic` - 数据验证和设置管理

## 项目结构

```
/workspace/
├── api/                    # FastAPI后端
│   └── tts_api.py          # API端点和逻辑
├── frontend/               # Streamlit前端
│   └── tts_frontend.py     # Web界面
├── config/                 # 配置
│   └── settings.py         # 应用程序设置
├── utils/                  # 实用函数
│   └── helpers.py          # 辅助函数
├── app.py                  # 主应用程序入口点
├── run_api.py              # 仅API启动脚本
├── run_frontend.py         # 仅前端启动脚本
├── requirements.txt        # Python依赖项
├── Dockerfile             # 容器配置
├── docker-compose.yml     # 多容器编排
└── README.md              # 文档
```

## 许可证

该项目是开源的，根据MIT许可证提供。