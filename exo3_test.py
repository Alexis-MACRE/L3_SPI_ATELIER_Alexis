#Auteur : Alexis MACRE
#Date : 07/09/2020
#Version : 1.0
#Description : Atelier de programmation Exo 3 Python

def imposable() :
     sexe=input("H ou F ? ")
     age=int(input("quel age ? "))

     if(sexe == "H" and age>20) :
          imposable = True
     elif(sexe == "F" and age >= 18 and age <= 35) :
          imposable = True
     else :
          imposable = False
     
     print(imposable)

imposable()