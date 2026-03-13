#!/bin/bash

echo "Starting Hybrid Search System..."

# install dependencies
pip install -r requirements.txt

# run ingestion
python Backend/app/ingest.py

# build indexes
python Backend/app/bm25_index.py
python Backend/app/vector_index.py

# start API
uvicorn Backend.app.api:app --reload &

# start dashboard
python -m streamlit run Frontend/dashboard.py