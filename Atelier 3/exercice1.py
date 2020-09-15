# Auteur : Ezzaatari Zakaria & Alexis Macre
# Date : 14/09/2020
# Version : 1.0
# Description : Atelier de programmation 3 Exo 1 Python

from fonctions_persos import test_fonction

def somme_avec_for(L:list=[]) -> int:
     """Calcule la somme des éléments d'une liste en utilisant un for"""

     taille_liste = len(L)
     resultat_somme = 0
     
     for i in range (0,taille_liste):
          resultat_somme += L[i]

     return resultat_somme
     

def somme_avec_for_in(L:list=[])->int:
     """Calcule la somme des éléments d'une liste en utilisant un for in"""
     resultat_somme = 0

     for nombre in L:
          resultat_somme+=nombre
     
     return resultat_somme


def somme_avec_while(L:list=[])->int:
     """Calcule la somme des éléments d'une liste en utilisant un while"""
     i = 0
     resultat_somme = 0
     taille_liste = len(L)

     while i<taille_liste:
          resultat_somme += L[i]
          i+=1
     
     return resultat_somme

def test_exercice_1():
     """Fonction de test de l'énoncé"""

     print("TEST SOMME")
     #test liste vide
     print("Test liste vide:",somme_avec_while([]))
     #test somme 11111
     S=[1,10,100,1000,10000]
     print("Test somme 11111 : ",somme_avec_while(S)) 


def moyenne(L:list)->float:
     """Prend une liste de nombres et en retourne la moyenne (somme divisé par le nombre d'élements)"""
     nombre_d_elements = len(L)
     return somme_avec_for_in(L)/nombre_d_elements

def nb_sup_for(L:list,e:int)->int:
     """Prend une liste de nombres et retourne le nombre d'élements supérieurs à un entier e donné à l'aide d'un for

     Arguments:
     L -- liste de nombre
     e -- valeur minimale
     
     Retourne le résultat final du compteur
     """
     longueur = len(L)
     compteur = 0

     for i in range(longueur):
          if L[i]>e:
               compteur+=1
     
     return compteur

def nb_sup_for_in(L:list,e:int)->int:
     """Prend une liste de nombres et retourne le nombre d'élements supérieurs à un entier e donné à l'aide d'un for in

     Arguments:
     L -- liste de nombre
     e -- valeur minimale
     
     Retourne le résultat final du compteur
     """
     compteur = 0

     for elem in L:
          if elem > e:
               compteur+=1
     
     return compteur
     
def moy_supp(L:list,e:int)->float:
     """Fait la moyenne des nombres d'une liste supérieurs à un entier e
     
     Arguments:
     L -- liste de nombre
     e -- valeur minimale
     
     Retourne la somme des nombres superieurs à e divisé par le nombre d'élements supérieurs à e
     """
     somme = 0

     for nombre in L:
          if nombre > e:
               somme+=nombre
     return somme / nb_sup_for_in(L,e)

def val_max(L:list)->float:
     """Retourne la valeur max d'une liste d'élements"""
     return max(L)

def ind_max(L:list)->int:
     """Retourne l'indice de l'élement de la liste qui a la plus grande valeur"""
     return L.index(val_max(L))
     
