@echo off
echo Installing dependencies...
pip install streamlit pandas numpy scikit-learn joblib

echo.
echo Starting Autism Detection App...
echo Open your browser to: http://localhost:8501
echo.

python -m streamlit run simple_app.py

pause