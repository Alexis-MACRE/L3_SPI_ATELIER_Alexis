# import sys
# sys.path.append('../L3')
# import testfonction

def test_fonction(fonction:callable,valeurs:list,valeurs_attendues:list) -> None :
     """Permet de tester une fonction avec une liste de valeurs et celle des resultats attendus"""
     for i in range(len(valeurs)) :
          if fonction(valeurs[i])!=valeurs_attendues[i]:
               print("Test pour",valeurs[i],": Resultat Incorrect",fonction(valeurs[i]),"au lieu de",valeurs_attendues[i])
          else:
               print("Test pour",valeurs[i],": Resultat Correct",fonction(valeurs[i]))