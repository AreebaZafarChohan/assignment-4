import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
    

# HERO SECTION

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("https://i.pinimg.com/736x/b0/0a/17/b00a173c36fcd31f028d311a2cc8cd3b.jpg", width=230)
    
with col2:
   # st.title("", anchor=False)
    st.markdown("<h2 style='text-align: left; text-decoration: underline; color: cyan; font-weight: bold; font-size: 45px '>Areeba Zafar</h2>", unsafe_allow_html=True)
    st.write(
        "I’m a passionate web developer and teacher, focused on creating responsive, user-friendly websites. I’m also excited to dive into AI, and I love sharing my knowledge with others to help them grow in web development and beyond."
    )
    # Custom CSS for button border
    st.markdown("""
    <style>
    div.stButton > button {
        border: 2px solid cyan;
        color: white;
        background-color: black;
        padding: 0.5em 1em;
        border-radius: 5px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        border-color: white;
        color: cyan;
    }
    </style>
    """, unsafe_allow_html=True)
    if st.button("✉ Contact Me"):
        show_contact_form() 
        
# EXPERIENCE & QUALIFICATIONS
st.write("\n")
st.markdown("<h2 style='text-align: left; text-decoration: underline; color: cyan; '>Experience & Qualifications</h2>", unsafe_allow_html=True)

st.write(
    """
- Matriculation (2020): Completed in Science with an A grade (71%) from Little Citizen Primary and Secondary School.

- Intermediate (2022): Completed in Commerce with an A+ grade (84%) from Government College of Women, Korangi No. 4.

- Current Studies (Since March 2024): Pursuing Generative AI with IT expertise and web development at Governor House.

- Leadership Experience: As a Leader Student at Governor House, where I guided students in TypeScript, Next.js, HTML, and CSS.

- Currently mentoring students in Python.

- Teaching Experience: 4 years of experience as a school teacher.
    """
)           

# SKILLS

st.write("\n")

st.markdown("<h2 style='text-align: left; text-decoration: underline; color: cyan; '>Skills</h2>", unsafe_allow_html=True)

st.write("\n")
# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.write("**Hard Skills**:")
    st.write("- CSS")
    st.write("- HTML")
    st.write("- TypeScript")
    st.write("- Next.js")
    st.write("- Python")
    st.write("- Prompt Engineering")
    st.write("- Git")

with col2:
    st.write("**Soft Skills**:")
    st.write("- Communication Skills")
    st.write("- Debugging")
    st.write("- Quick Learner")
    st.write("- Leadership")