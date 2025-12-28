
import streamlit as st
import random
import urllib.parse
import time
import requests
from io import BytesIO

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")

# 2. تصميم احترافي
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A futuristic city")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري الاتصال بالسيرفر وتوليد الصورة... قد يستغرق ذلك 10 ثوانٍ"):
            seed = random.randint(1, 1000000)
            safe_prompt = urllib.parse.quote(prompt)
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true"
            
            try:
                # محاولة تحميل الصورة فعلياً للتأكد من وجودها
                response = requests.get(image_url, timeout=15)
                if response.status_code == 200:
                    # إذا نجح التحميل، نعرض الصورة من الذاكرة مباشرة
                    st.image(response.content, caption=f"✨ {prompt}", use_container_width=True)
                    st.balloons()
                    st.success("✅ تم التوليد بنجاح!")
                else:
                    st.error("❌ السيرفر مشغول حالياً، اضغطي على الزر مرة أخرى")
            except Exception as e:
                st.error("⚠️ يبدو أن هناك ضغطاً على الشبكة، يرجى المحاولة مرة ثانية")
    else:
        st.warning("⚠️ برجاء كتابة وصف أولاً")

st.markdown("---")
st.caption("نصيحة للمشتري: هذا التطبيق يعتمد على بروتوكول API مجاني لتقليل تكاليف التشغيل.")
