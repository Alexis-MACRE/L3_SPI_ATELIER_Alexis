# Auteur(s) : Macre Alexis & Ezzaatari Zakaria
# Date : 16/09/2020
# Version : 1.0
# Description : Atelier de programmation 3 Exo 5 Python

def present(L:list,e:int)->bool:
     """Retourne True ou False si e est dans la liste L ou non"""
     return (e in L)


def present1(L:list,e:int)->bool:
     for i in range(0,len(L),1):        # range(len(L)) suffit
          if(L[i] == e):
               return True
          else:                         # On peut mettre ce else après le for et la fonction marche
               return False


def present2(L:list,e:int)->bool:
     b = True                           # Soit on l'initialise à False soit on ne le met pas 
     for i in range(0,len(L),1):        # range(len(L)) suffit
          if(L[i] == e):
               b = True
          else:                         # la condition else n'est pas nécéssaire si b est initialisé à False
               b = False                # sinon, si on a retiré b au début on peut juste décaler le else après le for
     return(b)

def present3(L:list,e:int)->bool:
     b = True                           # la variable n'est pas utilisée
     for i in range(0,len(L),1):        # range(len(L)) suffit
         return (L[i]==e)               # pas de moyen de faire fonctionner cette version là ? la fonction s'arrête après la première execution

def present4(L:list,e:int)->bool:
     b = False
     i = 0
     while (i<len(L) and b):            # la condition (and b) fait que l'on entre jamais dans la boucle, i<len(L) suffit
          if(L[i]==e): 
               b=True
          #i+=1                         il manque l'incrémentation de i
     return(b)


def test_present(fonction_present:callable):
     """Test les fonctions present"""
     liste_test = [1,2,3,4,5,6,7,8,9,10]

     succes_test = {
          "liste vide" : not fonction_present([],5),
          "debut"      : fonction_present(liste_test,1),
          "fin"        : fonction_present(liste_test,10),
          "milieu"     : fonction_present(liste_test,6),
          "absence"    : not fonction_present(liste_test,11)
     }

     for titre_test in succes_test:
          if succes_test[titre_test]:
               print("SUCCES: test",titre_test)
          else:
               print("ECHEC: test",titre_test)


def pos(L:list,e:int)->list:
     """Renvoie les positions des occurences e dans la liste L"""
     return [i for i in range(len(L)) if e == L[i]]

def pos1(L:list,e:int)->list:
     Lres = list(L)                          # L est déja une liste ; Si on initialise Lres à [], la fonction marche
     for i in range (0,len(L),1):            # range(len(L)) suffit
          if(L[i]==e):
               Lres+=[i]
     return Lres

def pos2(L:list,e:int)->list:
     Lres = list(L)                          # L est déja une liste ; Il faut initialiser Lres à []
     for i in range (0,len(L),1):            # range(len(L)) suffit
          if(L[i]==e):
               Lres[i]=i                     # Lres+=[i]
     return Lres

def pos3(L:list,e:int)->list:
     nb= L.count(e)
     Lres = [0]*nb
     for i in range (0,len(L),1):            # range(len(L)) suffit
          if(L[i]==e):
               Lres.append(i)                # Lres[i]=[i]
     return Lres

def pos4(L:list,e:int)->list:
     nb= L.count(e)
     Lres = [0]*nb   
     j = 0                        
     for i in range (0,len(L),1):            # range(len(L)) suffit
          if(L[i]==e):
               Lres[j]= i             
               #j+=1                         Il manque l'incrémentation de j
     return Lres


def test_pos(fonction_pos):
     """Test les fonctions pos"""
     liste_test = [1,1,3,4,5,5,7,8,10,10]

     succes_test = {
          "liste vide" : (fonction_pos([],5)==[]),
          "debut"      : (fonction_pos(liste_test,1)==[0,1]),
          "fin"        : (fonction_pos(liste_test,10)==[8,9]),
          "milieu"     : (fonction_pos(liste_test,5)==[4,5]),
          "absence"    : (fonction_pos(liste_test,11)==[])
     }

     for titre_test in succes_test:
          if succes_test[titre_test]:
               print("SUCCES: test",titre_test)
          else:
               print("ECHEC: test",titre_test)

