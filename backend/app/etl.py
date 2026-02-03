import requests
import datetime as dt
from .db import get_conn

API_URL = "https://jsonplaceholder.typicode.com/posts"

def extract():
    r = requests.get(API_URL, timeout=10)
    r.raise_for_status()
    return r.json()

def transform(raw):
    now = dt.datetime.utcnow().isoformat()
    return [{
        "id": int(p["id"]),
        "user_id": int(p["userId"]),
        "title": str(p["title"]).strip(),
        "body": str(p["body"]).strip(),
        "loaded_at": now
    } for p in raw]

def load(rows):
    with get_conn() as conn:
        conn.executemany("""
        INSERT OR REPLACE INTO posts (id, user_id, title, body, loaded_at)
        VALUES (:id, :user_id, :title, :body, :loaded_at)
        """, rows)
        conn.commit()
    with get_conn() as conn:
        conn.execute(
        "INSERT INTO etl_runs (ran_at, rows_loaded) VALUES (?, ?)",
        (dt.datetime.utcnow().isoformat(), len(rows)))
        conn.commit()

def run_etl():
    raw = extract()
    rows = transform(raw)
    load(rows)
    return {"rows_loaded": len(rows)}

def preview(n=3):
    raw = extract()[:n]
    transformed = transform(raw)
    return {"raw": raw, "transformed": transformed}