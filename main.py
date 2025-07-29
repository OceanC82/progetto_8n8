from fastapi import FastAPI, UploadFile, File
import os
from parser import extract_text
from utils import clean_text

app = FastAPI()

@app.post("/upload")
async def upload_book(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[-1].lower()
    path = f"temp{ext}"
    
    with open(path, "wb") as f:
        f.write(await file.read())

    # Estrazione e pulizia testo
    raw = extract_text(path)
    cleaned = clean_text(raw)

    # Salva il risultato
    with open("libro_clean.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)

    return {
        "message": "Libro caricato e pulito con successo.",
        "lunghezza_caratteri": len(cleaned)
    }
