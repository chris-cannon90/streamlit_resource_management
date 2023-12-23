import streamlit as st
import base64
import random

####################################################################################################
# formatting functions

### EVERYTHING HERE NEEDS FIXING
####################################################################################################
def include_floating_logo():
    # floating logo
    path_string = "images/das42_logo-1.webp"

    with open(path_string, "rb") as f:
        image_data = f.read()

    base64_img = base64.b64encode(image_data).decode("utf-8")

    html = f"""
    <div style="position: fixed; bottom: 45px; right: 0; z-index: 9999">
        <img style="height: 25px; width: 100px; margin: 10px;" src="data:image/webp;base64,{base64_img}"></img>
    </div>
    """

    # display the HTML using st.markdown
    st.markdown(html, unsafe_allow_html=True)

def thicker_divider_formatting():
    st.markdown("""
    <style>
    .horizontal-line {
    border-top: thick solid grey;
    width: 100%;
    margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

def insert_thicker_divider():
    st.markdown('<div class="horizontal-line"></div>', unsafe_allow_html=True)