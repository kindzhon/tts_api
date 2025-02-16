# main.py
import streamlit as st
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import uvicorn
from multiprocessing import Process
from gtts import gTTS
from io import BytesIO
import requests

# ==============================
# FastAPI 服务端 (API 服务)
# ==============================
api_app = FastAPI(title="TTS API")

class TTSPayload(BaseModel):
    text: str
    lang: str = "en"
    slow: bool = False

def generate_tts(text: str, lang: str, slow: bool) -> bytes:
    try:
        tts = gTTS(text=text, lang=lang, slow=slow)
        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.getvalue()
    except Exception as e:
        raise ValueError(str(e))

@api_app.post("/api/tts")
async def tts_endpoint(payload: TTSPayload):
    try:
        audio = generate_tts(payload.text, payload.lang, payload.slow)
        return Response(content=audio, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def run_api_server():
    uvicorn.run(api_app, host="0.0.0.0", port=8000)

# ==============================
# Streamlit 网页端
# ==============================
def web_interface():
    st.set_page_config(page_title="TTS 服务", page_icon="🎤")
    st.title("🎤 文本转语音服务")
    
    # 界面布局
    col1, col2 = st.columns(2)
    with col1:
        text = st.text_area("输入文本", height=150, placeholder="输入要转换的文本...")
    with col2:
        lang = st.selectbox("选择语言", options=["en", "zh-CN", "es", "fr", "ja", "ko"])
        slow = st.checkbox("慢速模式")
    
    if st.button("✨ 生成语音"):
        if not text.strip():
            st.error("请输入文本内容")
            return
            
        with st.spinner("生成中..."):
            try:
                # 调用本地API
                response = requests.post(
                    "http://localhost:8000/api/tts",
                    json={"text": text, "lang": lang, "slow": slow}
                )
                
                if response.status_code == 200:
                    st.audio(response.content, format="audio/mpeg")
                    st.download_button(
                        "下载音频",
                        data=response.content,
                        file_name=f"tts_{lang}.mp3",
                        mime="audio/mpeg"
                    )
                else:
                    st.error(f"API 错误: {response.json()['detail']}")
            except Exception as e:
                st.error(f"请求失败: {str(e)}")

# ==============================
# 启动器
# ==============================
if __name__ == "__main__":
    # 启动 FastAPI 服务进程
    api_process = Process(target=run_api_server)
    api_process.start()
    
    # 启动 Streamlit 网页
    try:
        web_interface()
    finally:
        api_process.terminate()
