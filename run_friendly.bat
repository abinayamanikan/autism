@echo off
echo Starting Super Friendly Helper App...
python -m streamlit run user_friendly_app.py --server.port 8501 --server.address localhost
pause