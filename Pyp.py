import streamlit as st
import random
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")

# 2. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A space explorer on Mars")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري الاتصال بمحرك التوليد المستقر..."):
            seed = random.randint(1, 1000000)
            safe_prompt = urllib.parse.quote(prompt)
            
            # 🟢 استخدام رابط بديل ومستقر جداً (سيرفر مختلف)
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&nologo=true&private=true"
            
            # العرض المباشر
            st.image(image_url, caption=f"✨ Result for: {prompt}", use_container_width=True)
            
            st.balloons()
            st.success("✅ تم التوليد بنجاح! السيرفر يعمل الآن.")
    else:
        st.warning("⚠️ يرجى كتابة وصف")

st.markdown("---")
st.caption("نصيحة: إذا تأخرت الصورة، فهذا بسبب ضغط عالمي مؤقت على الـ API المجاني.")
