#Auteur: EZZAATARI Zakaria, MACRE Alexis
#Date: 08/09/2020
#Version: 1.0
#Description: Atelier de programmation 2 L3 SPI Info
import math

def discriminant(a:float,b:float,c:float)->float:
    """Cette fonction calcule le discirmant d'une equation du second degre"""
    delta=b*b-4*a*c
    return delta

def racine_unique(a:float,b:float)->float:
    """Cette fonction permet de calculer l'unique racine d'une equation du second degre"""
    x=(-b)/(2*a)
    return x

def racine_double(a:float,b:float,delta:float,num:int)->float:
    """Cette fonction permet de calculer un des deux racines d'une equation du second degre
    en fonction de num"""
    if num==1:
        x=(-b+sqrt(delta))/(2*a)
    else:
        x=(-b-sqrt(delta))/(2*a)
    
    return x

def str_equation(a:float,b:float,c:float)->str:
    """Cette fonction permet d'ecrire une chaine de caracteres contenant une equation de second degre
    a partir de 3 nombres reels """
    equation="%.2fx2+%.2fx+%.2f=0" % (a,b,c)
    return equation

def solution_equation(a:float,b:float,c:float)->str:
    """Cette fonction determine le nombre de solutions pour une equation de second degre"""
    delta=discriminant(a,b,c)
    equation=str_equation(a,b,c)
    solution="Solution de l'equation "+equation
    if delta<0:
        solution+="\n Pas de racine reelle"
    elif delta==0:
        x=racine_unique(a,b)
        solution+="\nRacine unique x=%f" %(x)
    else:
        x1=racine_double(a,b,delta,1)
        x2=racine_double(a,b,delta,2)
        solution+="\nDeux recines:\n x1=%f \nx2=%f" %(x1,x2)
    return solution

def equation(a:float,b:float,c:float)->None:
    """Cette fonction affiche l'equation de second degre et ses solutions"""
    print(solution_equation(a,b,c))

def test()->None:
    """Cette fonction permet de tester le correcte fonctionnement de la fonction message_imc"""
    a=float(input("Saisir premier coeff:"))
    b=float(input("Saisir deuxieme coeff:"))
    c=float(input("Saisir troixieme coeff:"))
    equation(a,b,c)

test()