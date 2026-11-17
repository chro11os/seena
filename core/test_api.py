from fastapi.testclient import TestClient
from core import json_format as jf
from server import app

client = TestClient(app)


def test_delete_endpoint_removes_session_from_history():
    jf.add_turn("hi", "hello", "a")
    jf.add_turn("bye", "goodbye", "b")

    res = client.delete("/api/sessions/a")

    assert res.status_code == 200
    assert {m["session"] for m in client.get("/api/history").json()} == {"b"}
