
#Auteur: Ezzaatari Zakaria
#Date: 07/09/2020
#Version: 1.0
#Description: Atelier de programmation 1 L3 SPI Info

def imposable() :
    """Cette fopnction permet de verifier si un citoyen est imposable en fontion de l'age et du sexe"""
    sexe=input("Saisir homme ou femme (H ou F):" )
    age=int(input("Saisir age :"))
    if sexe=="H" and age>20: #vous auriez pu faire plus court (en mettant les deux dans une seule proposition par ex)
        imposable=True
    elif sexe=="F" and age>=18 and age <=35: #pareil que dans l'exo du salaire, vous auriez pu mettre des constantes (pour les âges notamment)
        imposable=True
    else :
        imposable=False
    print(imposable)
imposable()

#plutôt que if.... imposable = true, vous auriez directeemnt pu mettre imposable = (la condition)
