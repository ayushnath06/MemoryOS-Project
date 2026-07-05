from fastapi import APIRouter, UploadFile, File
from backend.llm import generate_response
from backend.services.cognee_service import (
    store_memory,
    retrieve_memory,
    forget_memory,
    improve_memory,
)

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
async def memory_search(query: dict):
    search_text = query.get("query", "")

    result = await retrieve_memory(search_text)

    return result


@router.post("/memory/remember")
async def memory_remember(payload: dict):
    text = payload.get("text", "")

    result = await store_memory(text)

    return result

@router.delete("/memory/forget")
async def memory_forget():
    return await forget_memory()

@router.post("/memory/improve")
async def memory_improve():
    return await improve_memory()