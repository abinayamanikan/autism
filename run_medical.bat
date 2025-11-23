@echo off
echo Starting Medical-Grade Autism Screening Tool on port 8501...
python -m streamlit run medical_app.py --server.port 8501 --server.address localhost
pause