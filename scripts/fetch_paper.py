import logging
import os
import datetime
from typing import Literal
from typing import TypedDict
from concurrent.futures import ThreadPoolExecutor
import requests
from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
if not url or not key:
    logging.critical("Supabase credentials not found!")
    raise ValueError()

logging.info(
    "Supabase URL: %s Key: %s",
    url[:10],
    key[:10],
)
supabase: Client = create_client(url, key)

LOCAL_EMBEDDING_URL = os.getenv(
    "LOCAL_EMBEDDING_URL", "http://localhost:8080/embedding"
)
HF_EMBEDDING_URL = os.getenv(
    "HF_EMBEDDING_URL",
    "https://router.huggingface.co/hf-inference/models/google/embeddinggemma-300m/pipeline/feature-extraction",
)
EMBEDDING_METHOD: Literal["hf", "local"] = "hf"


class PaperInfo(TypedDict):
    id: str
    title: str
    abstract: str
    embedding: list[float]
    arxiv_url: str
    hf_url: str
    published_at: str | None


def get_embeddings(
    text, structure: Literal["document", "query"], method: Literal["hf", "local"] = "hf"
) -> list[float]:
    """generating embeddings either HF or llama.cpp server"""
    endpoints = {
        "local": LOCAL_EMBEDDING_URL,
        "hf": HF_EMBEDDING_URL,
    }
    endpoint = endpoints.get(method)
    if not endpoint:
        raise ValueError(f"Unsupported method: '{method}'. Expected 'hf' or 'local'.")

    # text is already suitably formatted in main for 'document'
    formatted_text = (
        text if structure == "document" else f"task: search result | query: {text}"
    )
    payload = {"inputs": formatted_text}

    headers = {
        "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}",
    }
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        data = response.json()
        return data if method == "hf" else data[0]["embedding"][0]

    except Exception:
        logging.error("An error occurred when generating embeddings")
        raise


def groq(text):
    """HyDE with groq API"""
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """
You are an expert AI researcher. The user will provide a technical problem or question.
Your task is to write a hypothetical scientific abstract for a research paper that perfectly solves the user's problem.

CRITICAL RULES:
1. Do NOT invent highly specific, fake acronyms (e.g., do not invent "Deferred Image Loading (DIL)"). Use broad, standard academic terminology instead (e.g., "on-demand loading mechanisms").
2. Contextualize the problem. If the user asks about a bot looking at webpages, assume the paper is about "Autonomous Agents", "Multimodal Search", or "Web Navigation" and include those terms.
3. Write exactly one paragraph. Do not include a title.
                """,
            },
            {
                "role": "user",
                "content": f"""Write a short abstract for an AI/ML research paper that would directly answer this search query.

                Query: {text}

                Abstract:""",
            },
        ],
        model="llama-3.3-70b-versatile",
        max_completion_tokens=500,
        # extra_body={"include_reasoning": False},
    )
    return chat_completion.choices[0].message.content


def create_paper_info(paper: dict, embedding: list[float]) -> PaperInfo:
    return {
        "id": paper["id"],
        "title": paper["title"],
        "abstract": paper["summary"],
        "embeddings": embedding,
        "arxiv_url": f"https://arxiv.org/abs/{paper['id']}",
        "hf_url": f"https://huggingface.co/papers/{paper['id']}",
        "published_at": paper.get("publishedAt", None),
    }


def process_paper(paper):
    input_text = f"title: {paper['title']} | text: {paper['summary']}"
    logging.info("Generating embeddings for %s", paper["title"])
    embedding = get_embeddings(
        input_text, method=EMBEDDING_METHOD, structure="document"
    )
    return create_paper_info(paper, embedding)


def main():
    response = requests.get("https://huggingface.co/api/daily_papers", timeout=15)
    response.raise_for_status()
    data = response.json()

    incoming_ids = [item["paper"]["id"] for item in data]

    existing_rows = (
        supabase.table("all_papers_db").select("id").in_("id", incoming_ids).execute()
    )
    existing_ids = {row["id"] for row in existing_rows.data}
    logging.info("Found %s existing papers.", len(existing_ids))

    new_papers = [
        item["paper"] for item in data if item["paper"]["id"] not in existing_ids
    ]

    with ThreadPoolExecutor(max_workers=3) as executor:
        papers = list(executor.map(process_paper, new_papers))

    if papers:
        supabase.table("all_papers_db").upsert(papers).execute()
        logging.info("Upserted %s new papers to db", len(papers))
        logging.info(
            "Run date=%s, found=%d existing=%d new=%d",
            datetime.utcnow().date(),
            len(incoming_ids),
            len(existing_ids),
            len(new_papers),
        )
    else:
        logging.info("No new papers to upsert")


if __name__ == "__main__":
    main()
