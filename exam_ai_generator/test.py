import os
import google.generativeai as genai
from dotenv import load_dotenv

# Charge la clé API
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Lister tous les modèles disponibles
models = genai.list_models()
for m in models:
    print(m)
