#Auteur : Alexis MACRE
#Date : 07/09/2020
#Version : 1.0
#Description : Atelier de programmation Exo 2 Python

def reconnaissance_caractere():
     """Cette fonction permet de reconnaître quel type de caractère le caractère saisi est grâce à son code ASCII"""
     cara = input("Saisir le caractere : ")
     if(cara >= '0' and cara <= '9') :
          print("C'est un chiffre")
     elif(cara >= 'A' and cara <= 'Z') :
          print("C'est une majuscule")
     elif(cara >= 'a' and cara <= 'z') :
          print("C'est une minuscule")
     else :
          print("C'est un caractere special")

reconnaissance_caractere()