from utils import *

# Get Image from the user
file_types = ["jpg", "jpeg", "png", "tif"]
uploaded_img = st.sidebar.file_uploader("Upload an Image", type=file_types, accept_multiple_files=False, key=None, on_change=None, label_visibility="visible")

pages = st.navigation(
    [
        st.Page("app.py", title="Home"),
        st.Page("pages/edge_detect.py", title="Edge Detection"),
        st.Page("pages/morphological.py", title="Morphological Operations"),
    ]
)
pages.run()
# st.sidebar.success("Select a demo above.")


if uploaded_img is not None:
    # Upload and display the image
    filepath = get_filepath(uploaded_img)
    save_uploadedfile(filepath, uploaded_img) 
    img = open_image(filepath)
    processed_img = img.copy()
    
    st.sidebar.write("Original Image:")
    st.sidebar.image(img, width=350, channels="BGR")

    st.image(processed_img, channels="BGR")