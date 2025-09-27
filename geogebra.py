import streamlit as st
import streamlit.components.v1 as components

def render():
    st.header("GeoGebra Page")
    st.write("Welcome to the GeoGebra page!")
    st.subheader("Interactive GeoGebra Applet")

    # HTML and CSS content for the GeoGebra applet, formatted as a single string
    geogebra_html = """
    <div style='
        background-color: rgb(230, 193, 228);
        padding: 2%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        margin: 0;
        font-family: "Arial", sans-serif;
        text-align: center;
    '>
        <fieldset style='
            box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.5);
            background-color: rgb(233, 233, 233);
            border: 2px solid rgb(0, 0, 0);
            border-radius: 15px;
            margin: 0 auto;
            width: auto;
            max-width: 800px;
        '>
            <legend><h1 style='
                box-shadow: rgb(0, 0, 0) 0px 0px 20px;
                border: 1px solid black;
                padding: 1%;
                background-color: rgb(117, 3, 142);
                color: rgb(215, 209, 209);
                font-size: 1.5rem;
                margin: 0 auto;
                border-radius: 5px;
            '>GeoGebra - Classic 6</h1></legend>
            <section id="Graphical" style="
                border: 2px solid black;
                box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.5);
                width: 100%;
                height: 600px;
                margin: 20px auto;
                background-color: white;
            "></section>
           
        </fieldset>
    </div>
    <script src="https://www.geogebra.org/apps/deployggb.js"></script>
    <script>
        var params = {
            "appName": "graphingcalculator",
            "width": 800,
            "height": 600,
            "showToolBar": true,
            "showAlgebraInput": true,
            "showMenuBar": true
        };
        var applet = new GGBApplet(params, true);
        window.addEventListener("load", function() {
            applet.inject("Graphical");
        });
    </script>
    """
    
    components.html(geogebra_html, height=800)
    st.markdown(
        """
        <style>
            /* Responsive adjustments */
            @media (max-width: 600px) {
                div[style*="min-height: 100vh"] {
                    padding: 5%;
                }
                fieldset {
                    width: 100% !important;
                }
                section#Graphical {
                    height: 400px !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )