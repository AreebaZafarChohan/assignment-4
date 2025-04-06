import streamlit as st
import os

# Assuming the absolute path to your image
image_path = os.path.join(os.getcwd(), "assets", "logo.png")
st.sidebar.image(image_path, width=150)

#  PAGE SETUP

about_page = st.Page(
    page = "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True 
)

project_1_page = st.Page(
    page = "views/qr_code_generator.py",
    title="QR Generator & Scanner",
    icon=":material/qr_code_scanner:",
)

project_2_page = st.Page(
    page = "views/chatbot.py",
    title="Chat bot",
    icon=":material/smart_toy:",
)



# NAVIGATION SETUP [ WITHOUT SECTIONS ]

#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# NAVIGATION SETUP [ WITHOUT SECTIONS ]

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# SHARED ON ALL PAGES
st.sidebar.text("Made with ❤ by Areeba Zafar")

# RUN NAVIGATION
pg.run()