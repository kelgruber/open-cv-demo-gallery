from pages.utils import *

# Set page config
st.set_page_config(page_title="Edge Detection Demo", page_icon=":camera:")

st.title('Edge Detection Demo')
st.markdown("""
 Choose an Edge Detection algorithm from the sidebar.
""")

# Choose Edge Detection Algorithm
option_list = ["Canny Edge Detection", "Laplacian Operator", "Sobel Operator", "Roberts Cross Operator", "Prewitt Operator"]
detect_method = st.sidebar.selectbox('Edge Detection Algorithms', option_list)

# Get Image from the user
file_types = ["jpg", "jpeg", "png", "tif"]
uploaded_img = st.sidebar.file_uploader("Upload an Image", type=file_types, accept_multiple_files=False, key=None, on_change=None, label_visibility="visible")

if uploaded_img is not None:
    # Upload and display the image
    filepath = get_filepath(uploaded_img)
    save_uploadedfile(filepath, uploaded_img) 
    img = open_image(filepath)
    processed_img = img.copy()
    
    st.sidebar.write("Original Image:")
    st.sidebar.image(img, width=350, channels="BGR")

    st.image(processed_img, channels="BGR")