import json
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from typing import TypedDict

import requests
from dotenv import load_dotenv

from papers_search.config import setup_logging
from papers_search.embeddings import EMBEDDING_METHOD, get_embeddings, logging, supabase

load_dotenv()
setup_logging()


class PaperInfo(TypedDict):
    id: str
    title: str
    abstract: str
    embedding: list[float]
    arxiv_url: str
    hf_url: str
    published_at: str | None


def get_paper(paper_info: PaperInfo):
    """fetching paper info from arxiv"""

    paper_url = f"https://arxiv.org/pdf/{paper_info['id']}"
    paper_name = f"{paper_info['title']}.pdf"

    if not os.path.isfile(paper_name) and os.path.isdir("./papers/"):
        try:
            response = requests.get(paper_url, stream=True, timeout=30)
            if response.status_code == 200:
                downloaded = 0

                print(f"Downloading paper: {paper_url}")

                with open(f"papers/{paper_name}", "wb") as f:
                    for chunk in response.iter_content(chunk_size=100_000):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)

                logging.info("Downloaded paper: %s", paper_name)
        except Exception:
            logging.critical("An error has occured when downloading paper from hf")
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
    """
    tasks done:
    1. fetch papers from hf api
    2. filter out existing papers from db
    3. generate embeddings and upsert new papers
    """
    t = date.today()
    d, m = f"{t.day:02d}", f"{t.month:02d}"

    output_path = f"./data/papers_fetch_{m}_{d}.json"
    if not os.path.isfile(output_path):
        response = requests.get("https://huggingface.co/api/daily_papers", timeout=15)
        response.raise_for_status()
        data = response.json()
    else:
        logging.info("papers metadata already exists!")
        with open(output_path, "r", encoding="utf-8") as f:
            response = json.load(f)
        data = response

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

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"written into {output_path}; size: {len(data)}")

    except Exception:
        logging.error("An error has occured when writing into %s", output_path)
        raise

    if papers:
        supabase.table("all_papers_db").upsert(papers).execute()
        logging.info("Upserted %s new papers to db", len(papers))
    else:
        logging.info("No new papers to upsert")


if __name__ == "__main__":
    main()
