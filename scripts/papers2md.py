import papers_search
import papers_search
import json
from pathlib import Path
from papers_search.config import supabase_auth

PATH = "./data/papers.json"


def json2md():
    with open(PATH, "w", encoding="utf-8") as out:
        for json_file in Path("./data/").glob("papers_fetch_*.json"):
            print("processing:", json_file)
            with open(json_file, "r", encoding="utf-8") as f:
                papers = json.load(f)

            for item in papers:
                paper = item["paper"]

                out.write(f"ID: {paper['id']}\n\n")
                out.write(f"# {paper['title']}\n\n")
                out.write(f"Abstract:\n{paper['summary']}\n\n")
                if paper.get("ai_summary"):
                    out.write(f"AI Summary:\n{paper['ai_summary']}\n\n")

                if paper.get("ai_keywords"):
                    out.write("Keywords:\n")
                    for keyword in paper["ai_keywords"]:
                        out.write(f"- {keyword}\n")

                out.write("\n---\n\n")


def db2md():
    supabase = supabase_auth()
    response = (
        supabase.table("all_papers_db").select("id", "title", "abstract").execute()
    )
    with open(PATH, "w", encoding="utf-8") as out:
        for i, paper in enumerate(response.data):
            out.write(f"ID: {paper['id']}\n\n")
            out.write(f"{paper['title']}\n\n")
            out.write(f"Abstract:\n{paper['abstract']}\n\n")
            out.write("\n---\n\n")
            print(f"written {i + 1} / {len(response.data)}\r", end="")


def combine_json():
    tmp = {}
    for json_file in Path("./data/").glob("papers_fetch_*.json"):
        print(f"processing: {json_file}\r", end="")
        with open(json_file, "r", encoding="utf-8") as f:
            papers = json.load(f)

        for item in papers:
            paper = item["paper"]
            tmp1 = {"title": paper["title"], "abstract": paper["summary"]}
            tmp[paper["id"]] = tmp1

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(tmp, f, indent=4, ensure_ascii=False)


combine_json()
