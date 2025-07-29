import re
from unidecode import unidecode

def clean_text(text: str) -> str:
    """
    Pulisce il testo rimuovendo accenti, spazi doppi e caratteri inutili.
    """
    text = unidecode(text)  # Rimuove accenti (es. à → a)
    text = re.sub(r'\s+', ' ', text)  # Riduce tutti gli spazi multipli a uno
    text = re.sub(r'\n+', '\n', text)  # Riduce righe vuote consecutive
    return text.strip()
