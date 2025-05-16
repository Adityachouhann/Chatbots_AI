import streamlit as st
from chatbot import get_response

# Page setup
st.set_page_config(page_title="Jarvis Chatbot 🤖", page_icon="💬", layout="centered")

# CSS for styling
st.markdown("""
    <style>
        html, body {
            background-color: #0f1117;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #0f1117;
            padding: 2rem;
        }
        h1 {
            color: #36C5F0;
            font-size: 48px;
            text-align: center;
            margin-bottom: 1rem;
        }
        .chat-box {
            background-color: #1e212d;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🤖 Jarvis - Your AI Assistant</h1>", unsafe_allow_html=True)

# Default suggestion banner
st.markdown(
    "<div style='background-color:#1e212d; padding: 10px; border-radius: 10px; font-size: 18px;'>"
    "<b>💡 Try asking me:</b><br>"
    "• Who is the Prime Minister of India?<br>"
    "• What is Python?<br>"
    "• Motivate me<br>"
    "• Tell me a joke<br>"
    "• Who is the best cricketer?<br>"
    "• What is Streamlit?"
    "</div><br>", unsafe_allow_html=True
)

# Chat Input
user_input = st.text_input("💬 You:", "", key="input", help="Type your question here...")

if user_input:
    response = get_response(user_input)

    st.markdown(f"""
        <div class="chat-box">
            <b style="color:#1db954;">You:</b> {user_input}<br><br>
            <b style="color:#faca15;">Jarvis:</b> {response}
        </div>
    """, unsafe_allow_html=True)
