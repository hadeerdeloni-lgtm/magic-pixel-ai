import streamlit as st
import random
import urllib.parse
import requests
from io import BytesIO
from PIL import Image

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Magic Pixel AI", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        background-color: #ff4b4b; 
        color: white; 
        font-weight: bold; 
        height: 3.5em; 
        border: none;
    }
    .stTextInput>div>div>input { text-align: center; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("النسخة الاحترافية - توليد صور فائقة الجودة بتقنية Buffer")

# 2. المدخلات
prompt = st.text_input("اكتبي وصف الصورة بالإنجليزية:", value="A futuristic city with neon lights")

if st.button("توليد الصورة الآن ✨"):
    if prompt:
        with st.spinner("🚀 جاري معالجة الصورة في الذاكرة... انتظر ثوانٍ"):
            seed = random.randint(1, 999999)
            safe_prompt = urllib.parse.quote(prompt)
            # استخدام موديل Flux القوي والمستقر
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}&width=1024&height=1024&model=flux&nologo=true"
            
            try:
                # التحميل الفعلي لبيانات الصورة من السيرفر
                response = requests.get(image_url, timeout=25)
                
                if response.status_code == 200:
                    # تحويل البيانات إلى صورة حقيقية باستخدام Pillow
                    img = Image.open(BytesIO(response.content))
                    
                    # عرض الصورة من الذاكرة (وليس كرابط)
                    st.image(img, caption=f"✨ Result for: {prompt}", use_container_width=True)
                    st.balloons()
                    st.success("✅ تم توليد وعرض الصورة بنجاح باهر!")
                else:
                    st.error("⚠️ السيرفر مشغول جداً حالياً، يرجى المحاولة مرة أخرى بعد ثوانٍ.")
            except Exception as e:
                st.error("❌ عذراً، حدث خطأ في الاتصال. تأكدي من جودة الإنترنت وحاولي مجدداً.")
    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 تقنية العرض: Image Memory Buffer لضمان أقصى درجات الاستقرار للمشترين.")
