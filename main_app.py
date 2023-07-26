import streamlit as st
from PIL import Image

st.title('koyoアプリ')
st.caption('これはkoyoのテストアプリです')

image = Image.open('./data/koyoデフォルメ1.png')
st.image(image, width=200)