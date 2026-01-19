import os
from PyPDF2 import PdfReader
from docx import Document

MAX_CHARS = 12000  # sécurité IA

def extract_text(file_storage):
    """
    Extrait le texte depuis un fichier Flask FileStorage (PDF, DOCX, TXT)
    """
    if not file_storage or file_storage.filename == "":
        return ""

    filename = file_storage.filename
    extension = os.path.splitext(filename)[1].lower()
    text = ""

    # --- TXT ---
    if extension == ".txt":
        text = file_storage.read().decode("utf-8", errors="ignore")

    # --- PDF ---
    elif extension == ".pdf":
        reader = PdfReader(file_storage)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # --- WORD ---
    elif extension == ".docx":
        document = Document(file_storage)
        text = "\n".join(p.text for p in document.paragraphs if p.text.strip())

    else:
        return "FORMAT_NON_SUPPORTE"

    # 🔐 LIMITATION CRITIQUE POUR L’IA
    return text.strip()[:MAX_CHARS]
