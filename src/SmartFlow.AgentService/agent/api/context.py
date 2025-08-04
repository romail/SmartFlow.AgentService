from fastapi import APIRouter
from pydantic import BaseModel
from agent.services.embedding_service import EmbeddingService
import logging

router = APIRouter()
embedding_service = EmbeddingService()

class ContextRequest(BaseModel):
    user_id: str
    input: str
    language: str = "en"

@router.post("/context")
def build_context(req: ContextRequest):
    results = embedding_service.query_memory(
        user_id=req.user_id,
        query=req.input,
        limit=5,
        filters={"language": req.language}
    )

    logging.info(f"[CONTEXT][BUILD] {req.user_id} - {req.input} => {len(results)} matches")
    return "\n".join(results)
