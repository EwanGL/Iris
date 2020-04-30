# Auteur P.Vincent
# 28/04/2020
# coding : utf-8
import matplotlib.pyplot as plt
import csv
import sys
import math

# recupération des données dans le fichier iris.csv
def lireFichierCSV(nomFichier):
    '''
    Cette fonction lit les données du fichier "nomFichier"
    Le fichier lu est un tableau de valeurs séparées par ;
    L ensemble des données va être stocké dans un tableau
    Chaque ligne (= iris) est enregistrée sous forme de dictionnaire
    '''    
    tableau = []

    with open(nomFichier, newline = '') as fichier :
        lecteur = csv.DictReader(fichier, delimiter=',') 
        for element in lecteur:
            tableau.append(element)            
    return tableau
    
iris = lireFichierCSV("iris.csv")

# Algorithme k plus proche voisins
def distanceMath(xA,yA,xB,yB):
    '''
    Cette fonction renvoie la distance séparant les points A(xA,yA) et B(xB,yB)
    '''
    return math.sqrt(math.pow(xB-xA,2)+math.pow(yB-yA,2))

assert(distanceMath(3,0,0,4)==5.0)
assert(distanceMath(3,0,6,0)==3.0)
assert(distanceMath(0,0,2,1)==2.23606797749979)

def distance(fleur1,fleur2):
    '''
    Cette fonction renvoie la distance entre deux fleurs
    en considérant la longueur et la larguer des pétales
    '''
    return distanceMath(float(fleur1['PetalLength']),float(fleur1['PetalWidth']),float(fleur2['PetalLength']),float(fleur2['PetalWidth']))


def chercher_mini(uneFleur,indice_depart):
    '''
    Cette fonction renvoie l'indice de la fleur la plus proche de maFleur
    Elle parcours la liste d'iris à partir du rang indice_depart
    '''
    mini = 10000000
    indice_mini = indice_depart
    for indice in range (indice_depart, len(iris)):
        dist = distance(uneFleur, iris[indice])
        if dist < mini:
            mini = dist
            indice_mini = indice
    return indice_mini

def permuter(indice1, indice2):
    '''
    cette fonction permute deux fleurs dans la liste des iris
    '''
    global iris
    temp  = iris[indice1]
    iris[indice1] = iris[indice2]
    iris[indice2] = temp

def chercherPlusProches(uneFleur, k):
    global iris
    a_classer = 0
    while a_classer < k:
        mini = chercher_mini(uneFleur, a_classer)
        permuter(a_classer, mini)
        a_classer = a_classer + 1
    return  iris[0:k]

monIris ={'PetalLength':5.0,'PetalWidth':1.7}
lesPLusProches = chercherPlusProches(monIris ,5)
for fleur in lesPLusProches:
    print(fleur['Name'])

sys.exit()