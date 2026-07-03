# src/train_models_lang.py
from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.pipeline import Pipeline

TRAIN_PATH = Path("data/processed/train.csv")
TEST_PATH = Path("data/processed/test.csv")
MODEL_DIR = Path("model")

MODEL_DE = MODEL_DIR / "sentiment_de.joblib"
MODEL_EN = MODEL_DIR / "sentiment_en.joblib"

RANDOM_SEED = 42


def make_model() -> Pipeline:
    return Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.95)),
        ("clf", LogisticRegression(max_iter=2000, n_jobs=None)),
    ])


def train_one_lang(lang: str, train_df: pd.DataFrame, test_df: pd.DataFrame, out_path: Path) -> None:
    tr = train_df[train_df["lang"] == lang].copy()
    te = test_df[test_df["lang"] == lang].copy()

    if tr.empty or te.empty:
        raise ValueError(f"Keine Daten gefunden für lang='{lang}'. Prüfe Spalte 'lang' in train/test.")

    model = make_model()
    model.fit(tr["text"], tr["label"])

    y_pred = model.predict(te["text"])
    acc = accuracy_score(te["label"], y_pred)
    f1 = f1_score(te["label"], y_pred)

    print(f"\n===== {lang.upper()}-ONLY =====")
    print(f"Test n={len(te)} | Accuracy={acc:.4f} | F1={f1:.4f}")
    print(classification_report(te["label"], y_pred, digits=4))

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, out_path)
    print(f"✅ gespeichert: {out_path}")


def main() -> None:
    if not TRAIN_PATH.exists() or not TEST_PATH.exists():
        raise RuntimeError("train.csv / test.csv fehlt. Bitte erst prepare_data.py ausführen.")

    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    # Basic sanity check
    for col in ["text", "label", "lang"]:
        if col not in train_df.columns or col not in test_df.columns:
            raise ValueError(f"Spalte '{col}' fehlt. train cols={train_df.columns.tolist()}")

    train_one_lang("de", train_df, test_df, MODEL_DE)
    train_one_lang("en", train_df, test_df, MODEL_EN)

    print("\n✅ Fertig: 2 Sprach-Modelle erstellt (DE & EN).")


if __name__ == "__main__":
    main()
