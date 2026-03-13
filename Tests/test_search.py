import sys
import os

sys.path.append(os.path.abspath("."))

from Backend.app.search import hybrid_search


def test_search():

    results = hybrid_search("football", top_k=3)

    assert len(results) > 0