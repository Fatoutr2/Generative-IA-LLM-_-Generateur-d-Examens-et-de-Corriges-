import os # os : gestion des chemins et variables système
from dotenv import load_dotenv

load_dotenv() # Chargement des variables d'environnement (.env)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
