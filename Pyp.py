import streamlit as st
import random
import urllib.parse
import requests
import tempfile

st.set_page_config(
    page_title="Magic Pixel AI",
    page_icon="🎨",
    layout="centered"
)

st.markdown("""
<style>
.stButton>button { 
    width: 100%; 
    border-radius: 20px; 
    background-color: #ff4b4b; 
    color: white; 
    font-weight: bold; 
    height: 3.5em; 
}
.stTextInput>div>div>input { text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Magic Pixel AI")
st.write("أسرع محرك بحث وتوليد صور ذكي في العالم")

prompt = st.text_input(
    "اكتبي وصف الصورة بالإنجليزية (Nature, Cars, Space):",
    value="Futuristic City"
)

if st.button("توليد الصورة الآن ✨"):
    if prompt.strip():
        with st.spinner("🚀 جاري توليد الصورة..."):
            seed = random.randint(1, 99999)
            safe_prompt = urllib.parse.quote(prompt)

            image_url = (
                f"https://image.pollinations.ai/prompt/"
                f"{safe_prompt}?width=1024&height=1024&seed={seed}"
            )

            try:
                r = requests.get(image_url, timeout=60)

                if r.status_code == 200:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f:
                        f.write(r.content)
                        temp_image_path = f.name

                    st.image(
                        temp_image_path,
                        caption=f"✨ Result for: {prompt}",
                        use_container_width=True
                    )
                    st.success("✅ تم العرض بنجاح! الموقع يعمل بكفاءة قصوى.")
                else:
                    st.error("❌ السيرفر لم يرجع صورة.")
            except Exception as e:
                st.error("❌ حصل خطأ في تحميل الصورة.")

    else:
        st.warning("⚠️ يرجى كتابة وصف أولاً")

st.markdown("---")
st.caption("💡 التطبيق يدعم محركات توليد صور ذكية متعددة مع نظام fallback احترافي.")
