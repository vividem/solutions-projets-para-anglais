print("Bienvenu au convertisseur de monnaie.")
unite_base = input("Quelle est votre monnaie de base? ('EUR', 'USD', 'GBP', 'CAD', 'CHF', 'JPY')")

if unite_base=="EUR":
    base_en_euro = 1
elif unite_base=="USD":
    base_en_euro = 0.937
elif unite_base=="GBP":
    base_en_euro = 1.17
elif unite_base=="CAD":
    base_en_euro = 0.6801
elif unite_base=="CHF":
    base_en_euro = 1.0249
elif unite_base=="JPY":
    base_en_euro = 0.0061
else:
    print("Monnaie inconnue, programme terminé.")
    quit()
    
unite_fin = input("Vers quelle monnaie voulez-vous convertir votre somme? ")
if unite_fin=="EUR":
    fin_en_euro = 1
elif unite_fin=="USD":
    fin_en_euro = 0.937
elif unite_fin=="GBP":
    fin_en_euro = 1.17
elif unite_fin=="CAD":
    fin_en_euro = 0.6801
elif unite_fin=="CHF":
    fin_en_euro = 1.0249
elif unite_fin=="JPY":
    fin_en_euro = 0.0061
else:
    print("Monnaie inconnue, programme terminé.")
    quit()
    
monnaie_initiale = float(input("Quelle somme en "+unite_base+" voulez-vous convertir? "))
monnaie_finale = (monnaie_initiale*base_en_euro)/fin_en_euro
print(str(monnaie_initiale)+" "+unite_base+" vaut "+str(monnaie_finale)+" "+unite_fin)

