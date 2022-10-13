import random

def jeu():

  borne_minimale = int(input("Bienvenue au jeu de devinette! Choisissez une borne minimale."))
  borne_maximale = int(input("Bienvenue au jeu de devinette! Choisissez une borne maximale."))

  nombre = random.randint(borne_minimale, borne_maximale)
  essai = int(input("Entrez votre essai: "))
  nbr_essai = 0


  while essai != nombre:
    nbr_essai += 1
    if essai < nombre:
     essai = int(input("Votre essai est inférieure au nombre"))

    elif essai > nombre:
      essai = int(input("Votre essai est supérieure au nombre"))

  while essai == nombre:
    print("Félicitations, vous avez devinez le nombre en " + str(nbr_essai) + " essaies!")
    rejouer = input("Voulez-vous jouez une autre partie? (oui ou non)")
    if rejouer == "non":
        exit()
    if rejouer == "oui":
        jeu()
jeu()






