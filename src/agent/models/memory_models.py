# agent/models/memory_models.py
from pydantic import BaseModel

class MemorySaveRequest(BaseModel):
    user_id: str
    text: str
    type: str

class MemoryQueryRequest(BaseModel):
    user_id: str
    query: str
    limit: int = 5