
import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

if "hf_token" in st.secrets:
    headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
    
    # رابط المحرك الجديد (فائق السرعة)
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/sdxl-lightning"

    prompt = st.text_input("وصف الصورة (English):", value="A cute kitten")

    if st.button("رسم ✨"):
        with st.spinner("جاري الرسم بسرعة البرق..."):
            res = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            if res.status_code == 200:
                img = Image.open(io.BytesIO(res.content))
                st.image(img, caption="أخيراً! تم التوليد بنجاح")
                st.balloons()
            else:
                st.warning("السيرفر يجهز الصورة، اضغطي رسم مرة أخرى")
else:
    st.error("تأكدي من وجود hf_token في Secrets")
