import streamlit as st
import requests
import io
from PIL import Image

# إعدادات واجهة الموقع
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 AI Image Generator")
st.write("اكتب وصف الصورة التي تتخيلها وسيقوم الذكاء الاصطناعي برسمها لك!")

# هنا نضع رابط المحرك من Hugging Face (مجاني)
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
# ملاحظة: ستحتاجين لتبديل "YOUR_TOKEN_HERE" بمفتاح الـ API الخاص بك لاحقاً
headers = {"Authorization": "Bearer YOUR_TOKEN_HERE"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

prompt = st.text_input("أدخل وصف الصورة (بالإنجليزية):", "A futuristic city in mars")

if st.button("توليد الصورة"):
    with st.spinner("انتظر قليلاً... الذكاء الاصطناعي يرسم الآن"):
        image_bytes = query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="الصورة التي تم توليدها")
        
        # زر التحميل
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.download_button(label="تحميل الصورة", data=buf.getvalue(), file_name="ai_image.png", mime="image/png")
