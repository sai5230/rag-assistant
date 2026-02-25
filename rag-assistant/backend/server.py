from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import json
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

VECTOR_FILE = "vector_store.json"

# Load vector store
if os.path.exists(VECTOR_FILE):
    with open(VECTOR_FILE, "r", encoding="utf-8") as f:
        vector_store = json.load(f)
else:
    vector_store = []

class ChatRequest(BaseModel):
    message: str
    sessionId: str | None = None

@app.post("/api/chat")
def chat(req: ChatRequest):
    if not vector_store:
        return {
            "answer": "No documents ingested yet.",
            "sessionId": req.sessionId
        }

    query_embedding = model.encode(req.message)

    best_score = -1
    best_text = ""

    for item in vector_store:
        score = np.dot(query_embedding, item["embedding"])
        if score > best_score:
            best_score = score
            best_text = item.get("text", "")

    return {
        "answer": best_text,
        "sessionId": req.sessionId
    }