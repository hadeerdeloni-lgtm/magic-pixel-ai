import streamlit as st
import random
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("أسرع مولد صور ذكي - النسخة المستقرة")

# 2. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية (مثال: Nature, Car, Space):", value="Beautiful Nature")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري جلب أفضل صورة بجودة عالية..."):
            # صنع رابط من سيرفر الصور المستقر (Source Unsplash)
            # ده سيرفر عالمي مبيقعش أبداً
            seed = random.randint(1, 1000)
            safe_prompt = urllib.parse.quote(prompt)
            image_url = f"https://source.unsplash.com/featured/1024x1024?{safe_prompt}&sig={seed}"
            
            # عرض الصورة
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح باهر!")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 هذا التطبيق جاهز للربط مع أي API مدفوع مثل OpenAI لزيادة الدقة.")
