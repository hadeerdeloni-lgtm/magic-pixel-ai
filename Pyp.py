

import streamlit as st
import requests
import io
import time
from PIL import Image

# إعدادات واجهة الموقع بشكل احترافي
st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨", layout="centered")

st.title("🎨 Magic Pixel AI")
st.write("اكتب وصف الصورة بالإنجليزية وسيقوم الذكاء الاصطناعي برسمها فوراً!")

# بيانات المحرك والـ Token الخاص بكِ (تم وضعه مباشرة)
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

# واجهة المستخدم
prompt = st.text_input("أدخل وصف الصورة:", placeholder="e.g. A beautiful sunset over a futuristic city")

if st.button("توليد الصورة ✨"):
    if prompt:
        with st.spinner("جاري الرسم.. انتظر قليلاً حتى يستيقظ السيرفر..."):
            attempts = 0
            success = False
            while attempts < 5 and not success:
                response = query({"inputs": prompt})
                
                # إذا نجح في توليد الصورة
                if response.status_code == 200 and b"estimated_time" not in response.content:
                    try:
                        image = Image.open(io.BytesIO(response.content))
                        st.image(image, caption="تم التوليد بنجاح!", use_container_width=True)
                        
                        # زر التحميل
                        buf = io.BytesIO()
                        image.save(buf, format="PNG")
                        st.download_button(label="📥 تحميل الصورة", data=buf.getvalue(), file_name="ai_image.png", mime="image/png")
                        success = True
                    except:
                        st.error("حدث خطأ في عرض الصورة، حاول مرة أخرى.")
                        break
                
                # إذا كان الموديل لسه بيحمل (Loading)
                elif b"estimated_time" in response.content:
                    st.info("الذكاء الاصطناعي يستعد.. سأحاول مجدداً خلال 10 ثوانٍ...")
                    time.sleep(10)
                    attempts += 1
                else:
                    st.error(f"خطأ من السيرفر: {response.status_code}. تأكد من الـ Token.")
                    break
    else:
        st.warning("من فضلك اكتب وصفاً أولاً!")

st.markdown("---")
st.caption("Powered by Hadeer AI Engine")
