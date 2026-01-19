# ==============================
# IMPORTS DES BIBLIOTHÈQUES
# ==============================
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv #permet de charger les variables d'environnement depuis un fichier .env
import os # os : gestion des chemins et variables système

# Fonctions métiers du projet
from services.exam_generator import generate_exam
from services.file_reader import extract_text
from services.pdf_generator import generate_pdf

load_dotenv() # Chargement des variables d'environnement (.env)


app = Flask(__name__)


# ======================
# PAGE D’ACCUEIL
# ======================
@app.route("/")
def index():
    return render_template("index.html")


# ======================
# GENERATION DU SUJET
# ======================
@app.route("/sujet", methods=["GET", "POST"])
def sujet():
    if request.method == "POST":
        cours_text = extract_text(request.files.get("cours_file"))

        if not cours_text or cours_text == "FORMAT_NON_SUPPORTE":
            return render_template("result.html", content="❌ Fichier invalide ou vide.")

        matiere = request.form["matiere"]
        duree = request.form["duree"]
        niveau = request.form["niveau"]
        nb_questions = request.form["nb_questions"]
        types = request.form.getlist("types[]")
        difficulte = request.form["difficulte"]
        format_choisi = request.form["format"]

        prompt = f"""
RÔLE :
Tu es un enseignant universitaire expérimenté.

MISSION UNIQUE ET EXCLUSIVE :
Générer UNIQUEMENT UN SUJET D’EXAMEN COMPLET.

INTERDICTIONS ABSOLUES :
- Aucune introduction
- Aucun texte hors examen
- Aucun commentaire
- Aucun corrigé
- Aucune question longue
- AUCUNE sous-question (1, 2, a, b, i, ii)
- AUCUNE question composée
- AUCUN paragraphe
- Aucune phrase comme "Voici", "Absolument", "Je vais"
- Ne jamais sortir du format imposé
- TERMINE IMPÉRATIVEMENT PAR LA DERNIÈRE QUESTION COMPLÈTE.
- NE COUPE JAMAIS UNE QUESTION.
- LA TOTALITE DES POINTS NE DOIT JAMAIS ETRE INFERIEURE OU SUPERIEURE A 20POINTS.


FORMAT STRICT OBLIGATOIRE :

EXAMEN DE {matiere}
Durée : {duree}
Niveau : {niveau}

STRUCTURE DES QUESTIONS :

POUR LES QCM :
QX. (X points) Question courte et directe.
A) ...
B) ...
C) ...
D) ...

POUR LES QUESTIONS OUVERTES :
QX. (X points) Question courte et directe.

POUR LES EXERCICES :
ExerciceX. (X points) Exercice simple et direct.

RÈGLES QCM :
- EXACTEMENT 4 propositions (A, B, C, D)
- UNE SEULE bonne réponse
- Propositions de longueur similaire
- Pas de phrases longues

RÈGLES QCM :
- EXACTEMENT 4 questions (1, 2, 3, 4)
- Propositions de longueur similaire
- Pas de phrases longues

PARAMÈTRES :
Nombre de questions : {nb_questions}
Types autorisés : {', '.join(types)}
Difficulté : {difficulte}
Format : {format_choisi}

CONTRAINTE FINALE :
- Ne jamais écrire de sous-questions
- Ne jamais numéroter à l’intérieur d’une question
- Terminer chaque question complètement

COURS :
{cours_text}
"""


        sujet = generate_exam(prompt)

        if format_choisi == "pdf":
            pdf_path = "Sujet_Examen.pdf"
            generate_pdf(sujet, pdf_path)
            return send_file(pdf_path, as_attachment=True)

        return render_template("result.html", content=sujet)

    return render_template("sujet.html")


# ======================
# CORRIGÉ
# ======================
@app.route("/corrige", methods=["GET", "POST"])
def corrige():
    if request.method == "POST":
        sujet_text = extract_text(request.files["sujet_file"])
        format_choisi = request.form["format"]

        prompt = f"""
RÔLE :
Tu es un enseignant universitaire correcteur officiel.

MISSION UNIQUE :
Générer UNIQUEMENT le CORRIGÉ COMPLET du sujet fourni.

INTERDICTIONS STRICTES :
- Ne jamais réécrire le sujet
- Ne jamais ajouter de nouvelles questions
- Ne jamais ajouter d’introduction ou de conclusion
- Ne jamais inclure le sujet dans la réponse
- Repond directement au question
- TERMINE IMPÉRATIVEMENT PAR LA DERNIÈRE QUESTION COMPLÈTE.
- NE COUPE JAMAIS UNE QUESTION.


FORMAT OBLIGATOIRE :
CORRIGÉ 

Q1. (X points) Question
Réponse

Q2. (X points) Question
Réponse

...

POUR CHAQUE QUESTION :
- Réponse claire
- Justification
- Respect du barème

SUJET À CORRIGER :
{sujet_text}
"""


        corrige = generate_exam(prompt)

        if format_choisi == "pdf":
            pdf_path = "Corrige_Examen.pdf"
            generate_pdf(corrige, pdf_path)
            return send_file(pdf_path, as_attachment=True)

        return render_template("result.html", content=corrige)

    return render_template("corrige.html")


if __name__ == "__main__":
    app.run(debug=True)
