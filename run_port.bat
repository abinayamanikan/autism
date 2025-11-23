@echo off
echo Starting Autism Detection App on port 8501...
python -m streamlit run simple_app.py --server.port 8501 --server.address localhost
pause