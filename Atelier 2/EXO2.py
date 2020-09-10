#Auteur : Alexis MACRE
#Date : 08/09/2020
#Version : 1.0
#Description : Atelier de programmation 2 Exo 2 Python

def est_bissextile(annee:int) -> bool :
     """Verifie si l'annee donnee en parametre est bissextile ou non et retourne un booleen"""
     return (annee%4 == 0 and annee%100!=0) or (annee%400 == 0)

def fonction_test(fonction:callable,valeurs:list,valeurs_attendues:list) -> None :
     """Permet de tester une fonction avec une liste de valeurs et celle des resultats attendus"""
     for i in range(0,len(valeurs)) :
          assert fonction(valeurs[i])==valeurs_attendues[i], "La valeur reçue n'est pas la bonne"
          print("Test numero :",i+1,"pour la valeur",valeurs[i],"le résultat est celui attendu (",fonction(valeurs[i]),")")

fonction_test(est_bissextile,[1600,2000,1515,1300],[True,True,False,False])
