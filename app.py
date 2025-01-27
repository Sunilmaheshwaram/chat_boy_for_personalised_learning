import streamlit as st
import requests

# Rasa API URL (replace with your Rasa server URL)
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# Function to send a message to Rasa and get a response
def get_bot_response(user_message):
    try:
        response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})
        response.raise_for_status()  # Raise an exception for bad responses (4xx, 5xx)
        if response.json():  # Check if there are responses
            return response.json()
        else:
            return [{"text": "Sorry, I couldn't understand that. Please try again."}]
    except requests.exceptions.RequestException as e:
        # Return a friendly error message if there is a problem with the request
        return [{"text": f"Sorry, there was an error: {e}. Please try again later."}]

# Streamlit UI setup
st.set_page_config(page_title="📚 StudyBuddy Educational Chatbot 📚", page_icon="🤖", layout="wide")

# Injecting custom CSS for background color and message styling
st.markdown("""
    <style>
        .user-message {
            background-color: #e6f7ff;  /* Light blue for user messages */
            padding: 8px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        .bot-message {
            background-color: #d1e7d1;  /* Light green for bot messages */
            padding: 8px;
            border-radius: 8px;
            margin-bottom: 5px;
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("📚 StudyBuddy Educational Chatbot 📚")
st.markdown("<h3 class='header' style='text-align: center;'>What can I help with?</h3>", unsafe_allow_html=True)

# Sidebar for additional information or settings (optional)
st.sidebar.title("About StudyBuddy📚")
st.sidebar.markdown("""
- This is an educational chatbot that clears any of your queries.

- This chatbot is open 24/7.

- Feel free to ask questions.

- You can ask questions like:

  - What is Machine Learning?

  - What is Data Science?

  - Tell me about containerisation?

  - What are Data Pipelines?

  - Tell me about Cyber Security?
""")

# Initialize session state if not already done
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat UI
for message in st.session_state["messages"]:
    if message["sender"] == "user":
        # Add "You" before the message with a custom style
        st.markdown(f'<div class="user-message"><strong>You:</strong> {message["text"]}</div>', unsafe_allow_html=True)
    else:
        # Add "Bot" before the message with a custom style
        st.markdown(f'<div class="bot-message"><strong>Buddy:</strong> {message["text"]}</div>', unsafe_allow_html=True)

# Input box for user query
if user_input := st.chat_input("Message StudyBuddy"):
    # Display the user's message in the chat
    st.session_state["messages"].append({"sender": "user", "text": user_input})
    st.markdown(f'<div class="user-message"><strong>You:</strong> {user_input}</div>', unsafe_allow_html=True)

    # Fetch the bot's response
    with st.spinner("Thinking..."):
        bot_responses = get_bot_response(user_input)

    # Combine bot responses into a single message and display it
    bot_message = "\n".join([resp["text"] for resp in bot_responses])
    st.session_state["messages"].append({"sender": "bot", "text": bot_message})
    st.markdown(f'<div class="bot-message"><strong>Buddy:</strong> {bot_message}</div>', unsafe_allow_html=True)
