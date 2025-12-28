import streamlit as st
import random
import urllib.parse
import requests
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨", layout="centered")

# 2. تحسين المظهر (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; height: 3.5em; font-weight: bold; font-size: 18px; }
    .stTextInput>div>div>input { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.subheader("أسرع مولد صور بالذكاء الاصطناعي")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A beautiful landscape")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري معالجة الصورة... انتظر لحظة"):
            seed = random.randint(1, 999999)
            safe_prompt = urllib.parse.quote(prompt)
            # رابط الصورة
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true"
            
            # محاولة التحقق من أن الرابط شغال قبل عرضه
            try:
                # عرض الصورة بطريقة مباشرة ومضمونة
                st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
                st.balloons()
                st.success("✅ تم إظهار الصورة!")
            except:
                st.error("❌ عذراً، السيرفر مشغول حالياً. حاول مرة أخرى.")
    else:
        st.warning("⚠️ برجاء كتابة وصف")

# تذييل بسيط
st.markdown("---")
st.write("💡 نصيحة: إذا لم تظهر الصورة، اضغط على الزر مرة أخرى لتحديث الاتصال.")
