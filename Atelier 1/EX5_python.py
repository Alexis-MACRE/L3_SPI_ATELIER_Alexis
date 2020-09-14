#Auteur : Ezzaatari Zakaria & Alexis Macre
#Date : 07/09/2020
#Version : 1.0
#Description : Atelier de programmation Exo 5 Python


def frais_portuaires() :
     """Cette fonction permet de calculer les frais annuels portuaire en fonction des caractéristiques du bateau"""
     nom_voilier = input("Veuillez saisir le nom du voilier: ")
     longueur_voilier = float(input("Veuillez saisir sa taille: "))
     categorie_voilier = int(input("Veillez saisir sa catégorie: "))

     taxe_annuelle = [100,150,250]

     if(longueur_voilier < 5) :
          cout_mensuel = 100

     elif(longueur_voilier <= 10) :
          cout_mensuel = 200

     elif(longueur_voilier <=12) :
          cout_mensuel = 400

     else :
          cout_mensuel = 600

     cout_annuel = cout_mensuel*12 + taxe_annuelle[categorie_voilier-1]
     
     print("Le coût annuel d'une place au port pour le voilier",nom_voilier,"est de",cout_annuel,"euros")


frais_portuaires()



