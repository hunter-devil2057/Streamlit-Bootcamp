import streamlit as st
from PIL import Image

image = Image.open("test.jpg")

st.image(
    image, 
    caption = "Caption: Nice Picture"
)