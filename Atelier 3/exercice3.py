# Auteur : Ezzaatari Zakaria & Alexis Macre
# Date : 14/09/2020
# Version : 1.0
# Description : Atelier de programmation 3 Exo 1 Python

from fonctions_persos import test_fonction

def separer(L:list)->list:
     """Sépare les nombres positifs,négatifs et nuls d'une liste
     
     Arguments:
     L -- la liste de nombres
     
     Retourne la liste triée avec: les nombres négatifs au début, les nombre postifs à la fin et les 0 au millieu
     """
     LSEP=[0]*len(L)                                   # Initie la liste LSEP à [0,0,0,0...], de même dimension que L
     compteur_positif=-1                               
     compteur_negatif=0                                


     for nombre in L:
          if nombre < 0:                               # Si c'est un nombre négatif, on le place au début de la liste
               LSEP[compteur_negatif]=nombre           # et on incrémente le compteur
               compteur_negatif+=1                     
          elif nombre > 0:                             # Si c'est un nombre positif, on le place à la fin de la liste
               LSEP[compteur_positif]=nombre           # et on incrémente le compteur
               compteur_positif-=1
     
     return LSEP


test_fonction(separer,  [[0,0,0,0,1,-2,-5,1],[5,0,0,9,1,-2,-5,5]]  ,  [[-2,-5,0,0,0,0,1,1],[-2,-5,0,0,5,1,9,5]])