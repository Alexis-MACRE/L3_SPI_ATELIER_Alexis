#Auteur : Alexis MACRE
#Date : 07/09/2020
#Version : 1.0
#Description : Atelier de programmation Exo 4 Python

def facture_photocopie() :
     """Cette fonction permet de calculer la facture en fonction du nombre de photocopie rentrée"""
     nbr_copie = int(input("Veillez saisir le nombre de copies :"))
     if(nbr_copie<=10) :
          prix_total = nbr_copie * 0.1

     elif(nbr_copie<=30) :
          prix_total = 1 + (nbr_copie-10)*0.09

     else :
          prix_total = 1 + 1.8 + (nbr_copie-30)*0.08 

     return prix_total
     

facture = facture_photocopie()

print("Prix total :",round(facture,2)," €")




