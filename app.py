import streamlit as st
import numpy as np


# Set page config
apptitle = 'OpenCv Demo'
st.set_page_config(page_title=apptitle, page_icon=":thread:")

# App Title and Give User Instructions
st.title('OpenCV Demo')
st.markdown("""
 Use the menu at left to select which algorithms you want to use
""")

# Get Image from the user
file_types = ["jpg", "jpeg", "png", "tif"]
uploaded_img = st.sidebar.file_uploader("Upload an Image", type=file_types, accept_multiple_files=False, key=None, on_change=None, label_visibility="visible")

# Process for Pattern Preview
if uploaded_img is not None:
    # Upload and display the image
    filepath = get_filepath(uploaded_img)
    save_uploadedfile(filepath, uploaded_img) 
    img = open_image(filepath)
    processed_img = img.copy()
    
    st.sidebar.write("Original Image:")
    st.sidebar.image(img, width=350, channels="BGR")

    # Checkbox to preserve aspect
    preserve_aspect = st.sidebar.checkbox("Preserve Aspect Ratio", value=False, key=None, on_change=None, disabled=False, label_visibility="visible")

    # Get current image information
    pixel_height, pixel_width = img.shape[:2]
    aspect_ratio = pixel_width / pixel_height
    
    new_height = pixel_height
    new_width = pixel_width
