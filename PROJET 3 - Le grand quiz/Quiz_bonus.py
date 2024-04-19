# On prépare une variable dans laquelle va s'accumuler le score du joueur
score = 0

# Cette variable va servir d'indicateur si l'utilisateur a eu juste à toutes les réponses
# Pour le moment, elle contient la valeur True (comme si on avait une lampe allumée)
# L'idée est que si l'utilisateur donne une bonne réponse, on ne touche pas à cette variable.
# Elle reste donc à True (allumée) tant que les réponses sont bonnes,
# mais reste Fausse si elle a été changée en False à un moment. Mais quand devient-elle fausse?
# On va mettre False dans la variable si l'utilisateur donne une mauvaise réponse (comme si on éteignait la lampe à ce moment là)
# Étant donné qu'on ne touche pas à la variable si l'utilisateur donne une bonne réponse,
# Aucune bonne réponse ne pourra venir remettre la variable à True (rallumer la lampe).
# La variable sera donc définitivement False (éteinte).
# Ainsi, il suffit d'une seule mauvaise réponse pour que la variable devienne False jusqu'à la fin du programme.
# Le seul moyen pour que la variable soit toujours True à la fin du programme, est que l'utilisateur ne fasse aucune erreur.
# À la fin du programme on peut donc voir si l'utilisateur a eu tout juste simplement en regardant si la variable "tout_réussi" est encore True.
tout_reussi = True

print("Bienvenue au grand quiz!")
print("Pour chaque question, choisissez combien de choix de réponse vous aurez (2 ou 4).")
print("Vous gagnerez 1 point pour une bonne réponse parmis 2 choix ou 2 points pour une bonne réponse parmis 4 choix.\n")

print("Comment s'appelle le chien de Tintin?")
# BONUS 1
n_choix = input("Combien de propositions voulez-vous (2 ou 4)? ")
if n_choix=="2":
    print("A) Milou")
    print("B) Jaques Chirac")
    # On précise la bonne réponse et les points à gagner dans des variables en fonction du nombre de choix
    # Ainsi, on ne doit pas écrire deux fois le code qui gère la réponse de l'utilisateur,
    # on peut le faire une seule fois en utilisant ces variables,
    # car ces variables sont adaptées en fonction nobre de choix qui a été choisi ici
    bonne_reponse = "A"
    points_a_gagner = 1
elif n_choix=="4":
    print("A) Jaques Chirac")
    print("B) Ariel")
    print("C) Milou")
    print("D) Scooby-Doo")
    bonne_reponse = "C"
    points_a_gagner = 2
else:
    print("Je n'ai pas compris, quiz annulé.")
    quit() # On arrête le programme
# Appeller la fonction input() sans lui donner de string en paramètre (dans les parenthèses)
# fait qu'on attend bel et bien une réponse de l'utilisateur dans la console,
# mais rien n'est printé avant cette attente.
reponse_q1 = input()
if reponse_q1==bonne_reponse:
    print("Bonne réponse!")
    score = score + points_a_gagner
else:
    print("Mauvaise réponse")
    tout_reussi = False

# Je fais un print vide après chaque question pour laisser un peu d'espace dans la console
print()

print("Qui est l'auteur de Tintin?")
n_choix = input("Combien de propositions voulez-vous (2 ou 4)? ")
if n_choix=="2":
    print("A) Hergé")
    print("B) Milou")
    bonne_reponse = "A"
    points_a_gagner = 1
elif n_choix=="4":
    print("A) Milou")
    print("B) Hergé")
    print("C) Thierry Intin")
    print("D) Jaques Chirac")
    bonne_reponse = "B"
    points_a_gagner = 2
else:
    print("Je n'ai pas compris, quiz annulé.")
    quit()

reponse_q2 = input()
if reponse_q2==bonne_reponse:
    print("Bonne réponse!")
    score = score + points_a_gagner
else:
    print("Mauvaise réponse")
    tout_reussi = False

print()

# BONUS 2
if tout_reussi:
    print("Vous avez eu tout juste, voici la question bonus!")
    print("Quel est le titre de Haddock?")
    n_choix = input("Combien de propositions voulez-vous (2 ou 4)? ")
    if n_choix=="2":
        print("A) Professeur")
        print("B) Capitaine")
        bonne_reponse = "B"
        points_a_gagner = 1
    elif n_choix=="4":
        print("A) Capitaine")
        print("B) Professeur")
        print("C) Docteur")
        print("D) Jaques Chirac")
        bonne_reponse = "A"
        points_a_gagner = 2
    else:
        print("Je n'ai pas compris, quiz annulé.")
        quit()

    reponse_q3 = input()
    if reponse_q3==bonne_reponse:
        print("Bonne réponse!")
        score = score + points_a_gagner
    else:
        print("Mauvaise réponse")

# Et ainsi de suite
print("Le quiz est terminé. Votre score total est: "+str(score))

# BONUS 3