from fastapi import APIRouter, UploadFile, File
from backend.llm import generate_response
from backend.cognee import remember, recall

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "llm": "Groq",
        "api": "running"
    }


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "status": "success",
        "filename": file.filename,
        "message": "File received successfully. Ready for Cognee processing."
    }


# 🔥 MEMORY SEARCH (Cognee integrated)
@router.post("/memory/search")
def memory_search(query: dict):
    search_text = query.get("query", "")
    user_id = query.get("user_id", "default")

    results = recall(search_text, user_id)

    return {
        "query": search_text,
        "results": results,
        "message": "Fetched from Cognee"
    }


# 🔥 OPTIONAL (VERY IMPORTANT FOR HACKATHON DEMO)
@router.post("/memory/remember")
def memory_remember(payload: dict):
    text = payload.get("text", "")
    user_id = payload.get("user_id", "default")

    result = remember(text, user_id)

    return {
        "message": "Stored in Cognee",
        "result": result
    }