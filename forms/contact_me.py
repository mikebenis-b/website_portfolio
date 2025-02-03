import streamlit as st
import re
import requests

webhooks_url=st.secrets["webhooks_url"]
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    return re.match(regex, email) is not None
@st.dialog("contact_me")
def contact_me():
    with st.form("contact_form"):
        name=st.text_input("enter your name")
        email=st.text_input("enter your email")
        cont_no=st.text_input("enter your contact number")
        message=st.text_input("your message")
        submit=st.form_submit_button("Submit")

        if submit:
            if not webhooks_url:
                st.error("Email setup is not done✉")
                st.stop()
            if not name:
                st.error("Fill the Name feild")
                st.stop()
            if not email:
                st.error("Fill the Email feild")
                st.stop()
            if not is_valid_email(email):
                st.error("Enter a propper Email")
            if not cont_no:
                st.error("Fill the contact Number Field")
                st.stop()
            if not message:
                st.error("give any message to the owner")
                st.stop()

            data={"Name":name,"Email":email,"Contact_number":cont_no,"Message":message}
            response=requests.post(webhooks_url,json=data)
            if response.status_code== 200:
                st.success("the message has been sent",icon="✉")
            else:
                st.error("There was an error in sending your message")

    return
