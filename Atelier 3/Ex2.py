#Auteur : Zakaria Ezzaatari et Alexis MACRE
#Date : 14/09/2020
#Version : 1.0
#Description : Atelier de programmation 3

def position_for(L:list,e:int)->int:
    """Cette fonction permet de determiner l'indice de l'entier e dans la liste L 
    utilisant la boucle for """
    longeur=len(L)
    pos_e=-1
    for i in range(0,longeur):
        if L[i]==e:
            pos_e=i
    return pos_e


def position_while(L:list,e:int)->int:
    """Cette fonction permet de determiner l'indice de l'entier e dans la liste L 
    utilisant la boucle while """
    longeur=len(L)
    pos_e=-1
    i=0
    found=False
    while not found:
        if L[i]==e:
            pos_e=i
            found=True
        i+=1
        if i>=longeur:
            pos_e=-1
            found=True
    return pos_e

def nb_occurrences(L:list,e:int)->int:
    """Cette fonction permet de determine le nombre d'occurance d'un entier e dans une liste L"""
    longeur=len(L)
    nb_e=0
    for i in range (0,longeur):
        if L[i]==e:
            nb_e+=1
    return nb_e

def est_triee_for(L:list)->bool:
    """Cette fontion admet une liste L d'entiers et utilisant une boucle for retourne un 
    booléen vrai si la liste est croissante, faux sinon."""
    trie=False
    longeur=len(L)
    for i in range (1,longeur):
        if L[i]<L[i-1]:    
            trie=False
            break
    else:
        trie=True
    return trie

def est_triee_while (L:list)->bool:
    """Cette fontion admet une liste L d'entiers et utilisant une boucle while retourne un 
    booléen vrai si la liste est croissante, faux sinon."""
    trie=False
    fin=False
    i=0
    longeur=len(L)
    while not fin:
        if i>=longeur:
            trie=True
            fin=True
        elif i!=0 and L[i]<L[i-1]:
            trie=False
            fin=True
        i+=1
    return trie

def location_tri(L:list,e:int)->int:
    """Cette fonction permet de determiner l'indice de l'entier e dans la liste L 
    utilisant l'algorithme de recherche dichotomique' """
    pos_e=-1
    if est_triee_for(L):
        deb=0
        fin=len(L)-1
        res=False
        while not res and deb<fin:
            mil=(deb+fin)//2
            if L[mil]==e:
                pos_e=mil
                res=True
            elif e>L[mil]:
                deb=mil+1
            else:
                fin=mil-1
    return pos_e
        
def a_repetitions(L:list)->bool:
    """Cette fonction permet de determiner s'il y des valeurs 
    qui se repetent dans la liste L"""
    T=[]
    found=False
    i=0
    longeur=len(L)
    repetition=False
    while not found and i<longeur:
        if L[i] in T:
            repetition=True
            found=True
        else:
            T.append(L[i])
        i+=1
    return repetition
       

