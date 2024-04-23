import random

# Fonction pour afficher les propostions dans un ordre aléatoire et avec une lettre pour chacune
# Parametres: propositions: une liste de string représentant les propositions (la première string est la bonne réponse)
# Return: la fonction renvoie la bonne lettre à répondre pour avoir juste
def afficher_propositions(propositions):
    # On stocke la bonne réponse dans une variable pour se rappeler de celle-ci même après que les propositions aient été mélangées
    bon_choix = propositions[0]
    # On mélange les propositions aléatoirement
    random.shuffle(propositions)
    # Cette variable va nous permettre de donner une lettre pour chaque propositions (il ne peut donc pas y avoir plus de 26 propositions)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Cette variable va servir à retenir quelle est la bonne lettre à répondre
    bonne_reponse = None
    # On parcourt les propositions (mélangées) une par une pour les afficher dans la console.
    # On utilise i et enumerate() pour savoir à quel index nous sommes dans la liste.
    # Ceci permet de choisir une lettre à associer à chaque proposition
    for i, p in enumerate(propositions):
        print(f"{alphabet[i]}) {p}")
        # On regarde si la proposition est la bonne réponse.
        # Si oui, on retient la lettre à laquelle celle-ci a été associée
        if p==bon_choix:
            bonne_reponse = alphabet[i].lower()
    # On renvoit la lettre à laquelle a été associée la bonne réponse
    return bonne_reponse

# Cette fonction sert à reposer une question tant que la réponse de l'utilisateur ne correspond pas à une des réponses attendues
# Paramètres:
#               - q: une string représentant la question initiale à poser à l'utilisateur
#               - reponses_acceptees: une liste de string représentant les réponses que l'utilisateur a le droit de répondre
# Return: la fonction renvoie la première réponse d'utilisateur qui fait partie des réponses autorisées
def input_limite(q, reponses_acceptees):
    r = input(q).lower().strip()
    # On utilise "in" pour vérifier si la réponse r fait partie des réponses autorisées.
    # Et on utilise not pour que la condition soit vraie si r ne fait PAS partie des réponses autorisées
    # Donc tant que r ne fait pas partie des réponses autorisées, on repose la question.
    while not (r in reponses_acceptees):
        r = input("Réponse incorrecte veuillez entrer une des réponses suivantes: "+str(reponses_acceptees)).lower().strip()
    # Une fois qu'on sort de la boucle, celà signifie que r est enfin une réponse acceptée.
    # On peut donc la renvoyer
    return r

# Cette fonction s'occupe de poser une question à l'utilisateur et renvoie le nombre de points gagnés
# Paramètres:
#               - question: un dictionnaire qui contient:
#                                       - une entrée nommée "question" contenant la question à poser,
#                                       - une entrée nommée "propositions" qui contient les propositions
#                                         sous forme de liste de strings, dont la première string est la bonne réponse
# Return: La fonction renvoit un int représentant le nombre de points qu'a marqué l'utilisateur pour cette question
def poser_question(question):
    # On pose la question
    print(question["question"])
    n_choix = input_limite("Combien de propositions voulez-vous (2 ou 4)? ", ["2", "4"])
    if n_choix=="2":
        # On prend uniquement deux des propositions de la question:
        # la première, car il s'agit de la bonne réponse, et une autre au hasard
        # (la structure liste[x:y] permet de prendre qu'une section de la liste principale
        # dans liste[x:y] on ne prend les éléments de liste que de l'indice x à l'indice y-1.
        # Si x est absent, on part du premier élément jusqu'au y, et si le y est absent, on part de x jusqu'au dernier élément)
        # exemple: [4,5,6,11,25,2,3][2:5] -> [6,11,25]
        propositions = [question["propositions"][0], random.choice(question["propositions"][1:])]
        reponses_acceptees = ["a","b"]
        points_a_gagner = 1
    else:
        propositions = question["propositions"]
        reponses_acceptees = ["a", "b", "c", "d"]
        points_a_gagner = 2
    bonne_reponse = afficher_propositions(propositions)
    r = input_limite("", reponses_acceptees)
    if r==bonne_reponse:
        print("\nBonne réponse!\n")
        return points_a_gagner
    else:
        print(f"\nMauvaise réponse... La réponse était {bonne_reponse} et vous avez noté {r}\n")
        return 0
    
# On fait une liste qui contient toutes les questions
# Chaque question est encodée sous forme de dictionnaire (la liste est donc une liste de dictionnaires)
# Chaque dictionnaire contient deux entrées:
#           - une "question" qui contient la question sous forme de string
#           - les "propositions" sous forme de liste de strings (on s'est arrangé pour toujours mettre la bonne réponse en premier,
#             ainsi, les fonctions suivantes seront laquelle est la bonne facilement (sans devoir noter l'information en plus dans le dictionnaire)
#             le mélange sera fait par la suite)
questions = [
    {
        "question": "Comment s'appelle le chien de Tintin?",
        "propositions": ["Milou", "Jacques Chirac", "Ariel", "Scooby-Doo"]
    },
    {
        "question": "Qui est l'auteur de Tintin?",
        "propositions": ["Hergé", "Milou", "Thierry Intnin", "Jacques Chirac"]
    }
]

questions_bonus = [
    {
        "question": "Quel est le titre de Haddock?",
        "propositions": ["Capitaine", "Professeur", "Docteur", "Jacques Chirac"]
    }
]

il_y_a_eu_faute = False
score = 0
for q in questions:
    s = poser_question(q)
    if s==0:
        il_y_a_eu_faute = True
    score += s

if not il_y_a_eu_faute:
    print("C'est un sans faute! Voici les questions bonus:")
    for q in questions_bonus:
        score += poser_question(q)

print(f"Votre score final est: {score}")

# Voir Quiz_bonus.py pour le BONUS 3