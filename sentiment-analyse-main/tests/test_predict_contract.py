import os

os.environ["SKIP_MODEL_LOAD"] = "1"

from fastapi.testclient import TestClient
import src.main as main


class DummyModel:
    def predict(self, X):
        t = X[0].lower()
        return [1] if ("good" in t or "great" in t or "gut" in t) else [0]

    def predict_proba(self, X):
        t = X[0].lower()
        return [[0.05, 0.95]] if ("good" in t or "great" in t or "gut" in t) else [[0.90, 0.10]]


# Dummy Modelle setzen, damit die Endpoints nicht mit "Modell fehlt" abbrechen
main.model_de = DummyModel()
main.model_en = DummyModel()
main.model_all = DummyModel()

client = TestClient(main.app)


def _assert_schema(data: dict):
    assert data["label"] in [0, 1]
    assert data["sentiment"] in ["positive", "negative"]
    assert 0.0 <= data["prob_positive"] <= 1.0
    assert 0.0 <= data["prob_negative"] <= 1.0
    # optional, nice to have
    assert abs((data["prob_positive"] + data["prob_negative"]) - 1.0) < 1e-6


def test_predict_en_schema():
    r = client.post("/predict/en", json={"text": "This is good"})
    assert r.status_code == 200
    _assert_schema(r.json())


def test_predict_de_schema():
    r = client.post("/predict/de", json={"text": "Das ist gut"})
    assert r.status_code == 200
    _assert_schema(r.json())


def test_predict_auto_schema():
    r = client.post("/predict", json={"text": "This is good"})
    assert r.status_code == 200
    _assert_schema(r.json())


def test_empty_text_rejected():
    r = client.post("/predict/en", json={"text": ""})
    assert r.status_code in [400, 422]
