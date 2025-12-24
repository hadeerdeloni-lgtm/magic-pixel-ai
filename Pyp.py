
import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

# نداء للخزنة
if "hf_token" in st.secrets:
    headers = {"Authorization": f"Bearer {st.secrets['hf_token']}"}
    
    # أسرع موديل خفيف في العالم للنتائج الفورية
    API_URL = "https://api-inference.huggingface.co/models/segmind/SSD-1B"

    prompt = st.text_input("صف الصورة (English):", value="A cute cat")

    if st.button("رسم بضغطة واحدة ✨"):
        with st.spinner("جاري الرسم فوراً..."):
            try:
                # محاولة طلب الصورة
                res = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=20)
                
                if res.status_code == 200:
                    img = Image.open(io.BytesIO(res.content))
                    st.image(img, caption="أخيراً! نجحت التجربة")
                    st.balloons()
                elif res.status_code == 503:
                    st.warning("السيرفر يفتح عيونه.. انتظر 5 ثواني واضغط مرة أخيرة")
                else:
                    st.error("جربي الضغط مرة أخرى الآن، السيرفر استيقظ")
            except:
                st.error("مشكلة في الشبكة، جربي مرة ثانية")
else:
    st.error("المفتاح غير موجود في Secrets")
