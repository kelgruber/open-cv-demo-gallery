from pages.utils import *

about_page = st.Page("pages/about.py", title='About')
edge_page = st.Page("pages/edge_detect.py", title="Edge Detection")
morph_page = st.Page("pages/morphological.py", title="Morphological Operations")
segment_page = st.Page("pages/segment.py", title="Image Segmentation")

pages = st.navigation([about_page, edge_page, morph_page, segment_page])

pages.run()



