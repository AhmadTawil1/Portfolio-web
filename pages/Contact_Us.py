import streamlit as st


st.header("Contact Us")

with st.form(key="email_form"):
    User_email = st.text_input("Your email address")
    message = st.text_area("your message")
    button = st.form_submit_button("Submit")
    if button:
        message = message + User_email
