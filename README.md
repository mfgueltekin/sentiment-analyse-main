# Sentiment Analyse API (DE/EN)

**Autor:** Mehmet Fatih Gültekin

**Thema:**  
Automatische Sentiment-Erkennung (positiv / negativ) für Texte in Deutsch und Englisch

---

## Projektbeschreibung

Hinweis: Die Modelle sind domänenspezifisch auf Filmrezensionen trainiert worden
und erzielen in diesem Kontext die besten Ergebnisse.

Dieses Projekt stellt eine **Sentiment-Analyse als REST-API** bereit.  
Für einen gegebenen Text gibt die API das erkannte Sentiment (**positive** oder **negative**) sowie zugehörige Wahrscheinlichkeiten zurück.

**Modellansatz:**  
- TF-IDF (Feature-Extraktion, 1–2-Gramme)  
- Logistische Regression (Klassifikation)

**Verfügbare Modelle:**  
- Deutsch (DE)  
- Englisch (EN)  
- Combined (DE + EN)

---

## Schnellstart (ohne Docker – empfohlen)

### 1) Umgebung anlegen & Abhängigkeiten installieren
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r docs/requirements.txt
2) API starten
python -m uvicorn src.main:app --host 127.0.0.1 --port 8000
3) Swagger / OpenAPI
Swagger UI: http://127.0.0.1:8000/docs

Health-Check: http://127.0.0.1:8000/health

API-Nutzung
Health
GET /health
Predict (Deutsch)
POST /predict/de
Content-Type: application/json

{"text": "Das ist gut"}
Predict (Englisch)
POST /predict/en
Content-Type: application/json

{"text": "This is good"}
Predict (Combined)
POST /predict
Content-Type: application/json

{"text": "Das ist gut"}
Beispiel-Response
{
  "label": 1,
  "sentiment": "positive",
  "prob_positive": 0.93,
  "prob_negative": 0.07
}
Tests
pytest -q
Testarten:

Health-Test (API verfügbar, Modellstatus)

Contract-Tests (Schema & Wahrscheinlichkeiten konsistent)

CI-sichere Tests:
In CI wird SKIP_MODEL_LOAD=1 gesetzt. Dummy-Modelle ermöglichen API-Tests ohne geladene Artefakte.

CI/CD (GitLab)
Die Pipeline besteht aus zwei Stages:

test
installiert Dependencies

führt pytest aus

setzt SKIP_MODEL_LOAD=1

Dummy-Modelle ermöglichen Contract-Tests ohne echte Modelle

build
baut Docker-Image

pusht Image (nur auf main)

Docker (optional)
docker build -t sentiment-api:local .
docker run --rm -p 8000:8000 sentiment-api:local
Training (Modelle neu erzeugen)
python -m src.train_model
Erzeugte Artefakte:

model/sentiment_de.joblib

model/sentiment_en.joblib

model/sentiment_all.joblib

Daten & Experimente (Kurzüberblick)
## Daten & Experimente (Kurzüberblick)
- **Domänenkonsistenz (DE & EN):**  
  Sowohl die englischen als auch die deutschen Trainingsdaten bestehen aus
  **Filmrezensionen**.  
  Die englischen Daten waren von Beginn an domänenspezifisch (Filmreviews),
  während die ursprünglich verwendeten deutschen Daten allgemeinerer Natur waren.

- **Domänenanpassung (DE):**  
  Um eine konsistente Datenbasis sicherzustellen und die Modellleistung zu verbessern,
  wurden die deutschen Trainingsdaten gezielt auf die **Filmdomäne** umgestellt
  (Filmstarts-Reviews). Gleichzeitig wurde die verfügbare Datenmenge deutlich erhöht.

- **Balanciertes Sampling:**  
  Für beide Sprachen wird ein maximal balancierter Datensatz
  (positive vs. negative Samples) verwendet, um Klassenbias zu vermeiden.

- **Learning-Curve-Analyse:**  
  Die Lernkurven zeigen eine stabile Leistungssteigerung mit zunehmender
  Trainingsdatenmenge sowie ein Sättigungsverhalten bei größeren Datensätzen.

- **Tokenizer-Experimente:**  
  Alternative Tokenizer führten zu keiner signifikanten Verbesserung und wurden
  daher bewusst verworfen (Designentscheidung).


Balanciertes Sampling:
Maximale, balancierte Datensätze (pos/neg) zur Reduktion von Bias.

Learning Curve Analyse:
Analyse der Modellleistung in Abhängigkeit der Trainingsgröße.

Tokenizer-Experimente:
Keine signifikante Verbesserung → bewusst verworfen (Designentscheidung).

Data & Attribution
German sentiment resources are adapted from the public repository:
https://github.com/oliverguhr/german-sentiment (MIT License).

German training data is based on publicly available movie review sources for academic use.


---

# ✅ 2️⃣ THIRD PARTY LICENSE (copy & paste)

👉 Datei anlegen:
```text
THIRD_PARTY_LICENSES/german-sentiment_LICENSE.txt
👉 Inhalt:

This project includes resources adapted from the following public repository:

https://github.com/oliverguhr/german-sentiment

License: MIT License

The original license applies to the adapted components.
All rights remain with the original authors and data providers.

The data is included solely for academic and non-commercial use
as part of a university examination submission.