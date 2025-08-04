# agent/api/query.py
from fastapi import APIRouter
from agent.models.memory_models import MemoryQueryRequest
from agent.services.embedding_service import EmbeddingService
import logging

router = APIRouter()
embedding_service = EmbeddingService()

@router.post("/query")
def query_memory(req: MemoryQueryRequest):
    results = embedding_service.query_memory(req.user_id, req.query, req.limit)
    logging.info(f"[MEMORY][QUERY] {req.user_id} - {req.query} => {results}")
    return {"context": results, "user_id": req.user_id}