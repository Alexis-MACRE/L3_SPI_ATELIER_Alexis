# Auteur(s) : Macre Alexis & Ezzaatari Zakaria
# Date : 16/09/2020
# Version : 1.0
# Description : Atelier de programmation 3 Exo 4 Python

import matplotlib.pyplot as plt
from fonctions_persos import test_fonction


def histo(F:list)->list:
     H = [0]*(max(F)+1)
     for nombre in F:
          H[nombre]+=1

     return H

def est_injective(F:list)->bool:
     injective = True

     for valeur in F:
          if valeur > 1:
               injective = False
     
     return injective

def est_surjective(F:list)->bool:
     surjective = True

     for valeur in F:
          if valeur < 1:
               surjective = False
     
     return surjective

def est_bijective(F:list)->bool:
     return (est_injective(F) and est_surjective(F))


def afficheHisto(F:list):

     H = histo(F)

     max_occu = max(H)

     print("\nHISTOGRAMME: \n\n\n")

     for i in range(max_occu,0,-1):
          for j in range(len(H)):
               if H[j]>=i:
                    print("  #  ",end="")
               else:
                    print("     ",end="")
          

          print("")
     
     for i in range(len(H)):
          print("|---|",end="")

     print("")

     for i in range(len(H)):
          print(" ",i," ",end="")


#afficheHisto([6,5,6,8,4,2,1,5,6,6])

     





#test_fonction(histo,[[6,5,6,8,4,2,1,5]],[[0,1,1,0,1,2,2,0,1]])
#test_fonction(est_injective,[[0,1,1,1,1,1,1,1],[2,2,2,2,2],[0,0,0,0,0,8,0],[1,1,1,1,1,1,1]],[True,False,False,True])
#test_fonction(est_surjective,[[0,1,1,1,1,1,1,1],[2,2,2,2,2],[0,0,0,0,0,8,0],[1,1,1,1,1,1,1]],[False,True,False,True])
#test_fonction(est_bijective,[[0,1,1,1,1,1,1,1],[2,2,2,2,2],[0,0,0,0,0,8,0],[1,1,1,1,1,1,1]],[False,False,False,True])