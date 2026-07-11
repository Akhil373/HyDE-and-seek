import pytest

from papers_search.benchmarks.queries import queries
from papers_search.BM25 import BM25
from papers_search.retrieval import retrieval
from papers_search.search import create_search_pipeline


@pytest.fixture(scope="session")
def search_pipeline():
    return create_search_pipeline()


@pytest.fixture(scope="module")
def bm25():
    return BM25()


@pytest.mark.parametrize("query, expected_id", queries)
def test_hybrid_search_accuracy(query, expected_id, bm25):
    # results = search_pipeline(query, top_k=5)
    results, titles = retrieval(query, bm25, depth=50)
    result_ids = [doc_id for doc_id, _ in results] if results else []
    assert expected_id in result_ids, f"Expected {expected_id} but got {result_ids}"
