@echo off
echo Starting SRS-Compliant Capable Kitten App...
python -m streamlit run srs_compliant_app.py --server.port 8501 --server.address localhost
pause