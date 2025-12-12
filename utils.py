import cv2
import os
import sys
import streamlit as st

def hello():
    st.title("Hello")

@st.cache_data
def save_uploadedfile(filepath, uploaded_img):
    """
    Function saves the uploaded file to backend for processing. 

    Parameters:
        filepath (string): string containing the path to save the file at 
        uploaded_img (streamlit object) : object holding the image data
    Returns:
        image (numpy ndarray): array holding a grayscale image 
    """
    with open(filepath, "wb") as f:
        f.write(uploaded_img.getbuffer())

@st.cache_data
def get_filepath(uploaded_img):
    """
    Function gets the uploaded file path from the backend 

    Parameters:
        uploaded_img (streamlit object) : object holding the image data
    Returns:
        path (string): string holding filepath location
    """
    return os.path.join("./uploaded_images", uploaded_img.name)

@st.cache_data
def open_image(file):
    """
    Function checks if file exists and image can be read and is so returns the grayscale image. 
    If image cannot be read function displays error to user and terminates the program.

    Parameters:
        file (string): string containing the file to open and its path.  
    Returns:
        image (numpy ndarray): array holding the image 
    """
    # Check that needed files exist
    if not os.path.exists(file) :
        print(f"Error, input file {file} does not exist. Program terminated.")
        sys.exit(1)

    image = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    if image is None:
        print(f"Error, could not open {file}. Program terminated.")
    return image

