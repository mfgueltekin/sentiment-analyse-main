"""
Compatibility shim for joblib/pickle.

Models were trained with: `from text_preprocessing import normalize_text`
and persisted via joblib. During loading (e.g. in uvicorn), pickle needs
to import module `text_preprocessing` and access `normalize_text` from it.

The real implementation lives in `src/text_preprocessing.py`.
"""

from src.text_preprocessing import normalize_text  # re-export explicitly

__all__ = ["normalize_text"]
