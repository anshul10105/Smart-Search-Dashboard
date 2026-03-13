import json
import os
from pathlib import Path

INPUT_FOLDER = "Data/raw"
OUTPUT_FILE = "Data/processed/docs.jsonl"


def ingest_documents():

    documents = []

    # read all txt files
    for file in Path(INPUT_FOLDER).glob("*.txt"):

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        doc = {
            "doc_id": file.stem,
            "title": file.stem,
            "text": text,
            "source": "local"
        }

        documents.append(doc)

    # create processed folder
    os.makedirs("Data/processed", exist_ok=True)

    # save as JSONL
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for d in documents:
            f.write(json.dumps(d) + "\n")

    print(f"Ingested {len(documents)} documents successfully!")


if __name__ == "__main__":
    ingest_documents()