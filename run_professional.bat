@echo off
echo Installing professional dependencies...
pip install streamlit pandas numpy plotly

echo Starting Professional Autism Detection Platform...
python -m streamlit run professional_autism_app.py --server.port 8501 --server.address localhost
pause