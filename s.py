import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os


DEMO_IMAGE="vwo-social-share.png"

img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))

st.write(image.shape)


st.image(
    image, caption=f"Processed image", use_column_width=True,
)


st.write(cv2.imwrite("try/image.png",image))
