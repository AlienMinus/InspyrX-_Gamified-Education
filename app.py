# Import the necessary libraries, including the new chatbot module
import streamlit as st
from pages import GeoGebra, Scratch, PlayStation, Documentation
from pages.Spyrotron import ai_chatbot

# Set the page configuration
st.set_page_config(page_title="Hackathon2025 UI", page_icon="🎮")

def render_page(page_name):
    """
    Renders the selected page based on the navigation menu.
    """
    if page_name == "PlayStation":
        PlayStation.render()
    elif page_name == "GeoGebra":
        GeoGebra.render()
    elif page_name == "Scratch3.0":
        Scratch.render()
    elif page_name == "Spyrotron AI":
        # Call the function from the separate chatbot.py file
        ai_chatbot()
    elif page_name == "Documentation":
        Documentation.render()
    else:
        st.error("Page not found")

# --- Main app configuration ---
st.markdown("""
<head>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7581861713562502"
     crossorigin="anonymous"></script>
</head>
""",  unsafe_allow_html=True)
st.title("Hackathon2025 UI")
page = st.sidebar.radio(
    "Navigation Menu",
    ["PlayStation", "GeoGebra", "Scratch3.0", "Spyrotron AI", "Documentation"]
)
render_page(page)

