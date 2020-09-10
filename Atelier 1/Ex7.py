#Auteur: Ezzaatari Zakaria
#Date: 08/09/2020
#Version: 1.0
#Description: Atelier de programmation 1 L3 SPI Info

def election_candidat_1():
    """ Cette fonction permet de saisir les suffrages obtenu par 4 candidat 
    et de verifier si le premier candidat est elu,battu en ballotage favorable ou deavorable """
    candidat =[0 , 0 , 0 , 0]
    second_tour=True
    favorable=True
    for i in range (0,4):
        candidat[i]=float(input("Saisir le score en pourcentage pour le candidat :"))
        if candidat[i]>50:
            second_tour=False

    if candidat[0]>50 :
        print("Le premier candidat a gagne")
    elif second_tour==False or candidat[0]<12.5 :
        print("Le premier candidat a perdu")
        second_tour=False
    else:
        for i in range(1,4):
            if candidat[i]>=12.5 and candidat[i]>candidat[0]:
                favorable=False
    
    if favorable and second_tour==True:
        print("Le premier candidat se trouve en ballottage favorable")
    elif second_tour==True:
        print("Le premier candidat se trouve en ballottage defavorable")

election_candidat_1()
             
#test avec 2,1,1,1 perdu
#test avec 50,10,10,30 favorable
#test avec 60,10,10,20 gagne
#test avec 20,30,20,30 defavorable 
