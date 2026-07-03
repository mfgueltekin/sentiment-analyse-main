# src/data/prepare_filmstarts.py

from __future__ import annotations

from pathlib import Path
import pandas as pd

RAW_PATH = Path("filmstarts/filmstarts.tsv")
OUT_PATH = Path("data/processed/de_filmreviews.csv")


def read_filmstarts_tsv(path: Path) -> pd.DataFrame:
    """
    Robust parser für filmstarts.tsv:
    - Erste 2 Felder: url, rating
    - Alles ab Feld 3 wird als Text zusammengefügt (auch wenn Tabs im Text vorkommen)
    - Keine Zeilen werden wegen 'zu vielen Spalten' verworfen
    """
    rows: list[tuple[str, int, str]] = []
    bad_lines = 0

    # encoding/errors bewusst robust, weil Web-Scrapes manchmal kaputte Zeichen enthalten
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if not line:
                continue

            parts = line.split("\t")
            if len(parts) < 3:
                bad_lines += 1
                continue

            url = parts[0].strip()
            rating_raw = parts[1].strip()
            text = "\t".join(parts[2:]).strip()  # Rest zusammenfügen

            # rating robust parsen
            try:
                rating = int(float(rating_raw))
            except ValueError:
                bad_lines += 1
                continue

            rows.append((url, rating, text))

    df = pd.DataFrame(rows, columns=["url", "rating", "text"])
    print(f"Zeilen gelesen: {len(df)} | Ungültige Zeilen verworfen: {bad_lines}")
    return df


def main() -> None:
    print("Lade filmstarts.tsv …")
    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Nicht gefunden: {RAW_PATH.resolve()}")

    df = read_filmstarts_tsv(RAW_PATH)
    print("Rohdaten (nach Parsing):", len(df))

    # Nur Ratings, die wir für binäres Sentiment sauber mappen können:
    # negativ: 0,1,2 | positiv: 4,5 | neutral/ambivalent (3) wird bewusst ausgeschlossen
    df = df[df["rating"].isin([0, 1, 2, 4, 5])].copy()

    # Binäres Mapping
    df["label"] = df["rating"].apply(lambda r: 1 if r >= 4 else 0)

    # Text säubern: leere/zu kurze entfernen (z.B. nur "ok")
    df["text"] = df["text"].astype(str).str.strip()
    df = df[df["text"].str.len() > 10].copy()

    # Nur die Spalten, die euer Training braucht
    df_out = df[["text", "label"]].copy()

    # Stats ausgeben (Hausarbeit-ready)
    n_total = len(df_out)
    n_pos = int((df_out["label"] == 1).sum())
    n_neg = int((df_out["label"] == 0).sum())

    print("Nach Filterung:", n_total)
    print("Positiv:", n_pos)
    print("Negativ:", n_neg)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(OUT_PATH, index=False, encoding="utf-8")

    print("Gespeichert:", OUT_PATH.resolve())


if __name__ == "__main__":
    main()
