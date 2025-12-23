import streamlit as st
import requests
import io
import time
from PIL import Image

# 1. إعدادات الواجهة الاحترافية
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #6200ea;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎨 Magic Pixel AI")
st.write("حول كلماتك إلى لوحات فنية مذهلة باستخدام الذكاء الاصطناعي")

# 2. بيانات المحرك والـ Token الجديد الخاص بكِ
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
# تم تحديث الـ Token هنا بناءً على طلبك
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

# 3. مدخلات المستخدم
prompt = st.text_input("صف الصورة التي تتخيلها (بالإنجليزي):", placeholder="e.g. A futuristic car in a neon city")

if st.button("توليد الصورة ✨"):
    if prompt:
        with st.spinner("الذكاء الاصطناعي يرسم الآن..."):
            attempts = 0
            success = False
            while attempts < 3 and not success:
                response = query({"inputs": prompt})
                
                # حالة النجاح
                if response.status_code == 200 and b"estimated_time" not in response.content:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, caption="رؤيتك أصبحت حقيقة!", use_container_width=True)
                    
                    # تحويل الصورة للتحميل
                    buf = io.BytesIO()
                    image.save(buf, format="PNG")
                    st.download_button(label="📥 تحميل الصورة", data=buf.getvalue(), file_name="ai_art.png", mime="image/png")
                    success = True
                
                # حالة تحميل الموديل (Loading)
                elif b"estimated_time" in response.content:
                    st.info("السيرفر يستعد.. سأحاول مجدداً خلال 15 ثانية")
                    time.sleep(15)
                    attempts += 1
                
                else:
                    st.error(f"خطأ: {response.status_code}. قد يكون الـ Token محظور من GitHub، سأعلمك كيف تخفيه في الخطوة القادمة.")
                    break
    else:
        st.warning("من فضلك اكتب وصفاً أولاً!")

st.markdown("---")
st.caption("Powered by Hadeer's AI Engine | 2024")
