import streamlit as st
import requests
from forms.contact_me import contact_me
st.set_page_config(page_title="about_me", page_icon=":material/account_circle:")
col1,col2=st.columns(2,gap="large",vertical_alignment="center")
with col1:
    st.image(r"assets\unknwn_user_pic.jpg",use_column_width=True)
with col2:
    st.title("B.Mikebenis")
    st.write("I am a passionate data science student having good knowledge in python and also a avid learner")
    st.markdown('<center>',unsafe_allow_html=True)
    if st.button("✉Contact me"):
        contact_me()
    st.markdown('</center>', unsafe_allow_html=True)
st.markdown("""
    <style>
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        font-size: 18px;
        margin: 5px 0;
    }
    li::before {
        content: "";
        margin-right: 8px;
    }
    </style>
    <ul>
        <li><strong>Name:</strong> B. Mike Benis</li>
        <li><strong>Age:</strong> 19</li>
        <li><strong>Role:</strong> Data Engineer</li>
        <li><strong>
    </ul>
    
    """, unsafe_allow_html=True)