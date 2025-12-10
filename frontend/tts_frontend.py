"""
TTS Frontend Module
This module contains the Streamlit web interface for the Text-to-Speech service.
"""
import streamlit as st
import requests


def web_interface():
    """Create and run the Streamlit web interface"""
    st.set_page_config(
        page_title="TTS 服务", 
        page_icon="🎤",
        layout="wide"
    )
    
    st.title("🎤 文本转语音服务")
    st.markdown("---")
    
    # 界面布局
    col1, col2 = st.columns([2, 1])
    
    with col1:
        text = st.text_area(
            "📝 输入文本", 
            height=200, 
            placeholder="输入要转换的文本...",
            key="text_input"
        )
    
    with col2:
        st.subheader("⚙️ 设置")
        lang = st.selectbox(
            "🌐 选择语言", 
            options=[
                ("en", "英语"), 
                ("zh-CN", "简体中文"), 
                ("es", "西班牙语"), 
                ("fr", "法语"), 
                ("ja", "日语"), 
                ("ko", "韩语")
            ],
            format_func=lambda x: x[1],  # Display the language name
            key="lang_select"
        )[0]  # Get the language code
        
        slow = st.checkbox("🐌 慢速模式", key="slow_mode")
        
        # API server URL
        api_url = st.text_input(
            "🔗 API 服务器地址",
            value="http://localhost:8000",
            key="api_url"
        )
    
    if st.button("✨ 生成语音", type="primary", use_container_width=True):
        if not text.strip():
            st.error("❌ 请输入文本内容")
            return
            
        with st.spinner("🔊 正在生成语音..."):
            try:
                # 调用API
                response = requests.post(
                    f"{api_url}/api/tts",
                    json={"text": text, "lang": lang, "slow": slow},
                    timeout=30
                )
                
                if response.status_code == 200:
                    st.success("✅ 语音生成成功！")
                    
                    # Display audio player
                    st.subheader("🎧 音频播放")
                    st.audio(response.content, format="audio/mpeg")
                    
                    # Add download button
                    st.subheader("💾 下载音频")
                    st.download_button(
                        label="📥 下载 MP3",
                        data=response.content,
                        file_name=f"tts_{lang}_{len(text[:20])}.mp3",
                        mime="audio/mpeg"
                    )
                else:
                    try:
                        error_detail = response.json().get('detail', '未知错误')
                    except:
                        error_detail = response.text or '未知错误'
                    st.error(f"❌ API 错误: {error_detail}")
                    
            except requests.exceptions.Timeout:
                st.error("⏰ 请求超时，请检查API服务器是否运行正常")
            except requests.exceptions.ConnectionError:
                st.error("🔌 无法连接到API服务器，请检查服务器地址")
            except Exception as e:
                st.error(f"❌ 请求失败: {str(e)}")

    # Add footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Text-to-Speech Service &copy; 2023"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    web_interface()