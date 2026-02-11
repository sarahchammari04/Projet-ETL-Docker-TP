from app.etl import transform

def test_transform_adds_loaded_at_and_cleans_fields():
    raw = [
        {"id": "1", "userId": "2", "title": "  Hello  ", "body": "  World  "}
    ]
    rows = transform(raw)
    assert len(rows) == 1
    r = rows[0]
    assert r["id"] == 1
    assert r["user_id"] == 2
    assert r["title"] == "Hello"
    assert r["body"] == "World"
    assert "loaded_at" in r and isinstance(r["loaded_at"], str)
