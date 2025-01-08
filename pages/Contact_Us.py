import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


st.header("Contact Us")

with st.form(key="email_form"):
    User_email = st.text_input("Your email address")
    message = st.text_area("your message")
    button = st.form_submit_button("Submit")
    if button:
        # Email details
        your_email = "ahmadtawil.se@outlook.com"
        your_password = "AhmadTawilSe?!123"
        subject = "New Message from Contact Form"

        # Create email content
        email_message = MIMEMultipart()
        email_message["From"] = User_email
        email_message["To"] = your_email  # Send to yourself
        email_message["Subject"] = subject
        email_body = f"Message from: {User_email}\n\n{message}"
        email_message.attach(MIMEText(email_body, "plain"))

        try:
            # Connect to Outlook SMTP server and send the email
            with smtplib.SMTP("smtp.office365.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(your_email, your_password)
                server.send_message(email_message)
                st.success("Your message has been sent successfully!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
