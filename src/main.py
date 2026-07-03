# src/main.py
from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

import joblib
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

MODEL_DE = Path("model/sentiment_de.joblib")
MODEL_EN = Path("model/sentiment_en.joblib")
MODEL_ALL = Path("model/sentiment_all.joblib")

app = FastAPI(title="Sentiment Analyse API", version="1.0")


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text, der bewertet werden soll")


class PredictResponse(BaseModel):
    label: int
    sentiment: Literal["positive", "negative"]
    prob_positive: float
    prob_negative: float


model_de = None
model_en = None
model_all = None


def _load_models() -> None:
    global model_de, model_en, model_all

    # Für Tests/CI: kein echtes Laden nötig
    if os.getenv("SKIP_MODEL_LOAD") == "1":
        return

    if MODEL_DE.exists():
        model_de = joblib.load(MODEL_DE)
    if MODEL_EN.exists():
        model_en = joblib.load(MODEL_EN)
    if MODEL_ALL.exists():
        model_all = joblib.load(MODEL_ALL)

    if model_de is None and model_en is None and model_all is None:
        raise RuntimeError(
            "Kein Modell gefunden. Bitte erst src/train_model.py ausführen. "
            "Erwartet: model/sentiment_de.joblib oder model/sentiment_en.joblib oder model/sentiment_all.joblib"
        )


@app.on_event("startup")
def startup_event():
    _load_models()


def _predict_with(m, text: str) -> PredictResponse:
    text = text.strip()
    pred = int(m.predict([text])[0])

    proba = m.predict_proba([text])[0]

    # Klassenreihenfolge sicher ermitteln
    classes = None
    if hasattr(m, "classes_"):
        classes = list(m.classes_)
    elif hasattr(m, "named_steps"):
        for step in reversed(list(m.named_steps.values())):
            if hasattr(step, "classes_"):
                classes = list(step.classes_)
                break

    if classes and len(classes) == len(proba):
        prob_map = {int(c): float(p) for c, p in zip(classes, proba)}
        prob_negative = prob_map.get(0, float(proba[0]))
        prob_positive = prob_map.get(1, float(proba[1]))
    else:
        prob_negative = float(proba[0])
        prob_positive = float(proba[1])

    sentiment = "positive" if pred == 1 else "negative"
    return PredictResponse(
        label=pred,
        sentiment=sentiment,
        prob_positive=prob_positive,
        prob_negative=prob_negative,
    )



@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(
        """
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Sentiment Detection – DE vs EN vs Combined</title>
  <style>
    body{
      margin:0;
      font-family:system-ui,Segoe UI,Roboto,Arial;
      background:#0b1220;
      color:#e6edf7
    }

    /* Breiter + mittig */
    .wrap{
      max-width:1400px;
      margin:40px auto;
      padding:0 16px;
    }

    h1{margin:0 0 8px 0;font-size:30px}
    .sub{opacity:.85;margin-bottom:24px;line-height:1.4;font-size:14px}

    /* Grid sauber ausgerichtet */
    .grid{
      display:grid;
      grid-template-columns:1fr 1fr 1fr;
      gap:18px;
      align-items:start;
    }

    /* Cards größer */
    .card{
      background:linear-gradient(180deg,#0f1a33,#0b1220);
      border:1px solid #203056;
      border-radius:18px;
      padding:22px;
      box-shadow:0 10px 25px rgba(0,0,0,.25)
    }

    .card h2{margin:0 0 10px 0;font-size:19px}

    /* Textfeld größer, gleichmäßig */
    textarea{
      width:100%;
      min-height:210px;
      border-radius:14px;
      border:1px solid #2a3b68;
      background:#0a1020;
      color:#e6edf7;
      padding:12px;
      resize:vertical;
      box-sizing:border-box;
    }

    button{
      margin-top:12px;
      width:100%;
      background:#1b2b52;
      border:1px solid #2a3b68;
      color:#e6edf7;
      padding:12px 14px;
      border-radius:14px;
      cursor:pointer;
      font-weight:700;
    }
    button:hover{filter:brightness(1.1)}

    .res{
      margin-top:14px;
      padding:12px 12px;
      border-radius:14px;
      border:1px solid #2a3b68;
      background:#081022
    }

    .pill{
      display:inline-block;
      padding:5px 10px;
      border-radius:999px;
      border:1px solid #2a3b68;
      margin-right:8px
    }
    .ok{border-color:#2bd576}
    .bad{border-color:#ff5a7a}
    .nums{opacity:.9;margin-top:8px;font-size:13px}
    .hint{opacity:.75;font-size:12px;margin-top:8px}
    code{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace}

    /* Mobil: untereinander */
    @media(max-width:1100px){
      .grid{grid-template-columns:1fr}
      button{width:auto}
    }
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Sentiment Detection – Deutsch vs. Englisch vs. Combined</h1>
    <div class="sub">
      Drei Varianten: <b>DE-only</b> (nur deutsche Trainingsdaten), <b>EN-only</b> (nur englische Trainingsdaten) und
      <b>Combined</b> (DE+EN zusammen als Fallback). Ergebnis = Label + Wahrscheinlichkeiten.
    </div>

    <div class="grid">
      <div class="card">
        <h2>Deutsch (DE-only)</h2>
        <textarea id="txtDe">Das Produkt ist sehr gut</textarea>
        <button onclick="run('/predict/de','txtDe','resDe')">Analysieren (DE)</button>
        <div class="res" id="resDe">–</div>
        <div class="hint">Endpoint: <code>/predict/de</code></div>
      </div>

      <div class="card">
        <h2>English (EN-only)</h2>
        <textarea id="txtEn">The product is very good</textarea>
        <button onclick="run('/predict/en','txtEn','resEn')">Analyze (EN)</button>
        <div class="res" id="resEn">–</div>
        <div class="hint">Endpoint: <code>/predict/en</code></div>
      </div>

      <div class="card">
        <h2>Combined (DE+EN)</h2>
        <textarea id="txtAll">I like den Film, aber das Ende war schlecht.</textarea>
        <button onclick="run('/predict','txtAll','resAll')">Analysieren (Combined)</button>
        <div class="res" id="resAll">–</div>
        <div class="hint">Endpoint: <code>/predict</code> (Fallback)</div>
      </div>
    </div>

    <div class="sub" style="margin-top:18px">
      Swagger: <a href="/docs" style="color:#9cc2ff">/docs</a>
    </div>
  </div>

<script>
async function run(endpoint, textId, resId){
  const text = document.getElementById(textId).value;
  const box  = document.getElementById(resId);
  box.textContent = "Lade…";

  const r = await fetch(endpoint, {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({text})
  });

  if(!r.ok){
    const t = await r.text();
    box.textContent = "Fehler: " + r.status + " " + t;
    return;
  }

  const data = await r.json();
  const good = data.sentiment === "positive";
  box.innerHTML = `
    <span class="pill ${good?'ok':'bad'}">Label: ${data.label}</span>
    <span class="pill ${good?'ok':'bad'}">Sentiment: ${data.sentiment}</span>
    <div class="nums">P(pos): ${Number(data.prob_positive).toFixed(3)} | P(neg): ${Number(data.prob_negative).toFixed(3)}</div>
  `;
}
</script>
</body>
</html>
        """
    )


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_de_loaded": model_de is not None,
        "model_en_loaded": model_en is not None,
        "model_all_loaded": model_all is not None,
    }


@app.post("/predict/de", response_model=PredictResponse)
def predict_de(req: PredictRequest):
    if model_de is None:
        raise RuntimeError("DE-Modell fehlt. Bitte src/train_model.py ausführen (sentiment_de.joblib).")
    return _predict_with(model_de, req.text)


@app.post("/predict/en", response_model=PredictResponse)
def predict_en(req: PredictRequest):
    if model_en is None:
        raise RuntimeError("EN-Modell fehlt. Bitte src/train_model.py ausführen (sentiment_en.joblib).")
    return _predict_with(model_en, req.text)


@app.post("/predict", response_model=PredictResponse)
def predict_auto(req: PredictRequest):
    if model_all is None:
        raise RuntimeError("Combined-Modell fehlt. Bitte src/train_model.py ausführen (sentiment_all.joblib).")
    return _predict_with(model_all, req.text)
