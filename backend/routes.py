from fastapi import APIRouter, UploadFile, File
from backend.llm import generate_response

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


@router.post("/memory/search")
def memory_search(query: dict):
    search_text = query.get("query", "")

    return {
        "query": search_text,
        "results": [],
        "message": "Memory search endpoint ready. Cognee integration pending."
    }























