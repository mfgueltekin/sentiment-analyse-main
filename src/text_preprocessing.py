#text_preprocessing.py

from __future__ import annotations

import html
import re

HTML_TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")

# Negationswörter, DE und EN
# Wir tokenizen nur "Negation + nächstes Wort" (Fensterweite 1)
NEGATION_RE = re.compile(
    r"(?iu)\b("
    r"nicht|"
    r"kein(?:e|en|em|er)?|"
    r"nie|"
    r"nichts|"
    r"not|"
    r"never|"
    r"no"
    r")\s+([^\W\d_]+)\b"
)

def normalize_text(s: str) -> str:
    """
    Einheitliche Vorverarbeitung für Training und Inference.
    1) HTML unescape
    2) HTML Tags entfernen
    3) Whitespace normalisieren
    4) Negationshandling: "nicht gut" -> "nicht_gut"
    """
    if s is None:
        return ""

    s = str(s)
    s = html.unescape(s)
    s = HTML_TAG_RE.sub(" ", s)
    s = s.replace("\u00a0", " ")
    s = WHITESPACE_RE.sub(" ", s).strip()

    # Negations Tokenizing
    # Beispiel: "nicht schlecht" -> "nicht_schlecht"
    s = NEGATION_RE.sub(r"\1_\2", s)

    return s
