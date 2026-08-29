from rag.vector_store import build_index, semantic_search


build_index()

print("\n=== Semantic Search ===")

results = semantic_search(
    "ایمیل درباره پرداخت و سفارش"
)

for document in results["documents"][0]:
    print("\n---")
    print(document)