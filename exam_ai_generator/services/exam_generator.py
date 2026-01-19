import google.generativeai as genai
import os
from dotenv import load_dotenv

# ================================
# CONFIGURATION DE L’API GEMINI
# ================================

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

FORBIDDEN_STARTS = [
    "Absolument",
    "Voici",
    "En tant que",
    "Je vais",
]

# ================================
# FONCTION DE NETTOYAGE DU TEXTE
# ================================
def clean_exam(text: str) -> str:
    lines = text.strip().splitlines()
    cleaned_lines = []

    for line in lines:
        if any(line.strip().startswith(w) for w in FORBIDDEN_STARTS):
            continue
        cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()

# ================================
# VALIDATION DU TEXTE GÉNÉRÉ
# ================================
def validate_exam(text: str):
    if not text or len(text.strip()) < 100:
        raise ValueError("Réponse IA invalide ou incomplète")

# ================================
# FONCTION PRINCIPALE DE GÉNÉRATION
# ================================ss
def generate_exam(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(
            model_name="models/gemini-2.5-flash"
        )

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.6,
                "max_output_tokens": 8000
            }
        )

        result = clean_exam(response.text)
        validate_exam(result)

        return result

    except Exception as e:
        return f"Erreur IA : {str(e)}"
