import streamlit as st
import re
import requests

WEBHOOK_URL = "https://webhook.site/3c451d2a-bcec-42c3-958a-bcaf4bf71306"

def is_valid_email(email):
    # Basic regex for email validation
    email_pttern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pttern, email) is not None

def contact_form():
    with st.form("Contact Form"):
        name = st.text_input("First     Name")
        email = st.text_input("Email    Address")
        message = st.text_area("Your    Message")
        submit_button = st. form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.", icon="📧")
                st.stop()
            
            if not name:
                st.error("Please provide your name.", icon="☺")
                st.stop()
            
            if not email:
                st.error("Please provide your email address.", icon="📩")
                st.stop()
            
            if not is_valid_email(email):
                st.error("Please provide a valid email address.", icon="📪")
                st.stop() 
                
            if not message:
                st.error("Please provide a message.", icon="💬")
                st.stop()
                
            # Prepare the data payload and send it to the specified webhook url
            
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)
            
            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉", icon="🚀")
                
            else:
                st.error("There was an error sending your message.", icon="😨")                             