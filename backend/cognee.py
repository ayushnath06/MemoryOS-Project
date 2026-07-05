# backend/cognee.py

def remember(text: str, user_id: str):
    return {
        "status": "stored",
        "text": text,
        "user_id": user_id
    }


def recall(query: str, user_id: str):
    return {
        "query": query,
        "user_id": user_id,
        "results": []
    }