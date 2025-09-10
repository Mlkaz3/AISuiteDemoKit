import streamlit as st

st.set_page_config(
    page_title="AI Suite Demo Kit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar menu
st.sidebar.title("Productivity Tools")  # <- Not clickable, just a label

menu = st.sidebar.radio(
    "Choose a tool:",
    [
        "AI@ Minutes",
        "AI@ AskPro",
        "AI@ Summary",
        "AI@ EmailWriter",
        "AI@ SmartReply"
    ]
)

# Main content based on selection
st.title("AI Suite Demo Kit")

if menu == "AI@ Minutes":
    st.header("AI@ Minutes")
    st.write("[The module Minutes] demo kit")
elif menu == "AI@ AskPro":
    st.header("AI@ AskPro")
    st.write("[The module AskPro] demo kit")
elif menu == "AI@ Summary":
    st.header("AI@ Summary")
    st.write("[The module Summary] demo kit")
elif menu == "AI@ EmailWriter":
    st.header("AI@ EmailWriter")
    st.write("[The module EmailWriter] demo kit")
elif menu == "AI@ SmartReply":
    st.header("AI@ SmartReply")
    st.write("[The module SmartReply] demo kit")
