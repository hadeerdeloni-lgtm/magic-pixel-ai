
import streamlit as st
import requests
import io
import time
from PIL import Image

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

if "hf_token" in st.secrets:
    headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
    # موديل سريع جداً ومخصص للموبايل
    API_URL = "https://api-inference.huggingface.co/models/stablediffusionapi/stable-diffusion-v2-1"

    prompt = st.text_input("وصف الصورة (English):", value="A majestic cat")

    if st.button("رسم ✨"):
        with st.spinner("جاري إيقاظ السيرفر.. انتظر قليلاً"):
            # محاولة الطلب أكثر من مرة لو السيرفر مشغول
            for i in range(3):
                res = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                if res.status_code == 200:
                    img = Image.open(io.BytesIO(res.content))
                    st.image(img, caption="مبارك! أول صورة من صنع موقعك")
                    st.balloons()
                    break
                elif res.status_code == 503:
                    time.sleep(10) # انتظر 10 ثواني لو السيرفر بيحمل
                else:
                    continue
            if res.status_code != 200:
                st.warning("السيرفر يستعد.. اضغط 'رسم' مرة أخرى الآن")
else:
    st.error("المفتاح غير موجود في الخزنة")
