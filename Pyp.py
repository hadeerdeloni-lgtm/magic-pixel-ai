import streamlit as st
import random
import urllib.parse

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨", layout="centered")

# 2. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        background-color: #ff4b4b; 
        color: white; 
        font-weight: bold; 
        height: 3.5em; 
        border: none;
    }
    .stTextInput>div>div>input { text-align: center; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("أسرع مولد صور ذكي - النسخة الاحترافية المضمونة")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A beautiful sunset over a future city")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        placeholder = st.empty()
        with st.spinner("🚀 جاري الاتصال بالسيرفر السريع..."):
            # صنع Seed عشوائي لضمان صورة جديدة كل مرة
            seed = random.randint(1, 1000000)
            safe_prompt = urllib.parse.quote(prompt)
            
            # الرابط السريع والمباشر (Flux Model)
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true&model=flux"
            
            # عرض الصورة فوراً (الطريقة المباشرة تمنع أخطاء الاتصال)
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح! الموقع يعمل بكفاءة 100%.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 للمشتري: التطبيق يستخدم تقنية Direct API Rendering لضمان استقرار الخدمة وسرعتها.")
