from papers_search.benchmarks.queries import queries
from papers_search.search import create_search_pipeline
from concurrent.futures import ThreadPoolExecutor

search_pipeline = create_search_pipeline()


def recall_at_k(queries, k, log_fail=False):
    n = len(queries)
    hits = 0
    failures = []
    rr = 0.0

    print(f"processing k@{k}...")
    for id, (query, expected_id) in enumerate(queries):
        results = search_pipeline(query, top_k=k)
        result_ids = [r["id"] for r in results]

        if expected_id in result_ids:
            hits += 1
            rr += 1 / (result_ids.index(expected_id) + 1)
        else:
            if log_fail:
                failures.append((query, expected_id, result_ids))

    if log_fail and len(failures) > 0:
        print("failures:")
        for query, expected_id, result_ids in failures:
            print(f"\tQuery: {query}")
            print(f"\tExpected: {expected_id}")
            print(f"\tGot: {result_ids}")
            print("-" * 80)

    return hits / len(queries), rr / n


if __name__ == "__main__":
    print(f"Queries: {len(queries)}")
    arr = [5]
    results = []

    def process(v):
        log_fail = v == 5
        recall, mrr = recall_at_k(queries[100:], v, log_fail)
        return v, recall, mrr

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(process, arr)

    for v, recall, mrr in results:
        print(f"Recall@{v} : {recall:.3f} | MRR@{v}: {mrr}")
