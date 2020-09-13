#Auteur: EZZAATARI Zakaria, MACRE Alexis
#Date: 08/09/2020
#Version: 1.0
#Description: Atelier de programmation 2 L3 SPI Info

#review jo: remplacer les nombres par des constantes 
def message_imc(imc:float)->str:
    """cette fonction interprete le IMC"""
    if imc<16.5:
        message="dénutrition ou famine"
    elif imc<18.5:
        message="maigreur"
    elif imc<25:
        message="corpulence normale"
    elif imc<30:
        message="surpoids"
    elif imc<35:
        message="obesite moderee"
    elif imc<40:
        message="obesite severe"
    else:
        message="obesite morbide"
    return message

def test(fonction:callable,valeurs:list)->None:
    """Cette fonction permet de tester le correcte fonctionnement de la fonction message_imc"""
    # Review: A quoi sert cette constante?
    TEST=[16,18,20,27,32,38,42]
    for i in range(0,len(valeurs)):
        print(fonction(valeurs[i]))
    

test(message_imc,[16,18,20,27,32,38,42])
    
