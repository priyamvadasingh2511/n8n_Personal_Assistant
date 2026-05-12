🤖 Personal AI Assistant using n8n + Streamlit

This is a simple learning project where I built a basic AI Personal Assistant using n8n workflows and a Streamlit frontend.

🚀 What This Project Does

The user can chat with the assistant through a Streamlit interface.

The frontend sends the user message to an n8n webhook, where the workflow processes the request and returns an AI-generated response back to the frontend.

The assistant can:

Answer basic questions
Help with productivity-related tasks
Simulate email/calendar/task management workflows

🛠️ Tech Stack

Python
Streamlit
n8n
Webhooks
REST API calls

⚙️ How It Works

User enters a message in the Streamlit chat UI
The frontend sends the message to an n8n webhook
n8n processes the request through the workflow
The response is returned and displayed in the chat interface
