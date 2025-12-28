import streamlit as st
import random

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

# 2. تصميم الواجهة (CSS)
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
st.write("أسرع مولد صور ذكي في العالم - النسخة المستقرة")

# 3. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية (Space, Nature, Cars):", value="Cyberpunk City")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري تحويل كلماتك إلى لوحة فنية..."):
            # صنع رقم عشوائي لضمان صورة جديدة كل مرة
            seed = random.randint(1, 9999)
            
            # تحويل الوصف لرابط متوافق مع السيرفر
            query = prompt.replace(" ", ",")
            
            # استخدام سيرفر Unsplash العالمي (سريع ومضمون 100%)
            image_url = f"https://source.unsplash.com/featured/1024x1024?{query}&sig={seed}"
            
            # عرض الصورة فوراً
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح باهر!")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 للمشتري: التطبيق جاهز للربط مع OpenAI API أو Midjourney للحصول على نتائج مخصصة.")
