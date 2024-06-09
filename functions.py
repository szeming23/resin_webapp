import streamlit as st

img_dir = "resin_imgs/"

def add_img(filename, caption):
    st.image(img_dir+filename, caption=caption, width=200)
