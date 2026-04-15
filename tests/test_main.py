test_queries = (
    # --- LEVEL 1: Exact / Keyword Queries (Easy) ---
    # Tests if the pipeline can handle direct vocabulary overlap
    ("SCOPE: Signal-Calibrated On-Policy Distillation Enhancement", "2604.10688"),
    ("BMdataset LilyPond symbolic music", "2604.10628"),
    ("EquiformerV3 SE(3)-equivariant graph attention", "2604.09130"),
    ("DiningBench multi-view food dataset", "2604.10425"),
    ("CodeTracer architecture for agent states", "2604.11641"),
    # --- LEVEL 2: Conversational / Problem-Solution Queries (Medium) ---
    # Tests how well the embeddings map a user's "problem" to the paper's "solution"
    (
        "My LLM agent keeps forgetting who it is and mimics the user over long chats. How do I fix this?",
        "2604.09212",
    ),  # SPASM
    (
        "I need a way to track data lineage and see where my post-training dataset came from.",
        "2604.10480",
    ),  # Tracing the Roots
    (
        "Are there any benchmarks that test if LLMs can actually predict real-world chemistry and biology experiments?",
        "2604.10718",
    ),  # SciPredict
    (
        "I want to speed up my diffusion model by replacing it with a smaller model during some of the denoising steps.",
        "2604.02340",
    ),  # Not All Denoising Steps Are Equal
    (
        "How can I compress my LLM to 2-bit precision using additive quantization and fix the initialization bottlenecks?",
        "2604.08118",
    ),  # Initialisation Determines the Basin
    (
        "I need to evaluate my digital agent on tasks that require vision, search, and coding all at once.",
        "2604.11201",
    ),  # CocoaBench
    # --- LEVEL 3: Vague / Conceptual Queries (Hard) ---
    # Tests true semantic mapping without relying on the paper's specific jargon
    (
        "Using video game physics engines to teach AI how to solve science Olympiad problems.",
        "2604.11805",
    ),  # Solving Physics Olympiad
    (
        "That paper about how vision-language models completely fail when you rotate or scale an image.",
        "2604.01848",
    ),  # Semantic Richness or Geometric Reasoning
    (
        "Using an attacker-defender setup to teach language models how to manipulate beliefs and understand theory of mind.",
        "2604.11666",
    ),  # Playing Along
    (
        "A framework for software engineering agents that uses a sliding window to compress history so it doesn't forget the context.",
        "2604.11716",
    ),  # SWE-AGILE
    (
        "How human babies learn about the physical world so efficiently compared to AI.",
        "2604.10333",
    ),  # Zero-shot World Models
    (
        "Hacking distributed pipeline training by injecting a trigger word.",
        "2604.02372",
    ),  # Backdoor Attacks on Decentralised Post-Training
    # --- LEVEL 4: Highly Specific Niche & Cross-Disciplinary (Stress Tests) ---
    # Tests if the pipeline can pull up dense, specialized topics from a crowded vector space
    (
        "Applying Peircean semiotic theory to evaluate human-AI interaction in generative art.",
        "2604.08641",
    ),  # SemJudge
    (
        "Addressing the issue where transformers focus too much on specific, uninformative tokens.",
        "2604.10098",
    ),  # Attention Sink in Transformers
    (
        "Generating text-to-audio-video and testing the gaps in musical pitch control.",
        "2604.08540",
    ),  # AVGen-Bench
    (
        "Improving prompt optimization by filtering out bad user prompts to reduce response variance.",
        "2604.08801",
    ),  # p1
    (
        "Synthesizing human-object interaction videos conditioned on text, audio, and poses.",
        "2604.11804",
    ),  # OmniShow
)

import logging
import os

import pytest
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()


@pytest.fixture(scope="session")
def search_pipeline():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
    if not url or not key:
        logging.error("No supabase credentials")
        raise ValueError(
            "Missing SUPABASE_URL or SUPABASE_PUBLISHABLE_KEY in environment variables."
        )
    supabase = create_client(url, key)

    def run_search(query_text, top_k=3):
        import requests

        headers = {
            "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}",
        }

        payload = {"inputs": f"task: search result | query: {query_text}"}

        res = requests.post(
            "https://router.huggingface.co/hf-inference/models/google/embeddinggemma-300m/pipeline/feature-extraction",
            headers=headers,
            json=payload,
        )
        res.raise_for_status()
        query_vector = res.json()

        response = supabase.rpc(
            "match_documents",
            {
                "query_embedding": query_vector,
                "match_threshold": 0.35,
                "match_count": top_k,
            },
        ).execute()

        return response.data

    return run_search


@pytest.mark.parametrize("query, expected_id", test_queries)
def test_semantic_search_accuracy(query, expected_id, search_pipeline):
    results = search_pipeline(query, top_k=3)
    result_ids = [res["id"] for res in results] if results else []

    assert expected_id in result_ids, f"Expected {expected_id} but got {result_ids}"
