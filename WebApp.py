import streamlit as st

ans = st.selectbox('Login/Signup', ['Login', 'Signup'])
if ans == 'Login':
    email = st.text_input('Email Id')
    phone_no = st.text_input('Your Phone No (10-digit)')

