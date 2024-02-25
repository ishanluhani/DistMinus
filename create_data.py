import streamlit as st
import json
from PIL import Image

with st.form('fsv'):
    parent_email_id = st.text_input('Parent Email Id')
    parent_phone_no = st.text_input('Parent Phone No')
    kid_name = st.text_input('Kid Name')
    file = st.file_uploader('Choose an image file')

    ans_json = {
        "profile pic": 'internal_data/photo.png',
        "name": kid_name,
        "parent email id": parent_email_id,
        "parent phone no": parent_phone_no,
        "focused_currently": 0
    }
    if st.form_submit_button('Submit'):
        Image.open(file).save('internal_data/photo.png')
        with open('internal_data/data.json', 'w') as f:
            json.dump(ans_json, f, indent=4)
