@echo off
echo Installing required packages...
pip install streamlit pandas numpy scikit-learn joblib

echo.
echo Starting Autism Detection App...
python -m streamlit run app.py

pause