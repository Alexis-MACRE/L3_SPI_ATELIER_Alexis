import random

min = 0
max = 200

def plusoumoins():
    randomNomber = random.randint(min, max)
    finduJeu = False
    coup = 1
    while not (finduJeu) and (coup < 11):
        monNbr = int(input("Entrez en nombre: "))
        if (monNbr > randomNomber):
            print("trop grand")
        elif (monNbr < randomNomber):
            print("trop petit")
        else:
            print ("Tu gagnes en ", coup, "coup(s)")
            finduJeu = True            
        coup += 1

    if (coup > 10):
         print("perdu")


plusoumoins()