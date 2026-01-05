from fastapi import FastAPI

app = FastAPI(
    title="Agentic Helpdesk API",
    description="Backend API for autonomous ticket resolution system",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
