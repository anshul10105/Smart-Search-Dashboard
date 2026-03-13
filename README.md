# Hybrid Search + KPI Dashboard
Video Link is Below
## Overview

This project implements a hybrid search system combining:

- BM25 lexical search
- Semantic vector search using sentence-transformers
- Hybrid ranking with configurable alpha
- FastAPI backend
- Streamlit dashboard
- Evaluation harness
- Experiment tracking
- Unit tests

- The system runs fully on CPU and can be launched locally.

## Architecture

- Data -> Ingestion -> BM25 Index
                  -> Vector Index

- User Query -> Hybrid Search -> FastAPI API -> Dashboard
- The system processes raw documents, builds two indexes (BM25 and vector embeddings), and combines them to return ranked search results.

## Tech Stack

Backend:
- Python
- FastAPI
- rank-bm25
- sentence-transformers
- FAISS

Frontend:
- Streamlit

Storage:
- SQLite
- Local filesystem indexes

Testing:
- pytest


## Setup

Install dependencies:
- pip install -r requirements.txt

## Running the System

Start the backend API:
- uvicorn Backend.app.api:app --reload

Start the dashboard:
- streamlit run Frontend/dashboard.py

## API Endpoints

1.Health check:
- GET /health- Returns the System Status

2.Search endpoint:
- POST /search
Example request:
{
"query": "football",
"top_k": 5,
"alpha": 0.5
} -Returns ranked search results with:
                                1.BM25 score
                                2.Vector similarity score
                                3.Hybrid score

3.Metrics endpoint:
- GET /metrics-Returns system metrics such as - 
                                            1.total queries
                                            2.average latency


## Evaluation

1.Run evaluation harness:
- python Backend/app/eval.py


2.Evaluation queries:

- Data/eval/queries.jsonl


3.Relevance labels:

- Data/eval/qrels.json


4.Experiment results:

- Data/metrics/experiments.csv

## Testing

Run unit tests:
- pytest

## Project Structure
- Backend/
- Frontend/
- Data/
- Docs/
- Tests/
- requirements.txt
- up.sh
- README.md
- pytest.ini


## Hybrid Scoring

The final ranking score is calculated using:

hybrid_score = alpha * bm25_score + (1 - alpha) * vector_score

Where Alpha controls the balance between lexical and semantic search.


## Dashboard

The Streamlit dashboard provides:
- search interface
- result scoring breakdown
- KPI visualization
- query analytics

## Summary
This project demonstrates a complete hybrid retrieval system integrating:
- BM25 lexical ranking
- Semantic embedding search
- API services
- Evaluation framework
- Monitoring metrics
- Interactive dashboard
- The system is designed to run locally on CPU and can be reproduced easily using the  provided scripts.

- Video Link -:https://www.loom.com/share/aad9883c22714147964e0bcd044d2539
