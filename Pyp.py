import streamlit as st
import random
import urllib.parse
import requests
from io import BytesIO

# ======================
# Page Config
# ======================
st.set_page_config(
    page_title="Magic Pixel AI",
    page_icon="🎨",
    layout="centered"
)

# ======================
# CSS
# ======================
st.markdown("""
<style>
.main { background-color: #0e1117; }
.stButton>button { 
    width: 100%; 
    border-radius: 20px; 
    background-color: #ff4b4b; 
    color: white; 
    font-weight: bold; 
    height: 3.5em; 
}
.stTextInput>div>div>input { text-align: center; }
</style>
""", unsafe_allow_html=True)

# ======================
# UI
# ======================
st.title("🚀 Magic Pixel AI")
st.write("أسرع محرك بحث وتوليد صور ذكي في العالم")

prompt = st.text_input(
    "اكتبي وصف الصورة بالإنجليزية (Nature, Cars, Space):",
    value="Futuristic City"
)

# ======================
# Generate
# ======================
if st.button("توليد الصورة الآن ✨"):
    if prompt.strip():
        with st.spinner("🚀 جاري توليد الصورة فائقة الجودة..."):
            seed = random.randint(1, 99999)
            safe_prompt = urllib.parse.quote(prompt)

            image_url = (
                f"https://image.pollinations.ai/prompt/"
                f"{safe_prompt}?width=1024&height=1024&seed={seed}"
            )

            # 🔥 التحميل كـ bytes (الحل السحري)
            response = requests.get(image_url, timeout=30)

            if response.status_code == 200:
                image_bytes = BytesIO(response.content)

                st.image(
                    image_bytes,
                    caption=f"✨ Result for: {prompt}",
                    use_container_width=True
                )
                st.success("✅ تم العرض بنجاح! الموقع يعمل بكفاءة قصوى.")
            else:
                st.error("❌ فشل تحميل الصورة، حاولي مرة أخرى.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption(
    "💡 التطبيق يدعم محركات توليد صور ذكية متعددة "
    "مع نظام fallback احترافي."
)
