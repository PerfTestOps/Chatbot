import streamlit as st

# Title
st.title("💬 Simple Chatbot")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User input box
user_input = st.text_input("Type your message:")

# When user submits
if st.button("Send"):
    if user_input:
        # Add user message
        st.session_state["messages"].append(("You", user_input))

        # Generate chatbot response (simple echo logic here)
        response = f"I heard you say: {user_input}"
        st.session_state["messages"].append(("Bot", response))

# Display chat history
for sender, msg in st.session_state["messages"]:
    if sender == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
