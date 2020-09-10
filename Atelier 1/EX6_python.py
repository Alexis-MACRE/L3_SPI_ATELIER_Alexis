#Auteur : Alexis MACRE
#Date : 08/09/2020
#Version : 1.0
#Description : Atelier de programmation Exo 6 Python

def frais_mensuels_voiture(kilometres_annuels, type_carburant, cylindree_voiture, prix_carburant) :
     """Fonction de calcul des frais mensuels en fonction des divers parametres demandés"""
     if type_carburant == "D" :
          consommation_au_100km = 8
          coef_entretien = 1.7

     elif cylindree_voiture >= 2000 :
          consommation_au_100km = 10
          coef_entretien = 1.5
     else :
          consommation_au_100km = 8
          coef_entretien = 1.5
     
     prix_annuel = kilometres_annuels*(consommation_au_100km /100) * prix_carburant * coef_entretien

     return round((prix_annuel/12),2)


input_kilometres = int(input("nombre de kilomètres parcourus : "))
input_type = input("type de carburant utilisé (D / E) : ")
input_cylindree = int(input("cylindree de la voiture : "))
input_prix = float(input("prix du carburant : "))

frais_mensuels=frais_mensuels_voiture(input_kilometres,input_type,input_cylindree,input_prix)

print(frais_mensuels)


