import json
from pathlib import Path

import chromadb

from rag.embeddings import model


DATA_FILE = Path(__file__).parent.parent / "data" / "emails.json"

client = chromadb.PersistentClient(
    path=str(Path(__file__).parent / "chroma_db")
)

collection = client.get_or_create_collection(
    name="emails"
)


def build_index():

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        emails = json.load(f)

    documents = []
    ids = []

    for email in emails:

        text = (
            f"From: {email['from']}\n"
            f"Subject: {email['subject']}\n"
            f"Body: {email['body']}"
        )

        documents.append(text)
        ids.append(str(email["id"]))

    embeddings = model.encode(
        documents
    ).tolist()

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print(f"Indexed {len(documents)} emails.")


def semantic_search(query: str, n_results: int = 3):

    query_embedding = model.encode(
        [query]
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results