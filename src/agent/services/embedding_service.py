# agent/services/embedding_service.py
from langchain.vectorstores import Qdrant
from agent.config.vector_store import vectorstore

class EmbeddingService:
    def save_memory(self, text: str, metadata: dict):
        vectorstore.add_texts([text], metadatas=[metadata])

    def query_memory(self, user_id: str, query: str, limit: int = 5, filters: dict = None):
        base_filter = {"user_id": user_id}
        if filters:
            base_filter.update(filters)

        results = vectorstore.similarity_search(
            query=query,
            k=limit,
            filter=base_filter
        )
        return [doc.page_content for doc in results]