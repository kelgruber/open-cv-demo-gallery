from pages.utils import *

# Set page config
st.set_page_config(page_title="Image Segmentation", page_icon=":camera:")

# App Title and Give User Instructions
st.title("Image Segmentation")
st.markdown("""
 Choose an Image Segmentation Algorithm from the sidebar.
""")

# Choose Segmentation Algorithm
option_list = ["K-Means Clustering", "SLIC Superpixels"]
segment_method = st.sidebar.selectbox('Segmentation Algorithms', option_list)