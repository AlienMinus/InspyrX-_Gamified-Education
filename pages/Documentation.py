import streamlit as st
import base64
import os

def render():
    st.title("📄 Documentation")

    tab1, tab2 = st.tabs(["PDF", "README.md"])

    with tab1:
        st.subheader("InspyrX.pdf")
        pdf_file = "./docs/InspyrX.pdf"
        if os.path.exists(pdf_file):
            with open(pdf_file, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'''
            <iframe src="data:application/pdf;base64,{base64_pdf}" 
                    width="100%" height="800" type="application/pdf"></iframe>
            '''
            st.markdown(pdf_display, unsafe_allow_html=True)
        else:
            st.error("PDF file not found.")

    with tab2:
        st.subheader("README.md")
        readme_file = "./README.md"
        if os.path.exists(readme_file):
            with open(readme_file, "r", encoding="utf-8") as f:
                readme_content = f.read()
            st.markdown(readme_content, unsafe_allow_html=True)
        else:
            st.error("README.md file not found.")