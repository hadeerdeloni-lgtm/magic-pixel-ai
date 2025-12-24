
import streamlit as st
import requests
import io
from PIL import Image

st.title("🎨 Magic Pixel AI")

# نداء للخزنة السرية
if "hf_token" in st.secrets:
    headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

    prompt = st.text_input("وصف الصورة (بالإنجليزي):")

    if st.button("رسم ✨"):
        with st.spinner("انتظر ثواني..."):
            res = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            if res.status_code == 200:
                img = Image.open(io.BytesIO(res.content))
                st.image(img)
            else:
                st.error("السيرفر يحمل.. جربي كمان دقيقة")
else:
    st.error("المفتاح ناقص في الإعدادات")
