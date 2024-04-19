# On prépare une variable dans laquelle va s'accumuler le score du joueur
score = 0

print("Bienvenue au grand quiz! Répondez par vrai ou faux pour chacune des 10 affirmations suivantes.\n")

reponse_q1 = input("Le Kenya se situe en Amérique.")
if reponse_q1=="faux":
    print("Bonne réponse!")
    score = score + 1
elif reponse_q1=="vrai":
    print("Mauvaise réponse...")
else:
    print("Je n'ai pas compris la réponse. Je n'accorde donc pas le point.")

# Je fais un print vide après chaque question pour laisser un peu d'espace dans la console
print()

reponse_q2 = input("Georges Washington est le nom du premier Homme sur la lune.")
if reponse_q2=="faux":
    print("Bonne réponse!")
    score = score + 1
elif reponse_q2=="vrai":
    print("Mauvaise réponse...")
else:
    print("Je n'ai pas compris la réponse. Je n'accorde donc pas le point.")

print()

# Et ainsi de suite
print("Le quiz est terminé. Votre score total est: "+str(score))