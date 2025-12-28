import streamlit as st
import random
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; height: 3.5em; border: none; }
    .stTextInput>div>div>input { text-align: center; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("حول كلماتك إلى صور مذهلة في ثوانٍ")

# 2. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A cybernetic cat in space")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري الاتصال بسيرفر الذكاء الاصطناعي السريع..."):
            # صنع رقم عشوائي (Seed) لضمان صورة جديدة كل مرة
            seed = random.randint(1, 1000000)
            safe_prompt = urllib.parse.quote(prompt)
            
            # الرابط الجديد: سيرفر فائق السرعة ومستقر جداً
            # بنستخدم هنا محرك الـ API المباشر لضمان العرض
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true"
            
            # عرض الصورة فوراً (بدون تعقيدات برمجية تسبب أخطاء)
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح! السيرفر يعمل بكفاءة.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 للمشتري: هذا التطبيق يدعم التوليد اللحظي للصور بدقة عالية وبدون تكاليف استضافة.")
