
import streamlit as st
import requests
import io
import time
from PIL import Image

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

if "hf_token" in st.secrets:
    headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
    # سيرفر Lightning - سريع جداً ولا يحتاج تسخين طويل
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

    prompt = st.text_input("صف الصورة (English):", value="A cute cat in a hat")

    if st.button("توليد فوري ✨"):
        with st.spinner("جاري الرسم..."):
            # محاولة الإلحاح داخلياً عشان تطلع من ضغطة واحدة
            for i in range(3):
                res = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                if res.status_code == 200:
                    img = Image.open(io.BytesIO(res.content))
                    st.image(img, caption="مبروك! اشتغل بضغطة واحدة")
                    st.balloons()
                    break
                else:
                    time.sleep(5) # استراحة قصيرة للمحاولة التالية تلقائياً
            
            if res.status_code != 200:
                st.error("السيرفر يرفض الاستجابة حالياً، اضغطي مرة أخرى بعد ثوانٍ")
else:
    st.error("المفتاح غير موجود")
