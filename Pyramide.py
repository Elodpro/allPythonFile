"""
Nom exercice : Créer une pyramide dans la console
Date : 29.11.2023
Auteur : ELod Arifi
"""

#Variables
k = 0
Nb = 0

inputNb = input("Choisissez entre 3 et 15 : ")

def fn():
    global inputNb
    # Boucles permettant de vérifier si c'est inférieur a 3 et sup a 15 et verif s c'est un chiffre.
    while not inputNb.isdigit() or int(inputNb) > 15 or int(inputNb) < 3:
        print("\nSeulement entre 3 et 15")
        inputNb = input("Choisissez entre 3 et 15 : ")


# Demander à l'utilisateur le nombre de lignes pour le sapin
nbRows = fn()

# Boucle for pour dessiner la pyramide
for i in range(1, nbRows + 1):
    espaces = " " * (nbRows - i)  # Les spaces gauche
    etoiles = "* " * i  # Les étoiles du centre avec un space avant et après chaque *
    print(espaces + etoiles)






