import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

st.title("📸 Instagram Caption & Hashtag Recommender")
st.write("Upload an image and get recommended captions + hashtags!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Generate caption
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    st.success("✅ Caption generated!")
    st.write("**Caption:**", caption)
    
    # Generate hashtags from caption (simple approach: split words and add #)
    hashtags = " ".join([f"#{word}" for word in caption.split()])
    st.write("**Hashtags:**", hashtags)
