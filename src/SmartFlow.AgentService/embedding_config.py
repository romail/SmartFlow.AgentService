import os
from langchain_qdrant import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "smartflow_memory")
VECTOR_SIZE = int(os.getenv("VECTOR_SIZE", "512"))
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
MODEL_NAME = os.getenv("EMBEDDING_MODEL", "sentence-transformers/distiluse-base-multilingual-cased-v2")

def get_vectorstore():
    print(f"📦 Initializing vectorstore with model: {MODEL_NAME}, Qdrant: {QDRANT_HOST}:{QDRANT_PORT}, collection: {COLLECTION_NAME}")

    embedding_fn = HuggingFaceEmbeddings(model_name=MODEL_NAME)

    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

    if not client.collection_exists(collection_name=COLLECTION_NAME):
        print(f"⚠️ Collection '{COLLECTION_NAME}' not found. Creating...")
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
        )
    else:
        print(f"✅ Using existing collection: {COLLECTION_NAME}")

    return Qdrant(
        client=client,
        collection_name=COLLECTION_NAME,
        embeddings=embedding_fn
    )
