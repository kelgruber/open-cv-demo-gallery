import streamlit as st
from pages.utils import *

# Set page config
apptitle = 'OpenCv Demo'
st.set_page_config(page_title=apptitle, page_icon=":camera:")

# App Title and Give User Instructions
st.title('OpenCV Demo')
st.markdown("""
 Select a demo from the left sidebar to see some example OpenCV projects.
""")
pages = st.navigation(
    [
        st.Page("app.py", title="Home"),
        st.Page("pages/edge_detect.py", title="Edge Detection"),
        st.Page("pages/morphological.py", title="Morphological Operations"),
    ]
)
pages.run()
# st.sidebar.success("Select a demo above.")

