import json
from pathlib import Path

from rag.vector_store import semantic_search


EMAILS_FILE = Path(__file__).parent.parent / "data" / "emails.json"


def load_emails():
    with open(EMAILS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def search_emails(query: str):
    emails = load_emails()

    query = query.lower()
    results = []

    for email in emails:
        text = (
            email["subject"]
            + " "
            + email["body"]
            + " "
            + email["from"]
        ).lower()

        if query in text:
            results.append(email)

    return results


def search_emails_semantic(query: str, n_results: int = 3):
    results = semantic_search(query, n_results)

    documents = results.get("documents", [[]])[0]

    return documents


def get_email(email_id: int):
    emails = load_emails()

    for email in emails:
        if email["id"] == email_id:
            return email

    return None