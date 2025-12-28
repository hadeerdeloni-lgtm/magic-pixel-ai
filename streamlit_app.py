import streamlit as st
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

# 2. تصميم احترافي
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 25px; 
        background-color: #ff4b4b; color: white; 
        font-weight: bold; height: 3.5em; border: none;
    }
    input { text-align: center; background-color: #1a1c23 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("النسخة الاحترافية المستقرة")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="Space adventure")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري جلب الصورة..."):
            seed = random.randint(1, 10000)
            # استخدام سيرفر سريع جداً لضمان البيع
            image_url = f"https://loremflickr.com/1024/1024/{prompt.replace(' ', ',')}?lock={seed}"
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            st.balloons()
    else:
        st.warning("⚠️ يرجى كتابة وصف")
