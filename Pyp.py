
import streamlit as st
import requests
import io
import time
from PIL import Image

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

if "hf_token" in st.secrets:
    headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
    # اخترت لكِ أسرع سيرفر حالياً لا يحتاج انتظار طويل
    API_URL = "https://api-inference.huggingface.co/models/dataautogpt3/FLUX.1-dev-gguf"

    prompt = st.text_input("صف الصورة (English):", value="A cute kitten")

    if st.button("رسم بنقرة واحدة ✨"):
        with st.spinner("جاري الرسم.. جاري إيقاظ السيرفر تلقائياً..."):
            # محاولات تلقائية عشان متضطريش تضغطي كذا مرة
            success = False
            for i in range(5): 
                try:
                    res = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=30)
                    if res.status_code == 200:
                        img = Image.open(io.BytesIO(res.content))
                        st.image(img, caption="تم التوليد بنجاح!")
                        st.balloons()
                        success = True
                        break
                    else:
                        time.sleep(2) # انتظر ثانيتين وجرب تاني لوحده
                except:
                    continue
            
            if not success:
                st.error("السيرفر ثقيل جداً الآن، جربي الضغط مرة أخرى بعد ثوانٍ.")
else:
    st.error("تأكدي من وجود المفتاح في الخزنة")
