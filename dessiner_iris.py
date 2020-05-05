# Auteur P.Vincent
# 28/04/2020
# coding : utf-8
import matplotlib.pyplot as plt
import csv
import sys

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

# Création du graphique
def creerGraphique():
    for fleur in iris :
        abscisse = float(fleur['PetalLength'])
        ordonnee = float(fleur['PetalWidth'])
        
        if fleur['Name'] == 'Iris-setosa':
            couleur = 'blue'
        elif fleur['Name'] == 'Iris-versicolor':
            couleur = 'yellow'
        elif fleur['Name'] == 'Iris-virginica':
            couleur ='lime'
        forme = '.'
        plt.plot(abscisse, ordonnee, marker = forme, color = couleur)

creerGraphique()

# Réglages du graphique
plt.title("Pétales des iris")
plt.xlabel('Longueur en cm')
plt.ylabel('Largeur en cm')

# Affichage du graphique
plt.show()
sys.exit()