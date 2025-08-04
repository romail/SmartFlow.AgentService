import os
from dotenv import load_dotenv

from transformers import pipeline
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# Load environment variables from .env file
load_dotenv()

# Environment config
QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "smartflow_memory")
VECTOR_SIZE = int(os.getenv("VECTOR_SIZE", "512"))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/distiluse-base-multilingual-cased-v2")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "tiiuae/falcon-7b-instruct")
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "512"))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))

# Initialize embedding model
embedding_fn = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# Initialize Qdrant client
qdrant_client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

# Create collection if it does not exist
if COLLECTION_NAME not in [c.name for c in qdrant_client.get_collections().collections]:
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
    )

# Setup LangChain-compatible vector store
vectorstore = Qdrant(
    client=qdrant_client,
    collection_name=COLLECTION_NAME,
    embeddings=embedding_fn
)

retriever = vectorstore.as_retriever()

# Setup local LLM using HuggingFace pipeline
local_pipeline = pipeline(
    task="text-generation",
    model=LLM_MODEL_NAME,
    max_new_tokens=LLM_MAX_TOKENS,
    temperature=LLM_TEMPERATURE,
    repetition_penalty=1.1,
    do_sample=True,
    return_full_text=False
)

llm = HuggingFacePipeline(pipeline=local_pipeline)

# Final Retrieval-Augmented Generation (RAG) chain
agent_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)
