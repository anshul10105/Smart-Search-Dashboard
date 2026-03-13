import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

DOC_FILE = "Data/processed/docs.jsonl"
INDEX_FILE = "Data/index/vector.index"

def build_vector_index():

    texts = []

    # read processed documents
    with open(DOC_FILE, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            texts.append(doc["text"])

    print("Loading embedding model...")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Creating embeddings...")

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, INDEX_FILE)

    print("Vector index created successfully!")


if __name__ == "__main__":
    build_vector_index()