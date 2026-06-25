from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.redis_client import redis_client

app = FastAPI(title="Model Registry")


@app.get("/")
def root():
    return {"service": "model-registry", "status": "ok"}


@app.get("/health")
def health():
    checks = {}
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        checks["postgres"] = "ok"
    except Exception as e:
        checks["postgres"] = f"error: {e}"

    try:
        redis_client.ping()
        checks["redis"] = "ok"
    except Exception as e:
        checks["redis"] = f"error: {e}"

    return checks
