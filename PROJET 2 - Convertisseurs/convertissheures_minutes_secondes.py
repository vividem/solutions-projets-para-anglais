heures = int(input("Combien d'heures? "))
minutes = int(input("Combien de minutes? "))
secondes = int(input("Combien de secondes? "))

total_secondes = heures*3600 + minutes*60 + secondes
print("Celà fait "+str(total_secondes)+" secondes au total.")