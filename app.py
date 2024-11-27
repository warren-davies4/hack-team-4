import streamlit as st
import random
import time
import streamlit.components.v1 as components
import base64

LOGO_IMAGE = "images/NHS_England_logo.jpg"


# Streamed response emulator
def response_generator(message, persona, language):
    response = f"You said {message}, you are a {persona}, we are speaking in {language}"
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


with open('./style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">Workforce, training and education</p>
    </div>
    """,
    unsafe_allow_html=True
)



st.title("NHS Career coach")
st.subheader("Who are you?")



persona = st.selectbox(
    "Who are you?",
    (
        "Child", 
        "Adult",
    ),
    index=None,
    placeholder="I am a...",
)
language = st.selectbox(
    "Talk to me in...",
    (
        "English", 
        "Spanish", 
        "Korean",
        "Pirate"
    ),
    index=None,
    placeholder="I am a...",
)



st.subheader("Let's chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(st.session_state.messages[-1]['content'], persona, language))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})