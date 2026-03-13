import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# load BM25 index
with open("Data/index/bm25.pkl", "rb") as f:
    bm25, documents = pickle.load(f)

# load vector index
index = faiss.read_index("Data/index/vector.index")

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def hybrid_search(query, top_k=5, alpha=0.5):

    # tokenize query
    tokenized_query = query.lower().split()

    # BM25 scores
    bm25_scores = bm25.get_scores(tokenized_query)

    # vector embedding
    query_vector = model.encode([query])

    D, I = index.search(np.array(query_vector), len(documents))

    vector_scores = D[0]

    results = []

    for i in range(len(documents)):

        bm25_score = bm25_scores[i]
        vector_score = vector_scores[i]

        hybrid_score = alpha * bm25_score + (1 - alpha) * vector_score

        results.append({
            "doc_id": documents[i]["doc_id"],
            "bm25_score": float(bm25_score),
            "vector_score": float(vector_score),
            "hybrid_score": float(hybrid_score),
            "text": documents[i]["text"]
        })

    # sort by hybrid score
    results.sort(key=lambda x: x["hybrid_score"], reverse=True)

    return results[:top_k]