import streamlit as st

from tools import websearch_agent


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Autonomous Research Agent",
    page_icon="🔎",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🔎 Autonomous Research Agent")

st.caption(
    "Ask a research question and I will search the web, "
    "analyze the information, and generate a structured report."
)


# -----------------------------
# Chat history
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display previous messages
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -----------------------------
# Chat input
# -----------------------------

if prompt := st.chat_input(
    "What would you like me to research?"
):

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Agent response
    with st.chat_message("assistant"):

        with st.spinner("🔎 Researching the web..."):

            response = websearch_agent.run(prompt)

            answer = response.content

        st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )