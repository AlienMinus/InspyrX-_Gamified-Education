import streamlit as st

def render():
    st.header("PlayStation Page")
    st.write("Welcome to the PlayStation page!")

    st.subheader("Games Library")

    games = [
        {"name": "FIFA 25", "icon": "⚽", "path": "games/fifa25.html"},
        {"name": "Gran Turismo", "icon": "🏎️", "path": "games/granturismo.html"},
        {"name": "God of War", "icon": "🗡️", "path": "games/godofwar.html"},
        {"name": "Tic-Tac-Toe", "icon": "❌", "path": "games/tictactoe.html"},
        {"name": "Uncharted", "icon": "🧭", "path": "games/uncharted.html"},
    ]

    selected_game_path = None
    cols = st.columns(len(games))
    for idx, game in enumerate(games):
        with cols[idx]:
            if st.button(game['icon'], key=game['name']):
                selected_game_path = game['path']
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
        st.markdown(f"### {next(game['name'] for game in games if game['path'] == selected_game_path)}")
        st.components.v1.html(
            f'<iframe src="{selected_game_path}" width="100%" height="100%"></iframe>',
            height=600,
        )