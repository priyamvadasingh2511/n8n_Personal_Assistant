import streamlit as st
import requests
import uuid

# initialize session id
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# create the title for the page
st.title("🤝 Your Personal Assistant")

# add subheader
st.subheader("What can your personal assistant do?")

# create a list of what your assistant can do
st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)

# add chats subheader
st.subheader("💬 Chat with your assistant")

# create a session state for message history
if "messages" not in st.session_state:
    st.session_state.messages = []

 #show the messages in chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# create a chat input box
user_message = st.chat_input()

# if user sends a message
if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        # append the user message to message history
        st.session_state.messages.append({"role": "user", "content": user_message})

    # send the user message to the n8n webhook
response = requests.post(
        "http://localhost:5678/webhook/0e314c2b-2cdc-4b88-9bad-9778886f613c",
        json={"message": user_message, "sessionId": st.session_state.session_id}
    )
#st.write(response.json())
     # get the AI response from webhook
ai_response = response.json()[0]["output"]

     # display the AI response in chat
     #below line means Create a message box styled as an assistant reply"
with st.chat_message("assistant"):
        st.markdown(ai_response)
        # append the AI response to message history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})