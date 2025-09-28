import streamlit as st
import os

def render():
    st.title("📄 Documentation")

    readme_file = "./README.md"
    if os.path.exists(readme_file):
        with open(readme_file, "r", encoding="utf-8") as f:
            readme_content = f.read()
        st.markdown(readme_content, unsafe_allow_html=True)
    else:
        st.error("README.md file not found.")