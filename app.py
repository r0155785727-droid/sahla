import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

img = Image.open("logo.png")

st.set_page_config(
    page_title="رفيق الطالب الذكي",
    page_icon=img,
    layout="wide"
)

st.markdown("""
    <style>
        .block-container { padding: 0rem; max-width: 100%; }
        header, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=900, scrolling=True)
