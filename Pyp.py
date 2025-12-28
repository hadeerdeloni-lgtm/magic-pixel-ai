import streamlit as st
import random
import urllib.parse
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")

# 2. تحسين المظهر
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A futuristic city")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري تصميم صورتك الفريدة..."):
            # صنع رابط فريد جداً لمنع أي تهنيج
            seed = random.randint(1, 1000000)
            safe_prompt = urllib.parse.quote(prompt)
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true"
            
            # إضافة وقت انتظار بسيط لضمان استجابة السيرفر
            time.sleep(2) 
            
            # عرض الصورة مباشرة
            st.image(image_url, caption=f"✨ {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم إظهار الصورة بنجاح!")
    else:
        st.warning("⚠️ برجاء كتابة وصف")
