import streamlit as st
import geogebra, scratch, spyrotron, PlayStation, documentation
from spyrotron import ai_chatbot

st.set_page_config(page_title="Hackathon2025 UI", page_icon="🎮")

def render_page(page_name):
    if page_name == "PlayStation":
        PlayStation.render()
    elif page_name == "GeoGebra":
        geogebra.render()
    elif page_name == "Scratch3.0":
        scratch.render()
    elif page_name == "Spyrotron AI":
        ai_chatbot()
    elif page_name == "Documentation":
        documentation.render()
    else:
        st.error("Page not found")

# --- Main app configuration ---
st.title("Hackathon2025 UI")
page = st.sidebar.radio(
    "Navigation Menu",
    ["PlayStation", "GeoGebra", "Scratch3.0", "Spyrotron AI", "Documentation"]
)
render_page(page)