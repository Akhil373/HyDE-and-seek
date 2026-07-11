from dotenv import load_dotenv
from papers_search.embeddings import get_embeddings, supabase

load_dotenv()


def create_search_pipeline():
    def run_search(query_text, top_k=5):
        query_vector = get_embeddings(query_text, "query", "hf")

        response = supabase.rpc(
            "match_documents",
            {
                "query_embedding": query_vector,
                "match_threshold": 0.2,
                "match_count": top_k,
            },
        ).execute()

        return response.data

    return run_search
