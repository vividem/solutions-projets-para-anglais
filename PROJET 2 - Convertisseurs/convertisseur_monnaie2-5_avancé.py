# On crée la fonction question_en_boucle
# Cette fonction utilise la fonction input() à l'infini jusqu'à ce que l'utilisateur
# donne une réponse faisant partie des reponses_possibles
# Paramètres:
#     - question (string): La question qui doit être posée à l'utilisateur
#     - reponses_possibles (liste de string): liste des réponses qui peuvent être acceptées
# Return (le résultat de la fonction):
#     renvoie la première réponse de l'utilisateur qui fait partie de la liste des reponses_possibles
def question_en_boucle(question, reponses_possibles):
    # On fait une boucle qui recommence à l'infini
    while True:
        # On pose la question et on récupère la réponse
        reponse = input(question +" "+ str(reponses_possibles)+"\n")
        if reponse in reponses_possibles:
            # Si la réponse fait partie de la liste reponses_possibles, casse la boucle et on passe à la suite du code
            break
        else:
            print("La réponse doit faire partie des possibilitées suivantes: "+str(reponses_possibles)+"\n")
    # Cette ligne n'est atteinte qu'une fois que la boucle a été cassée
    # On renvoie la réponse acceptée comme résultat de la fonction
    return reponse

# On crée un dictionnaire qui relie une valeur à chaque string
valeur_en_euro = {
    "EUR": 1,
    "USD": 0.937,
    "GBP": 1.17,
    "CAD": 0.6801,
    "CHF": 1.0249,
    "JPY": 0.0061
    }

print("Bienvenu au convertisseur de monnaie.")

# On convertit les strings du dictionnaire nommées les keys en une liste
# pour pouvoir l'utiliser dans la fonction question_en_boucle()
reponses_acceptees = list(valeur_en_euro.keys())

# On utilise la fonction question_en_boucle que nous avons créé plus haut
# pour être sûr d'obtenir une réponse qui nous convient
unite_base = question_en_boucle("Quelle est votre monnaie de base?", reponses_acceptees)
unite_fin = question_en_boucle("Vers quelle monnaie voulez-vous convertir votre somme? ",
                               reponses_acceptees)

monnaie_initiale = float(input("Quelle somme en "+unite_base+" voulez-vous convertir? "))
monnaie_finale = (monnaie_initiale * valeur_en_euro[unite_base]) / valeur_en_euro[unite_fin]

print(str(monnaie_initiale)+" "+unite_base+" vaut "+str(monnaie_finale)+" "+unite_fin)


