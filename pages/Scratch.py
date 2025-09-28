import streamlit as st
import json
import os

def load_projects():
    """Loads scratch projects from a JSON file."""
    json_path = os.path.join(os.path.dirname(__file__), '../json-paths/scratch_projects.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f).get("projects", [])
    except Exception as e:
        st.error(f"Error loading projects: {e}")
        return []

def render():
    st.header("Scratch Page")
    st.write("Welcome to the Scratch page! Click a project to view it.")

    projects = load_projects()
    if not projects:
        st.warning("No Scratch projects found. Please add projects to `scratch_projects.json`.")
        return

    selected_game_path = None
    cols = st.columns(len(projects))
    for idx, project in enumerate(projects):
        with cols[idx]:
            if st.button(project['icon'], key=project.get('title', f"project_{idx}")):
                selected_game_path = project['url']
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
            st.write(project['title'])

    if selected_game_path:
        st.subheader("Now Playing:")
        st.markdown(f"### {next(project['title'] for project in projects if project['url'] == selected_game_path)}")
        st.components.v1.html(
            f"""
            <div style="position:relative;width:100%;height:0;padding-bottom:56.25%;">
                <iframe src="{selected_game_path}" style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;" allowfullscreen></iframe>
            </div>
            """,
            height=700,
            scrolling=True
        )