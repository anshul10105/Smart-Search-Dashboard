import json
import pickle
from rank_bm25 import BM25Okapi

DOC_FILE = "Data/processed/docs.jsonl"
INDEX_FILE = "Data/index/bm25.pkl"


def build_bm25_index():

    documents = []
    corpus = []

    with open(DOC_FILE, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            documents.append(doc)
            corpus.append(doc["text"].lower().split())

    bm25 = BM25Okapi(corpus)

    with open(INDEX_FILE, "wb") as f:
        pickle.dump((bm25, documents), f)

    print("BM25 index created successfully!")


if __name__ == "__main__":
    build_bm25_index()