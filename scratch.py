import streamlit as st
import json
import os
import math

# Define the path to the JSON file relative to this script
JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), 'scratch_projects.json')

def load_projects():
    """Loads scratch projects from a JSON file."""
    try:
        with open(JSON_FILE_PATH, 'r') as f:
            data = json.load(f)
            return data.get("projects", [])
    except FileNotFoundError:
        st.error(f"Error: The file {JSON_FILE_PATH} was not found.")
        return []
    except json.JSONDecodeError:
        st.error(f"Error: Could not decode JSON from {JSON_FILE_PATH}.")
        return []

def render():
    """Renders the Scratch page with a responsive grid of projects."""
    st.header("Scratch Page")
    st.write("Welcome to the Scratch page! Here are the available projects.")

    projects = load_projects()

    if not projects:
        st.warning("No Scratch projects found. Please add projects to `scratch_projects.json`.")
        return
    
    # 1. Generate the HTML for each project card
    project_cards_html = ""
    for project in projects:
        title = project.get('title', 'No Title')
        url = project.get('url')
        if not url:
            continue
        
        project_cards_html += f"""
        <div class="project-card">
            <h3 class="project-title">{title}</h3>
            <iframe
                src="{url}"
                allowtransparency="true"
                width="100%"
                height="402"
                frameborder="0"
                scrolling="no"
                allowfullscreen>
            </iframe>
        </div>
        """

    # 2. Define the CSS for the responsive grid.
    # This creates a grid that automatically adjusts the number of columns based on screen width.
    responsive_grid_style = """
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));
            gap: 1.5rem;
        }
        .project-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 0.75rem; }
    </style>
    """

    full_html = f"{responsive_grid_style}<div class='grid-container'>{project_cards_html}</div>"
    
    # 3. Estimate height to avoid scrollbars in the component.
    num_rows = math.ceil(len(projects) / 2) if len(projects) > 1 else 1
    estimated_height = num_rows * 480  # Approx 480px per row (iframe + title + gap)
    
    st.components.v1.html(full_html, height=estimated_height)