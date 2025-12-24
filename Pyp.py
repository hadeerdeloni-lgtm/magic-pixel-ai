
import streamlit as st
import urllib.parse

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

prompt = st.text_input("صف الصورة (English):", value="A futuristic city")

if st.button("توليد فوري ✨"):
    if prompt:
        with st.spinner("جاري جلب الصورة..."):
            # تعديل طريقة معالجة النص لضمان عمل الرابط
            safe_prompt = urllib.parse.quote(prompt)
            image_url = f"https://pollinations.ai/p/{safe_prompt}?width=1024&height=1024&nologo=true"
            
            # عرض الصورة باستخدام الرابط المباشر
            st.image(image_url, caption="تم التوليد بنجاح!", use_container_width=True)
            st.success("تمت العملية بنجاح!")
            st.balloons()
    else:
        st.warning("برجاء كتابة وصف")
