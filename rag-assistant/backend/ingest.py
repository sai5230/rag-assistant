from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "This project is a Retrieval Augmented Generation assistant.",
    "RAG combines vector search with language models.",
    "FastAPI is used to expose backend APIs."
]

vector_store = []

for i, doc in enumerate(documents):
    embedding = model.encode(doc).tolist()
    vector_store.append({
        "id": f"doc_{i}",
        "text": doc,
        "embedding": embedding
    })

with open("vector_store.json", "w", encoding="utf-8") as f:
    json.dump(vector_store, f, indent=2)

print("Documents ingested successfully.")