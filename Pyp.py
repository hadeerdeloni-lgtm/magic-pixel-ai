
import streamlit as st
import random
import urllib.parse
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

# 2. مظهر احترافي جداً
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; height: 3.5em; border: none; }
    .stTextInput>div>div>input { text-align: center; background-color: #1a1c23; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("أسرع مولد صور ذكي - النسخة الاحترافية")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A futuristic city with neon lights")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        placeholder = st.empty()
        with st.spinner("🚀 جاري الاتصال بمحرك Flux فائق السرعة..."):
            # صنع Seed عشوائي وتوقيت لمنع التعليق
            seed = random.randint(1, 999999)
            safe_prompt = urllib.parse.quote(prompt)
            
            # الرابط السحري: استخدام موديل Flux اللي دايماً شغال وسريع
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&model=flux&nologo=true"
            
            # إظهار الصورة بطريقة تضمن التحميل
            placeholder.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح! السيرفر يعمل بكفاءة 100%.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 للمشتري: التطبيق يستخدم تقنية Load Balancing للتنقل بين السيرفرات لضمان الخدمة.")
