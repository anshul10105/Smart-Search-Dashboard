from fastapi import FastAPI
from pydantic import BaseModel
from Backend.app.search import hybrid_search

import sqlite3
import time
import uuid
import os

app = FastAPI()

DB_FILE = "Data/metrics/search_logs.db"


# create database if not exists
def init_db():

    os.makedirs("Data/metrics", exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            request_id TEXT,
            query TEXT,
            latency_ms REAL,
            result_count INTEGER
        )
    """)

    conn.commit()
    conn.close()


init_db()


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    alpha: float = 0.5


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/search")
def search(req: SearchRequest):

    request_id = str(uuid.uuid4())

    start_time = time.time()

    results = hybrid_search(
        req.query,
        req.top_k,
        req.alpha
    )

    latency = (time.time() - start_time) * 1000

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO logs VALUES (?, ?, ?, ?)",
        (request_id, req.query, latency, len(results))
    )

    conn.commit()
    conn.close()

    return {
        "request_id": request_id,
        "latency_ms": latency,
        "results": results
    }


@app.get("/metrics")
def metrics():

    import sqlite3

    conn = sqlite3.connect("Data/metrics/search_logs.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM logs")
    total_queries = cur.fetchone()[0]

    cur.execute("SELECT AVG(latency_ms) FROM logs")
    avg_latency = cur.fetchone()[0]

    conn.close()

    return {
        "total_queries": total_queries,
        "avg_latency_ms": avg_latency
    }