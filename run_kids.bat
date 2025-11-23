@echo off
echo Starting Kids Autism Helper on port 8501...
python -m streamlit run kids_app.py --server.port 8501 --server.address localhost
pause