@echo off
echo Starting Autism Awareness & Prediction Platform...
python -m streamlit run autism_detection_app.py --server.port 8501 --server.address localhost
pause