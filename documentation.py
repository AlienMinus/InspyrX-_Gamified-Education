import streamlit as st
import base64

def render():
    st.title("📄 PDF Viewer in Streamlit")

    # Path to your PDF file
    pdf_file = "./docs/InspyrX.pdf"

    # Read the PDF file and encode it
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embed the PDF in an iframe
    pdf_display = f'''
    <iframe src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" height="800" type="application/pdf"></iframe>
    '''

    st.markdown(pdf_display, unsafe_allow_html=True)