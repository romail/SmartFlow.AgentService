# 🧠 SmartFlow.AgentService

This is the AI microservice for SmartFlow — a FastAPI-based application powered by LangChain, Qdrant, and SentenceTransformers. It enables task generation, prompt processing, and Retrieval-Augmented Generation (RAG) capabilities.

---

## 📦 Tech Stack

- **FastAPI** — Lightweight Python web framework
- **LangChain** — LLM orchestration and RAG pipelines
- **Qdrant** — Vector database for memory and similarity search
- **sentence-transformers** — Text embedding generation
- **Docker** — Containerized deployment
- **Render** — Cloud hosting & deployment

---

## 🚀 Local Development (Docker Compose)

Start the agent and Qdrant services locally:

```bash
docker-compose up --build
```

- Agent: [http://localhost:8000](http://localhost:8000)  
- Qdrant: [http://localhost:6333](http://localhost:6333)

---

## ⚙️ Environment Variables (`.env`)

Example:

```env
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION=smartflow_memory
VECTOR_SIZE=512
EMBEDDING_MODEL=sentence-transformers/distiluse-base-multilingual-cased-v2
```

---

## 📂 Project Structure

```
src/
├── agent/                  # FastAPI route definitions
├── embedding.py           # Embedding generation logic
├── memory.py              # Qdrant memory functions
├── vector_store.py        # LangChain + Qdrant integration
├── query.py               # RAG queries
├── request_models.py      # Pydantic schemas
├── http_tests.http        # Example HTTP requests
├── Dockerfile             # For containerized deployment
├── requirements.txt
├── docker-compose.yml
└── render.yaml
```

---

## ☁️ Deploying to Render

### 1. Deploy via Render Blueprint (`render.yaml`)

This repository includes a `render.yaml` file that automatically provisions:

- `smartflow-agent` — the FastAPI service
- `smartflow-qdrant` — a private Qdrant vector DB

To deploy:

1. Push this repository to GitHub
2. Connect it to [Render](https://render.com/)
3. Choose **"Deploy from Blueprint"**

### 2. After Deployment

- Agent will be available at:  
  `https://smartflow-agent.onrender.com`

- Qdrant will be accessible internally via:  
  `http://smartflow-qdrant:6333`

---

## 📮 API Endpoints (Examples)

```http
POST /generate-tasks
GET  /summary
```

You can test them using `http_tests.http` (e.g., in VS Code with REST Client extension).

---

## ✅ TODO

- [ ] Authentication support
- [ ] OpenAI / HuggingFace model switching
- [ ] GitHub Actions CI/CD
- [ ] Unit tests
- [ ] Logging and monitoring

---