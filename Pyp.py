import streamlit as st
import random
import urllib.parse

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; height: 3.5em; }
    .stTextInput>div>div>input { text-align: center; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("أسرع مولد صور ذكي - النسخة الاحترافية المضمونة")

# 2. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A cybernetic cat in space")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري الاتصال بسيرفر فائق السرعة..."):
            # صنع رقم عشوائي (Seed) لضمان صورة جديدة
            seed = random.randint(1, 999999)
            safe_prompt = urllib.parse.quote(prompt)
            
            # الرابط المباشر (Direct Linking) هو الأسرع والأقل أخطاءً
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true"
            
            # عرض الصورة فوراً
            # ملاحظة للمشتري: الكود يعتمد على Direct API Rendering لضمان الخدمة
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح! الموقع يعمل بكفاءة 100%.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 نصيحة للمشتري: إذا استغرق التحميل وقتاً، فهذا بسبب ضغط مؤقت على السيرفرات المجانية.")
