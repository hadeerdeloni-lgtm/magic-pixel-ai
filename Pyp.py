
import streamlit as st
import random
import urllib.parse
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

# 2. مظهر احترافي
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("حول كلماتك إلى لوحات فنية في ثوانٍ")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A magical forest with glowing lights")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري الاتصال بسيرفر الذكاء الاصطناعي..."):
            seed = random.randint(1, 1000000)
            safe_prompt = urllib.parse.quote(prompt)
            
            # استخدام محرك مختلف (Stable Diffusion عبر سيرفر سريع)
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&model=flux"
            
            # عرض الصورة فوراً
            st.image(image_url, caption=f"✨ {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح! يمكنك حفظ الصورة الآن.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("نصيحة للمشتري: التطبيق يعتمد على أقوى موديلات AI (Flux) لضمان جودة الصور.")
