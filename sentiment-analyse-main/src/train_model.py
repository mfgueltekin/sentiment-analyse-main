# src/train_model.py
from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

from text_preprocessing import normalize_text

TRAIN_PATH = Path("data/processed/train.csv")
TEST_PATH = Path("data/processed/test.csv")

OUT_DIR = Path("model")
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_DE = OUT_DIR / "sentiment_de.joblib"
MODEL_EN = OUT_DIR / "sentiment_en.joblib"
MODEL_ALL = OUT_DIR / "sentiment_all.joblib"


def build_model() -> Pipeline:
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            preprocessor=normalize_text,
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.95,
        )),
        ("clf", LogisticRegression(max_iter=2000, class_weight="balanced")),
    ])


def print_split_stats(name: str, df: pd.DataFrame) -> None:
    print(f"\n===== Split Stats: {name} =====")
    print("Rows:", len(df))
    if "label" in df.columns:
        print("Label dist (0=neg,1=pos):", df["label"].value_counts().sort_index().to_dict())
    if "lang" in df.columns:
        print("Lang dist:", df["lang"].value_counts().to_dict())
        print("By lang+label:")
        print(df.groupby("lang")["label"].value_counts().unstack(fill_value=0))


def eval_and_print(name: str, model: Pipeline, test_df: pd.DataFrame) -> None:
    y_true = test_df["label"].astype(int)
    y_pred = model.predict(test_df["text"])
    print(f"\n===== Evaluation: {name} =====")
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, digits=4))


def main() -> None:
    if not TRAIN_PATH.exists() or not TEST_PATH.exists():
        raise RuntimeError("train/test CSV fehlt. Bitte erst prepare_data.py ausführen.")

    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    train_df["label"] = train_df["label"].astype(int)
    test_df["label"] = test_df["label"].astype(int)

    # Split nach Sprache
    train_de = train_df[train_df["lang"] == "de"].copy()
    train_en = train_df[train_df["lang"] == "en"].copy()

    test_de = test_df[test_df["lang"] == "de"].copy()
    test_en = test_df[test_df["lang"] == "en"].copy()

    # Stats (für Abgabe super)
    print_split_stats("TRAIN (all)", train_df)
    print_split_stats("TEST (all)", test_df)
    print_split_stats("TRAIN_DE (Filmstarts)", train_de)
    print_split_stats("TEST_DE (Filmstarts)", test_de)

    # 1) DE-Modell
    model_de = build_model()
    model_de.fit(train_de["text"], train_de["label"])
    eval_and_print("DE (nur DE-Test)", model_de, test_de)
    joblib.dump(model_de, MODEL_DE)
    print(f"✅ gespeichert: {MODEL_DE}")

    # 2) EN-Modell
    model_en = build_model()
    model_en.fit(train_en["text"], train_en["label"])
    eval_and_print("EN (nur EN-Test)", model_en, test_en)
    joblib.dump(model_en, MODEL_EN)
    print(f"✅ gespeichert: {MODEL_EN}")

    # 3) Combined-Modell
    model_all = build_model()
    model_all.fit(train_df["text"], train_df["label"])
    eval_and_print("GESAMT (gesamter Test)", model_all, test_df)
    joblib.dump(model_all, MODEL_ALL)
    print(f"✅ gespeichert: {MODEL_ALL}")


if __name__ == "__main__":
    main()
