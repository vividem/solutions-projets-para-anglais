# Dans la ligne suivante, la fonction input() demande un nombre,
# mais la réponse de l'utilisateur, même si composée de chiffres,
# est encodée sous forme de string.
# On ne peut pas faire de calculs mathématiques sur des strings il faudra donc trouver un moyen de la convertir en int ou en float
valeur_utilisateur = input("Quelle température en degrés Fahrenheit voulez-vous convertir en degrés Celcius? ")

# On utilise la fonction float() pour obtenir la valeur numérique (nombre décimal) que représente la string fournie par l'utilisateur.
# (on utilise float() plutôt que int() pour que l'utilisateur puisse aussi fournir des nombres décimaux (que la fonction int() ne pourrait pas convertir))
temp_fahrenheit = float(valeur_utilisateur)

# On peut désormais calculer la valeur numérique en celcius
temp_celcius = (temp_fahrenheit - 32) * 5 / 9

# On donne la réponse finale
# Afin de combiner cette réponse numérique avec des strings,
# il faut d'abords la traduire en string via la foction str()
print("La température que vous avez entrée équivaut à "+str(temp_celcius)+" degrés Celcius.")