# rag-assistant
# RAG Assistant (Retrieval Augmented Generation)

## Overview
This project is a simple implementation of a Retrieval Augmented Generation (RAG) system.
It allows users to ask questions, retrieves the most relevant information from stored documents using vector similarity search, and returns accurate responses through an API and a frontend interface.

## What This Project Does
- Converts documents into vector embeddings
- Stores embeddings in a JSON-based vector store
- Accepts user questions via API or frontend
- Finds the most relevant document using cosine similarity
- Returns the retrieved answer to the user

## Technologies Used
- Python
- FastAPI
- Sentence Transformers (all-MiniLM-L6-v2)
- NumPy
- HTML
- JavaScript

## Project Structure
rag-assistant/
│
├── backend/
│   ├── server.py
│   ├── ingest.py
│   ├── vector_store.json
│   ├── vector_math.py
│   └── .env
│
├── frontend/
│   ├── index.html
│   └── script.js
│
└── README.md

## Setup Instructions

### Clone Repository
git clone https://github.com/sai5230/rag-assistant.git
cd rag-assistant/backend

### Install Dependencies
pip install fastapi uvicorn sentence-transformers numpy

## Running the Project
uvicorn server:app --reload

Backend URL:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

## Frontend Usage
Open frontend/index.html in a browser.
Enter a question and click Send to view the response.

## API Example

POST /api/chat

Request:
{
  "message": "Explain this project",
  "sessionId": "frontend1"
}

Response:
{
  "answer": "This project is a Retrieval Augmented Generation (RAG) assistant...",
  "sessionId": "frontend1"
}

## Author
Kotta Sai Teja
Email: ksaiteja5230@gmail.com
GitHub: https://github.com/sai5230
#working demo rag assistant
link :http://127.0.0.1:5500/frontend/index.html
