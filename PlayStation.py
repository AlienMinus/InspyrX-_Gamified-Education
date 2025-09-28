import streamlit as st
import json
import os

def render():
    st.header("PlayStation Page")
    st.write("Welcome to the PlayStation page!")

    st.subheader("Games Library")

    # Load games from JSON file
    json_path = os.path.join(os.path.dirname(__file__), "./json-paths/games.json")
    with open(json_path, "r", encoding="utf-8") as f:
        games = json.load(f)

    selected_game_path = None
    cols = st.columns(len(games))
    for idx, game in enumerate(games):
        with cols[idx]:
            if st.button(game['icon'], key=game['name']):
                selected_game_path = game['iframe_url']
            st.markdown(
                f"""
                <style>
                .st-emotion-cache-15hul6a {{
                    font-size: 50px;
                    text-align: center;
                    margin-bottom: 10px;
                    color: #ff4500;
                    border-radius: 10px;
                    padding: 10px;
                    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
                    justify-content: center;
                }}
                .st-emotion-cache-15hul6a:hover {{
                    background-color: #f0f0f0;
                }}
                .st-emotion-cache-1wmy9hl .e1f1d6gn1{{
                    text-align: center;
                    font-weight: bold;
                    font-size: 100px;
                }}
                """,
                unsafe_allow_html=True
            )
            st.write(game['name'])

    if selected_game_path:
        st.subheader("Now Playing:")
        st.markdown(f"### {next(game['name'] for game in games if game['iframe_url'] == selected_game_path)}")
        st.components.v1.html(
            f"""
            <div style="position:relative;width:100%;height:0;padding-bottom:56.25%;">
                <iframe src="{selected_game_path}" style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;" allowfullscreen></iframe>
            </div>
            """,
            height=700,
            scrolling=True,
            seamless=True,
            unsafe_allow_html=True
        )