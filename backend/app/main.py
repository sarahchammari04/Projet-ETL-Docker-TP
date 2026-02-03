from fastapi import FastAPI, Query
from .db import init_db, get_conn
from .etl import run_etl
from .etl import preview as etl_preview

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

@app.get("/etl/preview")
def etl_preview_route(n: int = Query(3, ge=1, le=10)):
    return etl_preview(n)


@app.get("/etl/runs")
def etl_runs():
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM etl_runs ORDER BY id DESC LIMIT 20"
        ).fetchall()
    return [dict(r) for r in rows]