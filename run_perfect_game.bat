@echo off
echo Starting Perfect Game Center...
python -m streamlit run perfect_game_ui.py --server.port 8501 --server.address localhost
pause