from pydantic import BaseModel, Field

class MemoryInput(BaseModel):
    text: str = Field(..., description="The raw user statement or fact to store in memory.")

class QueryInput(BaseModel):
    query: str = Field(..., description="The question or search query to find relevant memories for.")

from typing import Optional

class ForgetInput(BaseModel):
    dataset: Optional[str] = Field(
        default="user_memory",
        description="Dataset to delete."
    )
    everything: bool = Field(
        default=False,
        description="Delete all memories."
    )

class ImproveInput(BaseModel):
    dataset: str = Field(
        default="user_memory",
        description="Dataset to improve."
    )