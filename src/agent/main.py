from fastapi import FastAPI
from agent.api import memory, query, context
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="SmartFlow AgentService")

app.include_router(memory.router, prefix="/memory")
app.include_router(query.router, prefix="/query")
app.include_router(context.router, prefix="/context")

