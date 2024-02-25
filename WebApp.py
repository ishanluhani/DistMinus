from PIL import Image
import streamlit as st
import json


minute_data = None
og_minutes = None
st.set_page_config(layout="wide")
data = json.load(open('internal_data/data.json'))
img = Image.open(data['profile pic'])

with open('style.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

st.write('<p class="title">DistMinus Tracker</p><hr class="title_hr">', unsafe_allow_html=True)

profile_pic, profile_hi = st.columns([4, 5])

with profile_pic:
    st.image(img, width=200)
with profile_hi:
    st.write(f'<p class="hi">Hello</p><p class="hi purple">{data["name"]}</p>', unsafe_allow_html=True)

st.write('<hr class="sub_hr">', unsafe_allow_html=True)
st.write('<p class="hi2">Focus Mode</p>', unsafe_allow_html=True)


toggle = st.toggle('Start Blocking')

if toggle:
    data['focused_currently'] = 1
    with open("internal_data/data.json", "w") as f:
        json.dump(data, f, indent=4)
else:
    data['focused_currently'] = 0
    with open("internal_data/data.json", "w") as f:
        json.dump(data, f, indent=4)