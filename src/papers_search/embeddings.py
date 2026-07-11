import logging
import os
from typing import Literal

import requests
from dotenv import load_dotenv

from papers_search.config import setup_logging, supabase_auth

load_dotenv()

setup_logging()
supabase = supabase_auth()

LOCAL_EMBEDDING_URL = os.getenv("LOCAL_EMBEDDING_URL")
HF_EMBEDDING_URL = os.getenv("HF_EMBEDDING_URL")
EMBEDDING_METHOD: Literal["hf", "local"] = "hf"


def get_embeddings(
    text,
    structure: Literal["document", "query"],
    method: Literal["hf", "local"] = "local",
) -> list[float]:
    """generating embeddings either HF or self-hosted model ran through sentence-transformer"""
    endpoints = {
        "local": LOCAL_EMBEDDING_URL,
        "hf": HF_EMBEDDING_URL,
    }
    endpoint = endpoints.get(method)
    if not endpoint:
        raise ValueError(f"Unsupported method: '{method}'. Expected 'hf' or 'local'.")

    if method == "local":
        payload = {"input": text, "task_type": structure}
        headers = {}
    else:
        # text is already suitably formatted in main for 'document'
        formatted_text = (
            text if structure == "document" else f"task: search result | query: {text}"
        )
        payload = (
            {"inputs": formatted_text} if method == "hf" else {"input": formatted_text}
        )

        headers = {
            "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}",
        }

    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        data = response.json()

        if method == "hf":
            return data
        else:
            if isinstance(data, dict) and "embeddings" in data:
                embeddings = data["embeddings"]
                return embeddings[0] if len(embeddings) == 1 else embeddings
            return data

    except Exception as e:
        logging.error(f"An error occurred when generating embeddings: {e}")
        raise
