import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_top_k_docs(query_vector, vector_store, k=2):
    scores = []

    for doc in vector_store:
        score = cosine_similarity(query_vector, np.array(doc["embedding"]))
        scores.append((score, doc))

    scores.sort(key=lambda x: x[0], reverse=True)

    top_docs = [item[1] for item in scores[:k]]
    return top_docs