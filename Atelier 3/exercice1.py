def somme_avec_for1(L:list=[]) -> int:

     taille_liste = len(L)
     resultat_somme = 0
     
     for i in range (0,taille_liste):
          resultat_somme += L[i]

     return resultat_somme


def somme_avec_for2(L:list=[])->int:
     resultat_somme = 0

     for nombre in L:
          resultat_somme+=nombre
     
     return resultat_somme


def somme_avec_while(L:list=[])->int:
     i = 0
     resultat_somme = 0
     taille_liste = len(L)

     while i<taille_liste:
          resultat_somme += L[i]
          i+=1
     
     return resultat_somme

def test_exercice_1():
     print("TEST SOMME")
     #test liste vide
     print("Test liste vide:",somme_avec_while([]))
     #test somme 11111
     S=[1,10,100,1000,10000]
     print("Test somme 11111 : ",somme_avec_while(S)) 


def moyenne(L:list)->float:
     return somme_avec_for2(L)/len(L)

somme_avec_while()