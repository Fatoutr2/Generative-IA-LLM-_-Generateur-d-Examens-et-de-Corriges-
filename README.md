# Générateur d'Examens avec IA

## Description
Ce projet est une application web développée en **Python (Flask)** permettant de générer automatiquement des examens et leurs corrigés à partir de documents pédagogiques (PDF, Word, TXT).  
L'objectif est de faciliter la création de contenus d'évaluation pour enseignants et formateurs, en utilisant l'intelligence artificielle pour analyser le contenu et générer des questions pertinentes.

## Fonctionnalités
- Téléversement de documents (PDF, Word, TXT) comme source de cours.
- Génération automatique de questions d'examen.
- Création des corrigés correspondants.
- Interface web simple et intuitive via Flask.
- Base de données SQL pour stocker les examens et documents.
- Compatible avec MySQL et SQLite.

## Technologies Utilisées
- **Backend** : Python 3.8+, Flask
- **Base de données** : MySQL (ou SQLite pour tests)
- **Frontend** : HTML, CSS, Bootstrap
- **IA** : Intégration d’un modèle génératif pour la création automatique des questions
- **Gestion de dépendances** : `venv` et `requirements.txt`

## Installation
1. Cloner le dépôt :
   ```bash
   git clone https://votre-repo.git
   cd Generateur_Examens
Créer un environnement virtuel :

python -m venv venv


Activer l’environnement :

Windows :

venv\Scripts\activate


Linux / Mac :

source venv/bin/activate


Installer les dépendances :

pip install -r requirements.txt


Configurer la base de données (MySQL) et mettre à jour config.py avec vos informations.

Lancer l’application :

flask run


Accéder à l’application sur http://127.0.0.1:5000

Structure du Projet
Generateur_Examens/
│
├── app.py                # Entrée principale de l’application
├── config.py             # Configuration (DB, API Keys, etc.)
├── requirements.txt      # Dépendances Python
├── database/
│   └── schema.sql        # Structure de la base de données
├── templates/            # Templates HTML (Flask)
├── static/               # CSS, JS, images
<<<<<<< HEAD
└── venv/                 # Environnement virtuel (ignoré par Git)
=======
└── venv/                 # Environnement virtuel (ignoré par Git)
>>>>>>> 5647fcd (Initial commit - Generateur IA d'examen et de corrige)
