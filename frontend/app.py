import streamlit as st
import requests

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="LLM Chatbot", page_icon="🤖")

st.title("LLM Chatbot (Groq + FastAPI)")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            BACKEND_URL,
            json={"message": user_input}
        )

        if response.status_code == 200:
            reply = response.json().get("response", "No response")

            # Show bot reply
            with st.chat_message("assistant"):
                st.markdown(reply)

            st.session_state.messages.append({"role": "assistant", "content": reply})

        else:
            st.error("Backend error!")

    except Exception as e:
        st.error(f"Connection error: {e}")
