# src/data/prepare_data.py
from __future__ import annotations

import argparse
import csv
import html
import json
import re
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

RANDOM_SEED = 42

HTML_TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")


def clean_text(s: str) -> str:
    if s is None:
        return ""
    s = str(s)
    s = html.unescape(s)
    s = HTML_TAG_RE.sub(" ", s)  # entfernt <br />, <p> usw.
    s = s.replace("\u00a0", " ")
    s = WHITESPACE_RE.sub(" ", s).strip()
    return s


def map_sentiment_to_label(x: str) -> int | None:
    """Mappt Sentiment auf 0/1. Neutral/unklar -> None (wird entfernt)."""
    if x is None:
        return None
    s = str(x).strip().lower()
    if s in {"positive", "positiv"}:
        return 1
    if s in {"negative", "negativ"}:
        return 0
    return None


def load_en(path: Path) -> pd.DataFrame:
    """
    EN-Datei:
    - IMDb original: review, sentiment
    - oder schon vereinheitlicht: text, sentiment, ...
    """
    df = pd.read_csv(path)

    if "review" in df.columns:
        text_col = "review"
    elif "text" in df.columns:
        text_col = "text"
    else:
        raise ValueError(
            f"EN-Datensatz: Weder 'review' noch 'text' gefunden. Vorhanden: {list(df.columns)}"
        )

    if "sentiment" not in df.columns:
        raise ValueError(
            f"EN-Datensatz: Spalte 'sentiment' fehlt. Vorhanden: {list(df.columns)}"
        )

    out = pd.DataFrame(
        {
            "text": df[text_col].map(clean_text),
            "label": df["sentiment"].map(map_sentiment_to_label),
            "lang": "en",
        }
    )

    out = out[out["text"].str.len() > 0].copy()
    out = out.dropna(subset=["label"]).copy()  # neutral raus
    out["label"] = out["label"].astype(int)
    out = out.drop_duplicates(subset=["text"]).reset_index(drop=True)
    return out


def load_de_tsv(path: Path) -> pd.DataFrame:
    """
    DE-Datei (Basisdaten_De.tsv):
    - sehr wahrscheinlich KEINE Header-Zeile
    - robustes Lesen:
      1) Versuch mit Header
      2) fallback ohne Header (header=None) und nehmen text/sentiment per Positionsspalten
    Erwartetes Layout ohne Header:
      col0 = url
      col1 = text
      col2 = relevance (true/false)
      col3 = sentiment (positive/negative/neutral)
    """
    # 1) Versuch: mit Header (falls doch vorhanden)
    try:
        df_try = pd.read_csv(
            path,
            sep="\t",
            engine="python",
            quoting=csv.QUOTE_NONE,
            on_bad_lines="skip",
            encoding="utf-8",
        )
        if "text" in df_try.columns:
            sent_col_name = "sentiment" if "sentiment" in df_try.columns else None
            if sent_col_name is None:
                for cand in ["Sentiment", "polarity", "Polarity", "label"]:
                    if cand in df_try.columns:
                        sent_col_name = cand
                        break
            if sent_col_name is None:
                raise ValueError("DE: Keine Sentiment-Spalte gefunden.")

            out = pd.DataFrame(
                {
                    "text": df_try["text"].map(clean_text),
                    "label": df_try[sent_col_name].map(map_sentiment_to_label),
                    "lang": "de",
                }
            )
            out = out[out["text"].str.len() > 0].copy()
            out = out.dropna(subset=["label"]).copy()
            out["label"] = out["label"].astype(int)
            out = out.drop_duplicates(subset=["text"]).reset_index(drop=True)
            return out
    except Exception:
        pass

    # 2) Fallback: ohne Header
    for sep in ["\t", ";", ","]:
        df = pd.read_csv(
            path,
            sep=sep,
            engine="python",
            header=None,
            quoting=csv.QUOTE_NONE,
            on_bad_lines="skip",
            encoding="utf-8",
        )

        if df.shape[1] >= 4:
            text_series = df.iloc[:, 1]
            sent_series = df.iloc[:, 3]

            out = pd.DataFrame(
                {
                    "text": text_series.map(clean_text),
                    "label": sent_series.map(map_sentiment_to_label),
                    "lang": "de",
                }
            )

            out = out[out["text"].str.len() > 0].copy()
            out = out.dropna(subset=["label"]).copy()
            out["label"] = out["label"].astype(int)
            out = out.drop_duplicates(subset=["text"]).reset_index(drop=True)
            return out

    raise ValueError(
        f"DE-Datensatz: konnte die Datei nicht robust einlesen. "
        f"Bitte prüfe Separator/Encoding der Datei: {path}"
    )


def load_de_filmreviews(path: Path) -> pd.DataFrame:
    """
    Lädt vorbereitete deutsche Filmreviews (Filmstarts).
    Erwartet CSV mit Spalten: text,label
    label: 0/1
    """
    df = pd.read_csv(path)

    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError(
            f"de_filmreviews: Erwartet Spalten text,label. Vorhanden: {list(df.columns)}"
        )

    out = pd.DataFrame(
        {
            "text": df["text"].map(clean_text),
            "label": df["label"].astype(int),
            "lang": "de",
        }
    )

    out = out[out["text"].str.len() > 0].copy()
    out = out.dropna(subset=["label"]).copy()
    out["label"] = out["label"].astype(int)
    out = out.drop_duplicates(subset=["text"]).reset_index(drop=True)

    vc = out["label"].value_counts().to_dict()
    print(f"DE Quelle: Filmreviews ({path}) rows={len(out)} dist={vc}")
    return out


def sample_balanced(df: pd.DataFrame, n_pos: int, n_neg: int, name: str) -> pd.DataFrame:
    pos = df[df["label"] == 1]
    neg = df[df["label"] == 0]

    if len(pos) < n_pos:
        raise ValueError(f"{name}: Zu wenig POSITIV. Verfügbar {len(pos)}, benötigt {n_pos}.")
    if len(neg) < n_neg:
        raise ValueError(f"{name}: Zu wenig NEGATIV. Verfügbar {len(neg)}, benötigt {n_neg}.")

    pos_s = pos.sample(n=n_pos, random_state=RANDOM_SEED)
    neg_s = neg.sample(n=n_neg, random_state=RANDOM_SEED)

    out = pd.concat([pos_s, neg_s], ignore_index=True)
    out = out.sample(frac=1.0, random_state=RANDOM_SEED).reset_index(drop=True)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--en", default="data/raw/Basisdaten_En.csv")
    parser.add_argument("--de", default="data/processed/de_filmreviews.csv")
    parser.add_argument("--de-source", choices=["filmreviews", "tsv"], default="filmreviews")
    parser.add_argument("--out", default="data/processed")

    # 0 bedeutet: AUTO = maximal balanced
    parser.add_argument("--en-pos", type=int, default=0)
    parser.add_argument("--en-neg", type=int, default=0)
    parser.add_argument("--de-pos", type=int, default=0)
    parser.add_argument("--de-neg", type=int, default=0)

    parser.add_argument("--test-size", type=float, default=0.2)
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    en = load_en(Path(args.en))

    if args.de_source == "filmreviews":
        de = load_de_filmreviews(Path(args.de))
    else:
        de = load_de_tsv(Path(args.de))

    # Debug-Ausgabe
    en_dist = en["label"].value_counts().to_dict()
    de_dist = de["label"].value_counts().to_dict()
    print("EN rows:", len(en), "dist:", en_dist)
    print("DE rows:", len(de), "dist:", de_dist)

    # AUTO: maximal balanced = min(pos, neg)
    if args.en_pos == 0 or args.en_neg == 0:
        en_max = int(min(en_dist.get(1, 0), en_dist.get(0, 0)))
        args.en_pos = en_max
        args.en_neg = en_max
        print(f"EN AUTO balanced: {en_max} pos / {en_max} neg")

    if args.de_pos == 0 or args.de_neg == 0:
        de_max = int(min(de_dist.get(1, 0), de_dist.get(0, 0)))
        args.de_pos = de_max
        args.de_neg = de_max
        print(f"DE AUTO balanced: {de_max} pos / {de_max} neg")

    en_s = sample_balanced(en, n_pos=args.en_pos, n_neg=args.en_neg, name="EN")
    de_s = sample_balanced(de, n_pos=args.de_pos, n_neg=args.de_neg, name="DE")

    en_path = out_dir / "en_sample.csv"
    de_path = out_dir / "de_sample.csv"
    en_s.to_csv(en_path, index=False)
    de_s.to_csv(de_path, index=False)

    combined = pd.concat([en_s, de_s], ignore_index=True)

    # stratify nach lang+label, damit Balance im Train/Test stabil bleibt
    strat = combined["lang"].astype(str) + "_" + combined["label"].astype(str)
    train_df, test_df = train_test_split(
        combined,
        test_size=args.test_size,
        random_state=RANDOM_SEED,
        stratify=strat,
    )

    train_path = out_dir / "train.csv"
    test_path = out_dir / "test.csv"
    combined_path = out_dir / "combined.csv"

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    combined.to_csv(combined_path, index=False)

    # Report
    report = {
        "en_raw_rows": int(len(en)),
        "de_raw_rows": int(len(de)),
        "en_sample_rows": int(len(en_s)),
        "de_sample_rows": int(len(de_s)),
        "combined_rows": int(len(combined)),
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "distribution_combined": (
            combined.groupby(["lang", "label"]).size().reset_index(name="count").to_dict(orient="records")
        ),
        "distribution_train": (
            train_df.groupby(["lang", "label"]).size().reset_index(name="count").to_dict(orient="records")
        ),
        "distribution_test": (
            test_df.groupby(["lang", "label"]).size().reset_index(name="count").to_dict(orient="records")
        ),
        "outputs": {
            "en_sample": str(en_path),
            "de_sample": str(de_path),
            "combined": str(combined_path),
            "train": str(train_path),
            "test": str(test_path),
        },
    }

    (out_dir / "prepare_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("✅ Fertig. Report:")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

