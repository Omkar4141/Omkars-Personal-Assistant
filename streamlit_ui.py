# Import required libraries
import streamlit as st
from chatbot import get_ai_response

# Streamlit app title
st.title("🧠 Omkar's AI Assistant")

# Introduction message
st.write("Welcome! Ask anything about Omkar and get quick responses!")

# Initialize chat history if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input from the text area
user_input = st.chat_input("Type your message here...")

# Process input when user submits a message
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response from the chatbot
    ai_response = get_ai_response(user_input)

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Display user message and AI response
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        st.write(ai_response)
