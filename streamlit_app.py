import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("💬 FocusBud AI")
st.write("Talk to your AI assistant right here:")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# User input
user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Get response from OpenAI
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"]
        )

    bot_reply = response["choices"][0]["message"]["content"]
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

# Display chat
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**AI:** {msg['content']}")
