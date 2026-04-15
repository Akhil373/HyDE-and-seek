import os
from pprint import pprint

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def query(payload):
    API_URL = "https://router.huggingface.co/hf-inference/models/google/embeddinggemma-300m/pipeline/feature-extraction"
    headers = {
        "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}",
    }

    vec = requests.post(API_URL, headers=headers, json=payload)
    return vec.json()


def openrouter():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY"),
    )

    # First API call with reasoning
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=[
            {"role": "user", "content": "How many r's are in the word 'strawberry'?"}
        ],
        extra_body={"reasoning": {"enabled": True}},
    )

    # Extract the assistant message with reasoning_details
    response = response.choices[0].message
    print(f"Reasoning: {response.reasoning_details}")
    print(f"Content: {response.content}")

    # Preserve the assistant message with reasoning_details
    messages = [
        {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
        {
            "role": "assistant",
            "content": response.content,
            "reasoning_details": response.reasoning_details,  # Pass back unmodified
        },
        {"role": "user", "content": "Are you sure? Think carefully."},
    ]

    # Second API call - model continues reasoning from where it left off
    response2 = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=messages,
        extra_body={"reasoning": {"enabled": True}},
    )
    print(f"Reasoning2: {response2.choices[0].message.reasoning}")
    print(f"Content2: {response2.choices[0].message.content}")


def groq():
    client = OpenAI(
        api_key=os.environ.get("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    input = f"""Write a short abstract for a research paper that would directly answer the following search query.
    Claim: Are there any benchmarks that test if LLMs can actually predict real-world chemistry and biology experiments?
    Passage:"""

    response = client.responses.create(
        model="openai/gpt-oss-120b", input=input, max_output_tokens=400
    )

    print(response.output_text)


def main():
    # output = query(
    #     {
    #         "inputs": "hello",
    #     }
    # )

    # print(output)
    # openrouter()
    groq()


main()
