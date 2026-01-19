def build_prompt(data, cours):
    return f"""
Tu es un enseignant universitaire expérimenté.

À partir du cours suivant, génère un examen académique.

=== PARAMÈTRES ===
Durée : {data['duree']}
Niveau : {data['niveau']}
Nombre de questions : {data['nb_questions']}
Types de questions : {', '.join(data['types'])}
Difficulté : {data['difficulte']}

=== CONSIGNES ===
1. Génère uniquement le contenu académique
2. Structure claire
3. Barème détaillé
4. Corrigé pédagogique clair
5. Niveau universitaire

=== COURS ===
{cours}

=== SORTIE ATTENDUE ===
- Sujet d’examen
- Barème
- Corrigé détaillé
"""
