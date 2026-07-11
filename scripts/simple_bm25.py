import json
import math
import re
from pathlib import Path


class BM25:
    def __init__(self):
        self.data = {}
        self.num_papers = 0
        self.avg_dl = 0.0

        self.doc_tokens = {}
        self.doc_lens = {}
        self.doc_freqs = {}
        self.idf = {}

        self._load_data()
        self._build_index()

    def _load_data(self):
        for json_file in Path("./data/").glob("papers_fetch_*.json"):
            with open(json_file, "r", encoding="utf-8") as f:
                papers = json.load(f)

            for item in papers:
                paper = item["paper"]
                tmp1 = {
                    "title": paper["title"],
                    "abstract": paper["summary"],
                }
                self.data[paper["id"]] = tmp1
        self.num_papers = len(self.data)

    def _build_index(self):
        global_doc_freq = {}
        total_words = 0

        for key, document in self.data.items():
            search_data = document["title"] + " " + document["abstract"]
            tokens = self._tokenize(search_data)

            self.doc_tokens[key] = tokens
            self.doc_lens[key] = len(tokens)
            total_words += len(tokens)

            frequencies = {}
            for word in tokens:
                frequencies[word] = frequencies.get(word, 0) + 1
            self.doc_freqs[key] = frequencies

            for word in set(tokens):
                global_doc_freq[word] = global_doc_freq.get(word, 0) + 1

        self.avg_dl = total_words / self.num_papers

        for word, df in global_doc_freq.items():
            self.idf[word] = math.log((self.num_papers - df + 0.5) / (df + 0.5) + 1)

    def _tokenize(self, text: str) -> list[str]:
        text = text.lower()
        data_tok: list[str] = re.sub(r"[^\w\s]", " ", text).split()
        return data_tok

    def get_perfect_score(self, query: str, k1: float = 1.2) -> float:
        query_tok = self._tokenize(query)
        max_score = 0.0

        for token in query_tok:
            idf_score = self.idf.get(token, 0.0)

            max_score += idf_score * (k1 + 1)

        return max_score

    def search(self, query: str, k1: float = 1.2, b: float = 0.75) -> list:
        query_tok = self._tokenize(query)
        results = []

        for key in self.data.keys():
            score = 0.0
            doc_freq = self.doc_freqs[key]
            doc_len = self.doc_lens[key]

            for q in query_tok:
                if q in self.idf and q in doc_freq:
                    f_qd = doc_freq[q]
                    idf_score = self.idf[q]

                    numerator = f_qd * (k1 + 1)
                    denominator = f_qd + k1 * (1 - b + b * (doc_len / self.avg_dl))
                    score += idf_score * (numerator / denominator)

            if score > 0:
                results.append(
                    {"paper_id": key, "score": score, "title": self.data[key]["title"]}
                )

        results.sort(key=lambda x: x["score"], reverse=True)
        return results


bm25 = BM25()
query = "multimodal"
results = bm25.search(query, 1.2, 0.75)
perfect_sc = bm25.get_perfect_score(query)

print(f"Search results for '{query}':")
for idx, result in enumerate(results[:7]):
    percent = result["score"] / perfect_sc * 100.0
    print(
        f"\t{idx + 1}.  {result['paper_id']} - {result['title'][:50]}... --> ({percent:.02f} %)"
    )
