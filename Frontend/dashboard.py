import streamlit as st
import requests

st.title("Hybrid Search Dashboard")

API_URL = "http://127.0.0.1:8000/search"

query = st.text_input("Enter your search query")

top_k = st.slider("Number of results", 1, 10, 5)

alpha = st.slider("Hybrid Weight (alpha)", 0.0, 1.0, 0.5)

if st.button("Search"):

    response = requests.post(
        API_URL,
        json={
            "query": query,
            "top_k": top_k,
            "alpha": alpha
        }
    )

    data = response.json()

    # show latency
    st.write("Latency (ms):", round(data["latency_ms"], 2))

    results = data["results"]

    # display results with ranking
    for i, r in enumerate(results, start=1):

        st.subheader(f"{i}. Document {r['doc_id']}")

        st.write("BM25 Score:", r["bm25_score"])
        st.write("Vector Score:", r["vector_score"])
        st.write("Hybrid Score:", r["hybrid_score"])

        st.write(r["text"])

        st.write("---")