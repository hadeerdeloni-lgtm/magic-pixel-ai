
import streamlit as st
import random

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

prompt = st.text_input("صف الصورة (English):", value="A futuristic city")

if st.button("توليد فوري ✨"):
    if prompt:
        with st.spinner("جاري جلب الصورة..."):
            # توليد رقم عشوائي عشان الصورة تتغير كل مرة
            seed = random.randint(1, 100000)
            
            # تنظيف الوصف وتحويله لروابط بتفهمها المتصفحات
            clean_prompt = prompt.replace(" ", "%20")
            
            # رابط المحرك السريع جداً
            image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?seed={seed}&width=1024&height=1024&nologo=true"
            
            # عرض الصورة
            st.image(image_url, caption=f"النتيجة لـ: {prompt}", use_container_width=True)
            st.success("تم التوليد! اضغطي مرة أخرى لنتائج مختلفة.")
            st.balloons()
    else:
        st.warning("برجاء كتابة وصف")

st.markdown("---")
st.caption("Powered by Hadeer AI | 2025")
