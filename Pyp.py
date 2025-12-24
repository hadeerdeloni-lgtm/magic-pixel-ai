
import streamlit as st
import random

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

prompt = st.text_input("صف الصورة (English):", value="A futuristic city")

# ده الجزء اللي هيخلي الصورة تظهر أسرع
if st.button("توليد فوري ✨"):
    if prompt:
        placeholder = st.empty() # مكان محجوز للصورة
        with st.spinner("جاري الرسم..."):
            seed = random.randint(1, 999999)
            clean_prompt = prompt.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?seed={seed}&width=1024&height=1024&nologo=true"
            
            # عرض الصورة فوراً في المكان المحجوز لها
            placeholder.image(image_url, caption=f"النتيجة: {prompt}")
            st.balloons()
            st.success("تمت العملية! الصورة بالأعلى 👆")
    else:
        st.warning("برجاء كتابة وصف")

st.markdown("---")
st.caption("Powered by Hadeer AI | 2025")
