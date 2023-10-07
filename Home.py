import streamlit as st
from PIL import Image
from pathlib import Path

image_dir = Path('images')

st.set_page_config(page_title='Immersed in the Sounds of SPace')

st.title("Immersed in the Sounds of Space")

#insert image

image = Image.open(image_dir / 'poster.jpeg')
st.image(image, caption='Cosmic Harmony', use_column_width=True)

# 