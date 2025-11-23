@echo off
echo Installing packages...
pip install streamlit pandas numpy scikit-learn joblib
echo.
echo Starting app...
python -m streamlit run simple_app.py
pause