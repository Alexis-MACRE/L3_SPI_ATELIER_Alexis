#Auteur : Ezzaatari Zakaria & Alexis Macre
#Date : 08/09/2020
#Version : 1.0
#Description : Atelier de programmation 2 Exo 4 Python

from datetime import date

def est_bissextile(annee:int) -> bool :
     """Verifie si l'annee donnee en parametre est bissextile ou non et retourne un booleen"""
     return (annee%4 == 0 and annee%100!=0) or (annee%400 == 0)

def date_est_valide(jour:int,mois:int,annee:int) -> bool :
     """Verifie si la date entree est valide"""
     MOIS_31_JOURS=[1,3,5,7,8,10,12] 

     for i in range(0,len(MOIS_31_JOURS)):
          if mois==MOIS_31_JOURS[i]:
               jour_max = 31

     if (jour_max!=31 and mois!=2):
          jour_max = 30

     elif est_bissextile(annee):
          jour_max = 29
     
     else :
          jour_max = 28

     return (1<=jour<=jour_max and 1<=mois<=12)

def saisie_date_naissance() -> date :
     """Fonction de saisie de la date de naissance"""
     input_valide = False

     while(input_valide):
          print("------------------")
          print("Date de Naissance:")
          print("------------------")
          jour = int(input("Jour de naissance: "))
          mois = int(input("Mois de naissance: "))
          annee = int(input("Annee de naissance: "))

          if not date_est_valide(jour,mois,annee):
               print("\n Veillez rentrer une date valide\n")
          else:
               input_valide = True      

     return date(annee,mois,jour)    

def age(date_naissance:date)->int :
     age = (date_naissance.today() - date_naissance).days / 365.25
     
     return int(age)

def est_majeur(date_naissance:date)->bool :
     return ((date_naissance.today().year - date_naissance.year) > 18)

def test_acces() :
     date_saisie = saisie_date_naissance()
     mon_age = age(date_saisie)
     
     if(est_majeur(date_saisie)):
          print("Bonjour, vous avez",mon_age,"ans, accès autorisé")
     else :
          print("Désolé, vous avez",mon_age,"ans, vous ne pouvez pas entrer")  



def fonction_test(fonction:callable,valeurs:list,valeurs_attendues:list) -> None :
     """Permet de tester une fonction avec une liste de valeurs et celle des resultats attendus"""
     for i in range(0,len(valeurs)) :
          assert fonction(valeurs[i])==valeurs_attendues[i], "La valeur reçue n'est pas la bonne"
          print("Test numero :",i+1,"pour la valeur",valeurs[i],"le résultat est celui attendu (",fonction(valeurs[i]),")")


test_acces()
