import json
import logging
import os
from pprint import pprint
from typing import Literal

import numpy as np
import requests
from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
if not url or not key:
    logging.critical("Supabase credentials not found!")
    raise ValueError()

logging.info(f"Supabase URL: {url[:10]}, Key: {key[:10]}...")
supabase: Client = create_client(url, key)

embedding_method: Literal["hf", "local"] = "hf"


def get_paper(paper_info):
    paper_url = f"https://arxiv.org/pdf/{paper_info['id']}"
    paper_name = f"{paper_info['title']}.pdf"

    if not os.path.isfile(paper_name) and os.path.isdir("./papers/"):
        try:
            response = requests.get(paper_url, stream=True, timeout=30)
            if response.status_code == 200:
                # total_size = int(response.headers.get("content-length", 0))
                downloaded = 0

                print(f"Downloading paper: {paper_url}")

                with open(f"papers/{paper_name}", "wb") as f:
                    for chunk in response.iter_content(chunk_size=100_000):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)

                            # if total_size:
                            #     percent = (downloaded / total_size) * 100
                            #     print(f"{paper_url}: {percent:.1f}%", end="\r")

                logging.info(f"Downloaded paper: {paper_name}")
        except Exception as e:
            logging.critical("An error has occured when downloading paper from hf")
            raise


def store_db(paper_info):
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
    if not url or not key:
        logging.critical("Supabase credentials not found!")
        raise ValueError()

    logging.info(f"Supabase URL: {url}, Key: {key[:10]}...")
    supabase: Client = create_client(url, key)
    try:
        _ = (
            supabase.table("all_papers_db")
            .upsert(
                {
                    "id": paper_info["id"],
                    "title": paper_info["title"],
                    "abstract": paper_info["abstract"],
                    "embeddings": paper_info["embedding"],
                },
                on_conflict="id",
                ignore_duplicates=True,
            )
            .execute()
        )
    except Exception as e:
        logging.exception("Failed to fetch papers info from DB")
        raise


def get_embeddings(text, method: Literal["hf", "local"] = "hf"):
    url = (
        "http://localhost:8080/embedding"
        if method == "local"
        else "https://router.huggingface.co/hf-inference/models/google/embeddinggemma-300m/pipeline/feature-extraction"
    )

    payload = {"inputs": f"task: search result | query: {text}"}
    headers = {
        "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}",
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        # embedding_arr = np.array(data)
        # import math

        # print(f"Magnitude: {math.sqrt(sum(x**2 for x in data))}")
        # print(f"Full Array Shape: {embedding_arr.shape}")
        # print(f"Total Elements: {embedding_arr.size}")
        # print(data[0]["embedding"])
        return data if method == "hf" else data[0]["embedding"][0]

    except Exception as e:
        logging.error("An error occurred when generating embeddings")
        raise


def groq(text):
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

    # print(chat_completion.choices[0].message.content)

    return chat_completion.choices[0].message.content


def testing():
    while True:
        print("-" * 50)
        query: str = input("Type your query: ")
        if query == "/exit":
            break

        query_llm = groq(query)
        print(query_llm)
        query_embedding = get_embeddings(query_llm, method=embedding_method)

        try:
            response = supabase.rpc(
                "match_documents",
                {
                    "query_embedding": query_embedding,
                    "match_threshold": 0.2,
                    "match_count": 5,
                },
            ).execute()

            for row in response.data:
                row.pop("embedding", None)
            pprint(response.data)

        except Exception as e:
            logging.critical("An error occurred during semantic search")
            raise


def main():
    output_path = "./papers_fetch.json"
    if not os.path.isfile(output_path):
        response = requests.get("https://huggingface.co/api/daily_papers", timeout=15)
        response.raise_for_status()
        data = response.json()
    else:
        with open(output_path, "r", encoding="utf-8") as f:
            response = json.load(f)
        data = response

    incoming_ids = [item["paper"]["id"] for item in data]

    existing_rows = (
        supabase.table("all_papers_db").select("id").in_("id", incoming_ids).execute()
    )
    existing_ids = {row["id"] for row in existing_rows.data}
    logging.info(f"Found {len(existing_ids)} existing papers.")

    papers = []

    for item in data:
        paper = item["paper"]
        paper_id = paper["id"]
        if paper_id in existing_ids:
            continue

        input_text = f"title: {paper['title']} | text: {paper['summary']}"
        embedding = get_embeddings(input_text, method=embedding_method)
        logging.info(f"Generating embeddings for {paper['title']}")
        papers.append(
            {
                "id": paper["id"],
                "title": paper["title"],
                "abstract": paper["summary"],
                "embedding": embedding,
                "arxiv_url": f"https://arxiv.org/abs/{paper['id']}",
                "hf_url": f"https://huggingface.co/papers/{paper['id']}",
                "published_at": paper.get("publishedAt", None),
            }
        )

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"written into {output_path}; size: {len(data)}")

    except Exception as e:
        logging.error(f"An error has occured when writing into {output_path}")
        raise

    if papers:
        supabase.table("all_papers_db").upsert(papers).execute()
        logging.info(f"Upserted {len(papers)} new papers to db")
    else:
        logging.info("No new papers to upsert")


if __name__ == "__main__":
    main()
    # testing()
