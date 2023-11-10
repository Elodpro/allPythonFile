import time
# Donée bancaire
# By Elod
# 08.11.2022

# Variables
pays_eu = "SUISSE", "FRANCE", "ALLEMAGNE", "NORVEGE"
pays_input = ""
age = 0
nom = ""
prenom = ""
banque = 0
printdonne = ""
yes = "OUI"

# all inputs
nom = input("Votre nom ? ")
prenom = input("Votre prénom ? ")
banque = int(input("Votre compte bancaire ? "))
age = int(input("Votre âge ? "))
pays_input = input("Dans quel pays résidez-vous ? ").upper()

# pour que l'input soit en majuscule
while True:
    if pays_input in pays_eu:
        if age >= 18:
            print("Nous vérifions vos donées...")
            time.sleep(3)
            print("Votre compte a été créer avec succès")
            break
        else:
            print("Vous ne pouvez pas créez de compte")
            break

    else:
        if pays_input != pays_eu:
            if age >= 21 and pays_input != pays_eu:
                print("Nous vérifions vos donées...")
                time.sleep(3)
                print("Votre compte a été créer avec succès")
                break
            else:
                print("Vous ne pouvez pas créez de compte")
                break

printdonne = input("Voulez-vous voir vos données inscrites auparavant ? \n").upper()
if printdonne == yes:
    print(f"Votre nom: {nom}\nVotre prénom: {prenom}\nVotre pays: {pays_input}\nVotre âge: {age}\nVos coordonée bancaire: {banque}")
else:
    print("Pas de soucis ! Vous pourrez les voirs plus tard.")
