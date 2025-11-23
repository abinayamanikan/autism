@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Starting Autism Detection App...
python -m streamlit run app.py

pause