import random

somme_joueur = 100
while somme_joueur>0:
    print("Somme actuelle: "+str(somme_joueur))
    argent_pari = int(input("\nCombien d'argent souhaitez-vous miser? "))
    if argent_pari>somme_joueur:
        print("Vous n'avez pas assez de fonds pour ça, pari annulé.")
        continue
    type_pari = input("Voulez-vous parier sur:\n\tA - pair/impair\n\tB - un nombre exact\nA ou B?\n")
    if type_pari.lower()=="a":
        choix = input("pair ou impair?\n")
        if choix!="pair" and choix!="impair":
            print("Je n'ai pas compris, pari annulé.")
            continue
    elif type_pari.lower()=="b":
        choix = int(input("Quel nombre? (entre 1 et 36 inclus)\n"))
    else:
        print("Je n'ai pas compris votre demande, pari annulé.")
        continue
    print("Les jeux sont faits, rien ne va plus!")
    res = random.randint(1,36)
    print("Le "+str(res)+"!")
    somme_remportee = -argent_pari
    if type_pari.lower()=="a":
        if res%2 == 0:
            if choix == "pair":
                somme_remportee = argent_pari
        else:
            if choix == "impair":
                somme_remportee = argent_pari
    else:
        if choix == res:
            somme_remportee = 35*argent_pari
    if somme_remportee>0:
        print("Pari réussi! Félicitations!")
    else:
        print("Perdu...")
    somme_joueur = somme_joueur + somme_remportee

print("Vous n'avez plus assez d'argent, veuillez quitter le casino.")