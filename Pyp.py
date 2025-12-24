
import streamlit as st

st.set_page_config(page_title="Magic Pixel AI", page_icon="🎨")
st.title("🎨 Magic Pixel AI")

# واجهة بسيطة وسريعة
prompt = st.text_input("صف الصورة (English):", value="A futuristic city")

if st.button("توليد فوري ✨"):
    if prompt:
        with st.spinner("جاري جلب الصورة..."):
            # تحويل الوصف لرابط صورة مباشر سريع جداً
            # الطريقة دي بتضمن إن الصورة تظهر بضغطة واحدة مهما كان السيرفر بطيء
            formatted_prompt = prompt.replace(" ", "-")
            image_url = f"https://pollinations.ai/p/{formatted_prompt}?width=1024&height=1024&seed=42&model=flux"
            
            st.image(image_url, caption="تم التوليد بنجاح!", use_container_width=True)
            st.success("تمت العملية! يمكنك حفظ الصورة بالضغط المطول عليها.")
            st.balloons()
    else:
        st.warning("برجاء كتابة وصف")

st.markdown("---")
st.caption("Powered by Hadeer AI | 2025")
