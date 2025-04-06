import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyCL_gd1rWMK2SOF8sHxGHLYrMESdRyo2to")

# Using Gemini 1.5 Flash Model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

st.title("Gemini 1.5 Flash Chatbot ⚡")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = model.generate_content(prompt).text
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
