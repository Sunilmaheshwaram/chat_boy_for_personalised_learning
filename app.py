import streamlit as st
import requests

# Rasa API URL (replace with your Rasa server URL)
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# Function to send message to Rasa and get response
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

# Streamlit UI Setup
st.set_page_config(page_title="📚 StudyBuddy Educational Chatbot 📚", page_icon="🤖", layout="wide")

# Title of the app
st.title("📚 StudyBuddy Educational Chatbot 📚")

# Sidebar for additional information or settings (optional)
st.sidebar.title("About StudyBuddy📚")
st.sidebar.markdown("""
- This is an educational chatbot that clears any of your queries.
- This chatbot is open 24/7.
- Feel free to ask questions.
- Customer Support:
  - Mail   ✉️: xxxxxxxxxxx@gmail.com
  - Contact ☎: xxxxxxx987
- Powered by Rasa.
- Created by Sunil Maheshwaram
""")

# Initialize session state if not already done
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Display previous messages in the chat
for message in st.session_state['messages']:
    if message['sender'] == 'user':
        st.markdown(f"**You:** {message['text']}")
    else:
        st.markdown(f"**Bot:** {message['text']}")

# Input box for both search and question with watermark (placeholder text)
user_input = st.text_input("Ask your question/Topic:", placeholder="StudyBuddy")

# Handle user input and prevent duplicating previous responses
if user_input:
    # Add user message to chat history
    st.session_state['messages'].append({'sender': 'user', 'text': user_input})

    # Get response from Rasa bot immediately after the input is given
    bot_responses = get_bot_response(user_input)

    # Group bot responses and display them as a single message block
    bot_message = "\n".join([bot_response['text'] for bot_response in bot_responses])

    # Add the bot response to chat history
    st.session_state['messages'].append({'sender': 'bot', 'text': bot_message})

    # Rerun the Streamlit app to display the new messages immediately


