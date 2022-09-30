import random

def jeu():
    print("J'ai choisi un nombre entre 0 et 1000. À vous de le devinez!")

    nombre = random.randint(0, 1000)
    print(nombre)
    essai = int(input("Entrez votre essai: "))
    nbr_essai = 0

    while essai != nombre:
        nbr_essai += 1
        if essai < nombre:
            essai = int(input("Votre essai est inférieure au nombre"))

        elif essai > nombre:
            essai = int(input("Votre essai est supérieure au nombre"))

            if essai == nombre:
                print("Félicitations, vous avez devinez le nombre en" + nbr_essai + "essaies!")
                rejouer = input("Voulez-vous jouez une autre partie? (oui ou non)")
                if rejouer: "non"
                    break
                elif rejouer: "oui"
jeu()


