
import streamlit as st
import requests
import io
from PIL import Image

st.title("🎨 Magic Pixel AI")

# نداء للخزنة السرية
if "hf_token" in st.secrets:
    headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
    
    # غيرنا الرابط لنسخة أسرع وأخف (Stable Diffusion v2.1)
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"

    prompt = st.text_input("وصف الصورة (بالإنجليزي):", value="A beautiful cat")

    if st.button("رسم ✨"):
        with st.spinner("جاري الرسم..."):
            res = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            if res.status_code == 200:
                img = Image.open(io.BytesIO(res.content))
                st.image(img, caption="تم التوليد بنجاح!")
            else:
                st.error("السيرفر مشغول، حاول مرة أخرى خلال ثوانٍ.")
else:
    st.error("المفتاح ناقص في الإعدادات")
