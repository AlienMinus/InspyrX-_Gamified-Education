import streamlit as st

def render():
    st.header("Scratch Page")
    st.write("Welcome to the Scratch page!")

    st.markdown(
        """
        <!DOCTYPE html>
<html>
<head>
<title>Embedding Scratch Project</title>
</head>
<body>
<h1>My Scratch Project</h1>
<iframe
src="https://scratch.mit.edu/projects/164932339/embed"
allowtransparency="true"
width="485"
height="402"
frameborder="0"
scrolling="no"
allowfullscreen>
</iframe>
<p>Created using Scratch!</p>
</body>
</html>
        """,
        unsafe_allow_html=True
    )