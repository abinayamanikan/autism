@echo off
echo Installing ML dependencies...
pip install streamlit pandas numpy scikit-learn joblib matplotlib seaborn

echo Starting ML Autism Detection App on port 8501...
python -m streamlit run ml_autism_app.py --server.port 8501 --server.address localhost
pause