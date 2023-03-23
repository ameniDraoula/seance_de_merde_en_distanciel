nbr=0   # on a declarer un nbr initialiser a 0
global somme # puis on a declarer une variable globale pour qu'elle soit visible sur tt le projet 
nbr= int(input("saisir un nbre entier  ") ) # nbr recoit la conversion d'un nbre entier saisi par l'utilisateur
def my_function_somme(): # on a definit une fonction qui va faire le calcule du somme
        somme=0 #  on a utiliser la variable globale somme et on a initialiser a 0
        while somme <5: # la on a met un condition d'arret pour faire la somme 4fois
              somme = somme+ nbr
              print(somme)# l'affichage du somme
my_function_somme()
