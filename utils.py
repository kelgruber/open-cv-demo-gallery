import cv2
import os
import streamlit as st

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

def display_resize(image, desired_width=None, desired_height=None):
    """
    Function resizes image using nearest neighbor interpolation to fit within desired shape 
    while preserving the aspect ratio.

    Parameters:
        image (numpy ndarray): array of values representing the image shape and values
        desired_width (int): max columns wide the displayed image should be
        desired_height (int): max rows tall the displayed image should be
    Returns:
        resized_image (numpy ndarray): image array resized to desired dimensions
    """
    current_height, current_width = image.shape[:2]
    aspect_ratio = current_width / current_height

    if desired_width is None:
        # receved only height calculate based on the desired width
        new_width = int(desired_height * aspect_ratio)
        resized_image = cv2.resize(image, (new_width, desired_height), interpolation=cv2.INTER_NEAREST)
    elif desired_height is None:
        # receved only width calculate height based on the desired width
        new_height = int(desired_width / aspect_ratio)
        resized_image = cv2.resize(image, (desired_width, new_height), interpolation=cv2.INTER_NEAREST)
    else:
        # recieved both width and height
        new_width = int(desired_height * aspect_ratio)

        # verify new image size is within bounds if needed resize using height
        if new_width > desired_width:
            new_height = int(desired_width / aspect_ratio)
            resized_image = cv2.resize(image, (desired_width, new_height), interpolation=cv2.INTER_NEAREST)
        else:
            resized_image = cv2.resize(image, (new_width, desired_height), interpolation=cv2.INTER_NEAREST)

    return resized_image