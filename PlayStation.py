import streamlit as st

def render():
    st.header("PlayStation Page")
    st.write("Welcome to the PlayStation page!")

    st.subheader("Games Library")

    games = [
        {"name": "FIFA 25", "icon": "⚽", "path": "games/fifa25.html"},
        {"name": "Gran Turismo", "icon": "🏎️", "path": "games/granturismo.html"},
        {"name": "God of War", "icon": "🗡️", "path": "games/godofwar.html"},
        {"name": "Spider-Man", "icon": "🕷️", "path": "games/spiderman.html"},
        {"name": "Uncharted", "icon": "🧭", "path": "games/uncharted.html"},
    ]

    cols = st.columns(len(games))
    for idx, game in enumerate(games):
        with cols[idx]:
            st.markdown(
                f"""
                <div style='display: flex; flex-direction: column; align-items: center;'>
                    <a href='{game['path']}' style='text-decoration: none;'>
                        <div style='font-size:40px; cursor:pointer;'>{game['icon']}</div>
                    </a>
                    <div style='margin-top:8px; font-weight:bold;'>{game['name']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)