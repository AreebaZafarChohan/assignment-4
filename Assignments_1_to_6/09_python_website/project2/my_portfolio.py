import streamlit as st

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
st.logo("https://i.pinimg.com/736x/ca/54/d6/ca54d6ff28774102b7c6cb98aa38e0ea.jpg")
st.sidebar.text("Made with ❤ by Areeba Zafar")

# RUN NAVIGATION
pg.run()