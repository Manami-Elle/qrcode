import streamlit as st
import qrcode
from PIL import Image
import numpy as np

st.title("ORコード自動作成アプリ")

url=st.text_input ("QRコードを生成したいURL:")

if st.button("QRコード生成"):
    _img=qrcode.make(url)
    _img.save("qrcode.png")
    img=Image.open("qrcode.png")
    st.image(img)