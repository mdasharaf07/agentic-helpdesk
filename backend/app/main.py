from fastapi import FastAPI
from app.db.init_db import create_tables

app = FastAPI(
    title="Agentic Helpdesk API",
    description="Backend API for autonomous ticket resolution system",
    version="1.0.0"
)

# Create tables on startup
@app.on_event("startup")
async def startup_event():
    create_tables()

@app.get("/health")
async def health_check():
    return {"status": "ok"}
