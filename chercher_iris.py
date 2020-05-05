# Auteur Ewan GRIGNOUX LEVERT
# 05/05/2020
# coding : utf-8
import matplotlib.pyplot as plt
import csv
import sys
import math

InputPL = float(input("Quel est la longueur des pétals de votre iris?"))
InputPW = float(input("Quel est la largeur des pétals de votre iris?"))
InputSL = float(input("Quel est la longueur des sépals de votre iris?"))
InputSW = float(input("Quel est la largeur des sépals de votre iris?"))
InputK = int(input("Combien de proches voisins voulez-vous prendre en compte?"))
InputD = input("Quel méthode de calcul vous voulez utilisez, la distance Euclidienne ou la distance Manhattan? E/M")

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
def distanceMath(xA,yA,xB,yB,zB,zA,tA,tB):
    '''
    Cette fonction renvoie la distance séparant les points A(xA,yA) et B(xB,yB)
    '''
    if InputD == 'E':
        return math.sqrt(math.pow(xB-xA,2)+math.pow(yB-yA,2)+math.pow(zB-zA,2)+math.pow(tB-tA,2))
    elif InputD == 'M':
        return math.sqrt(abs(xB-xA)+abs(yB-yA)+abs(zB-zA)+abs(tB-tA))
    else:
        print("Vous avez saisie une mauvaise lettre")

def distance(fleur1,fleur2):
    '''
    Cette fonction renvoie la distance entre deux fleurs
    en considérant la longueur et la larguer des pétales
    '''
    return distanceMath(float(fleur1['PetalLength']),float(fleur1['PetalWidth']),float(fleur2['PetalLength']),float(fleur2['PetalWidth']),float(fleur1['SepalLength']),float(fleur1['SepalWidth']),float(fleur2['SepalLength']),float(fleur2['SepalWidth']))


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

monIris ={'PetalLength':InputPL,'PetalWidth':InputPW, 'SepalLength':InputSL, 'SepalWidth':InputSW}
lesPLusProches = chercherPlusProches(monIris ,InputK)

Iris_setosa = 0
Iris_versicolor = 0
Iris_virginica = 0

for fleur in lesPLusProches:
    if fleur['Name'] == 'Iris-setosa':
        Iris_setosa += 1
    elif fleur['Name'] == 'Iris-versicolor':
        Iris_versicolor += 1
    elif fleur['Name'] == 'Iris-virginica':
        Iris_virginica += 1

Voisins = {"Iris-setosa":Iris_setosa, "Iris-versicolor":Iris_versicolor,"Iris-virginica":Iris_virginica}

def Types(Voisins):
    nbr_maxi = 0
    cle_maxi = ''
    for cle,valeur in Voisins.items():
        if valeur > nbr_maxi:
            nbr_maxi = valeur
            cle_maxi = cle
    return cle_maxi

print (f"Le type de votre iris est: {Types(Voisins)}")
sys.exit()