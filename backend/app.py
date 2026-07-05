from fastapi import FastAPI
from pydantic import BaseModel
from backend.llm import generate_response
from backend.routes import router

app = FastAPI()


app.include_router(router)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: list[Message]


@app.get("/v1/models")
def models():
    return {
        "object": "list",
        "data": [
            {
                "id": "llama-3.3-70b-versatile",
                "object": "model"
            }
        ]
    }


@app.post("/v1/chat/completions")
def chat(req: ChatRequest):

    user_message = req.messages[-1].content

    answer = generate_response(user_message)

    return {
        "id": "chatcmpl-001",
        "object": "chat.completion",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": answer
                },
                "finish_reason": "stop"
            }
        ]
    }









