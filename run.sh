#!/bin/sh
chmod +x run.sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
