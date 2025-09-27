import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import re

# Load BLIP model (only once)
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

st.title("📸 Instagram Caption & Hashtag Recommender")
st.write("Upload an image and get recommended captions + hashtags!")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.success("✅ Image uploaded successfully!")

    # Generate caption
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=30)

    caption = processor.decode(output[0], skip_special_tokens=True)
    st.subheader("👉 Caption Recommendation")
    st.write(caption)

    # Generate hashtags (simple keyword extraction)
    words = re.findall(r"\w+", caption.lower())
    hashtags = ["#" + w for w in words if len(w) > 3][:10]  # keep only meaningful words
    hashtags = list(set(hashtags))  # remove duplicates

    st.subheader("👉 Hashtag Recommendation")
    st.write(" ".join(hashtags) if hashtags else "No hashtags found 😅")
