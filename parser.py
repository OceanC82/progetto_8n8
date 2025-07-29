import fitz  # PyMuPDF
from docx import Document

def extract_text(path: str) -> str:
    """
    Estrae il testo da un file PDF, DOCX o TXT.
    """
    if path.endswith(".pdf"):
        doc = fitz.open(path)
        return "\n".join([page.get_text() for page in doc])
    
    elif path.endswith(".docx"):
        doc = Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
    
    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    
    else:
        raise ValueError("Formato non supportato. Usa PDF, DOCX o TXT.")
