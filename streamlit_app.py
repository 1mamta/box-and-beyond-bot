import streamlit as st
from chatbot import get_response
import re

# Page config
st.set_page_config(page_title="Box and Beyond Bot", page_icon="🛍️")
st.title("🛍️ Box and Beyond Chatbot")
st.caption("Your personal gifting assistant. Ask me about earrings, clutchers, hampers, offers & more!")

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="input", placeholder="Ask me something...")

# Get response and store it
if user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Show chat
for sender, message in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        # Separate image URLs from message
        urls = re.findall(r'(https?://\S+)', message)
        text = re.sub(r'(https?://\S+)', '', message).strip()
        if text:
            st.markdown(text)
        for url in urls:
            st.image(url, use_column_width=True)

# Optional: Instagram & WhatsApp Buttons
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.link_button("📸 Instagram", "https://www.instagram.com/boxandbeyond_")
with col2:
    st.link_button("💬 WhatsApp", "https://wa.me/919999999999")
