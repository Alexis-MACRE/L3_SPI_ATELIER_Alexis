
#Auteur: Ezzaatari Zakaria
#Date: 07/09/2020
#Version: 1.0
#Description: Atelier de programmation 1 L3 SPI Info

def calcul_salaire():
    """Cette fonction permet de calculaire un salaire mensuel
    en fonction des heures majorées."""
    salaire_horaire = float(input("Saisir salaire horaire: "))
    nb_heures = int(input("Saisir nb heures travailles: "))
    salaire_mensuel=0
    if nb_heures <= 160 :
        salaire_mensuel = salaire_horaire * nb_heures
    elif nb_heures <= 200 :
        salaire_mensuel = salaire_horaire * 160 + salaire_horaire * (nb_heures - 160) * 1.25
    else :
        salaire_mensuel = salaire_horaire * 160 + salaire_horaire * 40 * 1.25 + salaire_horaire * (nb_heures - 200) * 1.5
    print(salaire_mensuel)

calcul_salaire()
        
