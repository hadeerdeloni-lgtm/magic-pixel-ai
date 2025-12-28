import streamlit as st
from huggingface_hub import InferenceClient

st.title("Magic Pixel AI")

client = InferenceClient(
    model="stabilityai/stable-diffusion-xl-base-1.0",
    token=st.secrets["HF_TOKEN"]
)

prompt = st.text_input("Describe your image:")

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image = client.text_to_image(prompt)
        st.image(image)
