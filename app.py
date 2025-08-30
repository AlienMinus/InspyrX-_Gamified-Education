# Import the necessary libraries, including the new chatbot module
import streamlit as st
import geogebra
import scratch
import PlayStation
from spyrotron import ai_chatbot # Import the new ai_chatbot function

def render_page(page_name):
    """
    Renders the selected page based on the navigation menu.
    """
    if page_name == "PlayStation":
        PlayStation.render()
    elif page_name == "GeoGebra":
        geogebra.render()
    elif page_name == "Scratch3.0":
        scratch.render()
    elif page_name == "Spyrotron AI":
        # Call the function from the separate chatbot.py file
        ai_chatbot()
    else:
        st.error("Page not found")

# --- Main app configuration ---
st.set_page_config(page_title="Hackathon2025 UI", page_icon="🎮")
st.title("Hackathon2025 UI")
page = st.sidebar.radio(
    "Navigation Menu",
    ["PlayStation", "GeoGebra", "Scratch3.0", "Spyrotron AI"]
)
render_page(page)
