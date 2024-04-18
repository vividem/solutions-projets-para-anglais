secondes = int(input("Combien de secondes? "))

heures = secondes//3600
# On enlève les secondes qui ont été comptabilisées dans le nombre d'heures
secondes_restantes = secondes - heures * 3600
minutes = secondes_restantes//60
# Des secondes restantes, on enlève également les secondes qui ont été comptabilisées dans le nombre de minutes
secondes_restantes = secondes_restantes - minutes * 60

print("Celà équivaut à "+str(heures)+"h, "+str(minutes)+"min et "+str(secondes_restantes)+"secondes")