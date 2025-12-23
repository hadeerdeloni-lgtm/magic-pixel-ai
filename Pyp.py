
import streamlit as st
import requests
import io
from PIL import Image

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")
st.write("حول كلماتك إلى لوحات فنية مذهلة باستخدام الذكاء الاصطناعي")

# استدعاء الـ Token من خزنة الأسرار (Secrets) بشكل آمن
if "hf_token" in st.secrets:
    API_TOKEN = st.secrets["hf_token"]
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        return requests.post(API_URL, headers=headers, json=payload)

    prompt = st.text_input("صف الصورة التي تتخيلها (بالإنجليزي):", placeholder="e.g. A magical cat in space")

    if st.button("توليد الصورة ✨"):
        if prompt:
            with st.spinner("الذكاء الاصطناعي يرسم الآن..."):
                response = query({"inputs": prompt})
                if response.status_code == 200:
                    try:
                        image = Image.open(io.BytesIO(response.content))
                        st.image(image, caption="تم التوليد بنجاح!", use_container_width=True)
                    except:
                        st.error("السيرفر أرسل بيانات غير صالحة، حاول مرة أخرى.")
                elif response.status_code == 503:
                    st.warning("السيرفر يستعد، انتظر 20 ثانية وحاول مجدداً.")
                else:
                    st.error(f"خطأ: {response.status_code}. تأكد من صحة الـ Token في الإعدادات.")
        else:
            st.warning("من فضلك اكتب وصفاً أولاً!")
else:
    st.error("برجاء وضع الـ Token في إعدادات Secrets بالموقع أولاً.")

st.markdown("---")
st.caption("Powered by Hadeer's AI Engine | 2025")
