# agent/api/memory.py
from fastapi import APIRouter
from agent.models.memory_models import MemorySaveRequest
from agent.services.embedding_service import EmbeddingService
from datetime import datetime
import logging

router = APIRouter()
embedding_service = EmbeddingService()

@router.post("/save")
def save_memory(req: MemorySaveRequest):
    metadata = {
        "user_id": req.user_id,
        "type": req.type,
        "createdAt": datetime.utcnow().isoformat()
    }
    embedding_service.save_memory(req.text, metadata)
    logging.info(f"[MEMORY][SAVE] {req.user_id} - {req.text}")
    return {"status": "saved", "user_id": req.user_id}