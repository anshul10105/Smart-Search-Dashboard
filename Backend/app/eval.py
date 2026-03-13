import json
from search import hybrid_search

print("Running evaluation...\n")

# read queries file
queries = []

with open("Data/eval/queries.jsonl", "r") as f:
    for line in f:
        data = json.loads(line)
        queries.append(data["query"])

# run search
for q in queries[:5]:

    print("Query:", q)

    results = hybrid_search(q, top_k=5)

    for r in results:
        print("   ", r["doc_id"], r["hybrid_score"])

    print()