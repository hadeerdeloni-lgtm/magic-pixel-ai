import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

# استدعاء المفتاح من خزنة الإعدادات السرية
if "huggingface_token" in st.secrets:
    API_TOKEN = st.secrets["huggingface_token"]
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        return requests.post(API_URL, headers=headers, json=payload)

    prompt = st.text_input("صف الصورة بالإنجليزية:", "A fantasy world")

    if st.button("توليد الصورة ✨"):
        with st.spinner("جاري الرسم..."):
            response = query({"inputs": prompt})
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content))
                st.image(image, use_container_width=True)
                st.success("تم التوليد بنجاح!")
            else:
                st.error("السيرفر مشغول حالياً، يرجى المحاولة بعد قليل.")
else:
    st.error("لم يتم ضبط مفتاح التشغيل في إعدادات الموقع بعد.")
