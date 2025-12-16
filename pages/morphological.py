from pages.utils import *

# Set page config
st.set_page_config(page_title="Morphological Operations Demo", page_icon=":camera:")

st.title('Morphological Operations Demo')
st.markdown("""
 Choose an Morphological Operator and Operation from the sidebar.
""")

# Choose Morphological Operations
option_list = ["Erosion", "Dilation", "Opening", "Closing", "Hit-or-Miss Transform", "Skeletonization", "Pruning"]
operation = st.sidebar.selectbox('Morphological Operations', option_list)