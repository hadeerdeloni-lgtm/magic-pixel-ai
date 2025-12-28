
import streamlit as st
import random
import urllib.parse
import time

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Magic Pixel AI - Pro Edition", page_icon="🎨", layout="centered")

# 2. تصميم واجهة المستخدم (Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        background-color: #ff4b4b; 
        color: white; 
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #1a1c23;
        color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.subheader("أقوى محرك لتوليد الصور الاحترافية")

# 3. خانة الوصف
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية (مثال: Cyberpunk City):", value="A futuristic city with neon lights")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        placeholder = st.empty()
        with st.spinner("🚀 جاري استدعاء الذكاء الاصطناعي..."):
            # توليد Seed عشوائي وتوقيت زمني لمنع التكرار (Cache Busting)
            seed = random.randint(1, 1000000)
            timestamp = time.time()
            safe_prompt = urllib.parse.quote(prompt)
            
            # الرابط المطور لضمان التحديث المستمر والجودة العالية
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true&enhance=true&t={timestamp}"
            
            # عرض الصورة
            placeholder.image(image_url, caption=f"النتيجة لـ: {prompt}", use_container_width=True)
            st.balloons()
            st.success("✨ تم التوليد بنجاح! الصورة الآن فريدة وجاهزة.")
    else:
        st.warning("⚠️ برجاء إدخال وصف أولاً")

# تذييل الصفحة
st.markdown("---")
st.caption("Powered by Magic Pixel AI - High Quality Image Generation")
