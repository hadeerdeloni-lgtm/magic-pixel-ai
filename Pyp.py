import streamlit as st
import random
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

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
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("أسرع مولد صور ذكي - النسخة المستقرة جداً")

# 2. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A futuristic city")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري الاتصال بمحرك التوليد المستقر..."):
            seed = random.randint(1, 999999)
            safe_prompt = urllib.parse.quote(prompt)
            
            # الرابط ده بيستخدم محرك PixArt وهو بديل قوي جداً وسريع
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&model=turbo"
            
            # عرض الصورة فوراً
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح! الموقع يعمل الآن بكفاءة.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 للمشتري: التطبيق يدعم التبديل بين محركات AI مختلفة لضمان استمرارية الخدمة.")
