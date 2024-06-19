# Cette fonction sert à traduire une lettre via le chiffement de César
# Pour ce faire, elle prend en paramètre un caractère (char nommé "lettre") ainsi
# qu'un "offset": un int qui représente le décalage à effectuer dans l'alphabet
# La fonction renvoit un char qui correspond au caractère reçu comme input, mais décalé dans l'alphabet
# d'autant qu'indiqué par le paramètre offset.
# (si le caractère n'est pas une lettre, la fonction renvoit ce caractère tel quel)
def traduire_lettre(lettre, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # On transforme la lettre en minuscule pour ne pas devoir traiter les majuscules séparément.
    lettre = lettre.lower()
    if lettre not in alphabet:
        # Si jamais la lettre n'est pas dans l'alphabet de base, celle-ci ne change pas.
        return lettre
    i = alphabet.index(lettre)
    # On trouve le nouvel indice et on utilise le modulo pour éviter que ce nouvel indice ne dépasse la longueur de l'alphabet
    # (le modulo a une propriété qui permet de recommencer à zéro quand on dépasse un nombre:
    # si je fait a = x%10 et que x est plus petit que 10, a sera égal à x.
    # Mais si x est plus grand ou égal à 10, a sera égal à x-10 (tant que x est plus petit que 20))
    new_i = (i+offset)%len(alphabet)
    return alphabet[new_i]

texte = """Fhfl hvw xqh sduwlh gx whawh, iéolflwdwlrqv.
Pdokhxuhxvhphqw, fhwwh sduwlh hvw xq slèjh srxu frqwuhu o'dssurfkh xqltxhphqw pdqxhooh.
Ohv oljqhv gx edv rqw xq dxwuh géfdodjh txh fhv oljqhv flv.
Lo idxw wurxyhu ohxu géfdodjh fdu fh vrqw hoohv txl frqwlhqqhqw oh yudl lqglfh.
Ev wrzkvj grj rkkvekzfe rlo 4 czxevj rl uvjjlj, vccvj jlzmvek le rlkiv uétrcrxv, drzj jfek zelkzcvj.
Cvj 4 czxevj jlzmrekvj jfek cvj gclj zdgfikrekvj:
Dfe givdzvi vjk lev efkv uv dljzhlv.
Urej dfe uvlozèdv fe gvlk kiflmvi uv c'fi.
Cv tfigj yldrze vjk wrzk à 60% uv dfe kifzjzèdv.
Dfe kflk vjk le avl uv jftzéké u'fizxzev tyzefzjv.
"""
offset = 1
while True:
    # On crée un nouveau texte vide dans lequel on va ajouter toutes les lettres décalées
    new_text = ""
    for c in texte:
        # On décale chaque lettre d'un même décalage "offset" et on les rajoute au nouveau texte
        new_text += traduire_lettre(c, offset)
    # On affiche le nouveau texte final
    print(new_text)
    # Le input sert ici juste à pauser la boucle. L'utilisateur peut laisser le code continuer en appuyant sur enter
    input()
    # On augmente l'offset de 1 pour essayer le décalage suivant si jamais on a pas encore trouvé le bon décalage
    offset += 1