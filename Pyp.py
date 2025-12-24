
import streamlit as st
import random
import urllib.parse

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Magic Pixel AI - Pro Edition", page_icon="🚀", layout="centered")

# تصميم واجهة المستخدم
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.subheader("أقوى محرك لتوليد الصور بالذكاء الاصطناعي")

# خانة الوصف
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A cybernetic cat in space")

col1, col2 = st.columns([1, 1])

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        placeholder = st.empty()
        with st.spinner("جاري الاتصال بالسيرفرات العملاقة..."):
            seed = random.randint(1, 999999)
            safe_prompt = urllib.parse.quote(prompt)
            # استخدام سيرفر فائق الجودة
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true&enhance=true"
            
            placeholder.image(image_url, caption=f"النتيجة لـ: {prompt}", use_container_width=True)
            st.balloons()
            st.success("تم التوليد بنجاح! يمكنك الآن بيع هذه الصورة أو حفظها.")
    else:
        st.warning("برجاء إدخال وصف أولاً")

st
