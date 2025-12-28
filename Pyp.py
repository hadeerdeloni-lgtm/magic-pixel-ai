
import streamlit as st
import random
import urllib.parse
import requests
from io import BytesIO
from PIL import Image

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("النسخة الاحترافية - توليد صور فائقة الجودة")

# 2. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A futuristic city")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري سحب البيانات وتجهيز اللوحة..."):
            seed = random.randint(1, 999999)
            safe_prompt = urllib.parse.quote(prompt)
            # استخدام موديل Flux القوي
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&model=flux&nologo=true"
            
            try:
                # التحميل المباشر للصورة من السيرفر
                response = requests.get(image_url, timeout=20)
                if response.status_code == 200:
                    # تحويل البيانات لصورة حقيقية
                    img = Image.open(BytesIO(response.content))
                    # عرض الصورة
                    st.image(img, caption=f"✨ Result for: {prompt}", use_container_width=True)
                    st.balloons()
                    st.success("✅ تم التوليد بنجاح باهر!")
                else:
                    st.error("⚠️ السيرفر مشغول، من فضلك اضغطي مرة أخرى.")
            except Exception as e:
                st.error("❌ عذراً، حاولي مرة أخرى بعد ثوانٍ.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 تقنية العرض: Image Buffer Streaming لضمان الاستقرار.")
