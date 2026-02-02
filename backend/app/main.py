from fastapi import FastAPI
from .db import init_db, get_conn
from .etl import run_etl

app = FastAPI(title="ETL API")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/etl/run")
def etl():
    return run_etl()

@app.get("/posts")
def posts(limit: int = 10):
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM posts LIMIT ?", (limit,)).fetchall()
    return [dict(r) for r in rows]
