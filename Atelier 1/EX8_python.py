#Auteur : Alexis MACRE
#Date : 09/09/2020
#Version : 1.0
#Description : Atelier de programmation Exo 8 Python

def couleur_client(age:int,duree_permis:int,accidents:int,duree_companie:int) -> str:
     """Fonction qui demande les informations du client puis en déduit la couleur qui lui est attribué"""
     NOM_COULEUR=["Refuse","Rouge","Orange","Vert","Bleu"]
     AGE_PIVOT = 25
     PALIER_BONUS_MOIS = 12

     REFUSE=0
     ROUGE=1
     ORANGE=2
     VERT=3
     #BLEU=4

     if age<AGE_PIVOT and duree_permis<2:
          couleur = ROUGE-accidents                                        #Rouge - Refusé
          
     elif age >= AGE_PIVOT and duree_permis>=2: 
          couleur = VERT-accidents                                         #Vert - Orange - Rouge - Refusé
     
     else:
          couleur = ORANGE-accidents                                       #Orange - Rouge - Refusé

     couleur = max(couleur, REFUSE)                                        #Pour ne pas descendre en dessous de 0

     couleur+= (duree_companie>=PALIER_BONUS_MOIS and couleur!=REFUSE)     #Augmente la couleur d'un palier s'il est là depuis plus d'un an

     return NOM_COULEUR[couleur]

age=int(input("Age du client: "))
duree_permis=int(input("Duree de l'obtention du permis en annees: "))
accidents=int(input("Nombre d'accidents: "))
duree_companie=int(input("Temps en mois chez la companie: "))

print("Le client est de couleur",couleur_client(age,duree_permis,accidents,duree_companie))

