# tests/test_api.py
import os
from fastapi.testclient import TestClient

# Für Tests: Model-Laden überspringen (wir testen API-Form, nicht ML-Qualität)
os.environ["SKIP_MODEL_LOAD"] = "1"

from src.main import app  # noqa: E402


client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"


def test_docs_available():
    r = client.get("/docs")
    assert r.status_code == 200
