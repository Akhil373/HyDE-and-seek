from ast import keyword
from datetime import datetime

from papers_search.BM25 import BM25
from papers_search.main import EMBEDDING_METHOD, get_embeddings, groq, logging, supabase


def semantic_search(query: str, depth: int):
    hyde = groq(query)
    # print(hyde, "\n")
    hyde_embedding = get_embeddings(hyde, method=EMBEDDING_METHOD, structure="query")

    try:
        response = supabase.rpc(
            "match_documents_with_scores",
            {
                "query_embedding": hyde_embedding,
                "match_threshold": 0.2,
                "match_count": depth,
            },
        ).execute()

        if response.data is not None:
            for row in response.data:
                row.pop("embeddings", None)

        return response
    except Exception:
        logging.critical("An error occurred during semantic search")
        raise


def retrieval(query: str, bm25: BM25, depth=50, k=60, top_k=7) -> tuple:
    titles = {}
    top_results = {}

    # --- BM25  keyword search ---
    then = datetime.now()
    results = bm25.search(query, count=depth)
    # perfect_sc = bm25.get_perfect_score(query)
    keyword_ranks = {doc["paper_id"]: idx + 1 for idx, doc in enumerate(results)}
    keyword_titles = {doc["paper_id"]: doc["title"] for doc in results}

    # --- HyDE semantic search ---
    response = semantic_search(query, depth)
    semantic_ranks = {doc["id"]: idx + 1 for idx, doc in enumerate(response.data)}
    semantic_titles = {doc["id"]: doc["title"] for doc in response.data}

    # --- rank reciprocal fusion ---
    titles = {**semantic_titles, **keyword_titles}
    rankings = {}
    for doc_id in keyword_ranks.keys() | semantic_ranks.keys():
        score = 0.0
        if doc_id in keyword_ranks:
            score += 1 / (k + keyword_ranks[doc_id])
        if doc_id in semantic_ranks:
            score += 1 / (k + semantic_ranks[doc_id])
        rankings[doc_id] = score

    top_results = sorted(rankings.items(), key=lambda x: x[1], reverse=True)[:top_k]

    # scores = [s for _, s in top_results]
    # max_s, min_s = max(scores), min(scores)
    # score_range = max_s - min_s if max_s != min_s else 1e-9
    return (top_results, titles)


if __name__ == "__main__":
    bm25 = BM25()
    depth = 50
    query = input()
    results, titles = retrieval(query, bm25, depth)
    print("Search results:")
    for i, (doc_id, score) in enumerate(results, 1):
        print(f"\t{i}.  {doc_id} - {titles[doc_id]}")
