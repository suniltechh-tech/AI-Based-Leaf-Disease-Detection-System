import streamlit as st
import numpy as np
from PIL import Image
import os

# Page Configuration
st.set_page_config(
    page_title="Leaf Disease Detection System",
    page_icon="🌿",
    layout="centered"
)

# App Title & Description
st.title("🌿 Leaf Disease Detection System")
st.markdown(
    """
    This application detects whether a plant leaf is **Healthy** or **Diseased**
    using image analysis techniques.  
    It demonstrates how **Artificial Intelligence** can support **smart agriculture**.
    """
)

st.divider()

# Sidebar Information
st.sidebar.header("📌 About Project")
st.sidebar.write(
    """
    - Domain: Agriculture + AI  
    - Type: Image Classification  
    - Approach: Deep Learning (CNN - extendable)  
    - Interface: Streamlit Web App
    """
)

st.sidebar.header("⚙️ Instructions")
st.sidebar.write(
    """
    1. Upload a clear leaf image  
    2. Click **Predict Disease**  
    3. View prediction result  
    """
)

# Image Upload Section
st.subheader("📤 Upload Leaf Image")

uploaded_image = st.file_uploader(
    "Choose a leaf image (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

# Image Preprocessing Function
def preprocess_image(image: Image.Image):
    """
    Preprocess the image before prediction.
    Steps:
    - Resize image
    - Convert to array
    - Normalize pixel values
    """
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Dummy Prediction Function (Replace with CNN later)
def predict_leaf_disease(image_array):
    """
    Dummy prediction logic.
    This simulates a trained CNN model.
    """
    prediction = np.random.rand()

    if prediction > 0.5:
        return "Healthy Leaf 🌱", prediction
    else:
        return "Diseased Leaf 🍂", prediction

# Display Uploaded Image
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Leaf Image", use_container_width=True)

    st.info("Image uploaded successfully. Ready for prediction.")

    # Prediction Button
    if st.button("🔍 Predict Disease"):
        with st.spinner("Analyzing leaf image..."):
            processed_image = preprocess_image(image)
            result, confidence = predict_leaf_disease(processed_image)

        st.success("Prediction Completed")

        # Display Result
        st.subheader("📊 Prediction Result")
        st.write(f"**Result:** {result}")
        st.write(f"**Confidence Score:** {confidence:.2f}")

        if "Healthy" in result:
            st.success("The leaf appears to be healthy.")
        else:
            st.warning("The leaf may be affected by disease.")

# Additional Information Section
st.divider()
st.subheader("ℹ️ Project Notes")

st.write(
    """
    - This version demonstrates the **complete application flow**
    - The prediction logic can be replaced with a trained **CNN model**
    - Suitable for academic projects and portfolio demonstrations
    """
)

# Footer
st.divider()
st.markdown(
    """
    **Developed by:** Sunil Kumar  
    **Project Type:** AI / Machine Learning  
    """
)
