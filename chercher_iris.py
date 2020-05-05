# Auteur Ewan GRIGNOUX LEVERT
# 05/05/2020
# coding : utf-8
import matplotlib.pyplot as plt
import csv
import sys
import math
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title('Iris')
root.geometry("800x400+200+0")
root.config(bg = '#06B70E')

PL = Label(root, text='Quel est la longueur des pétals de votre iris?',bg = '#06B70E', fg='white')
PL.grid(row=0, column=0, padx=5,pady=5)
PL_nbr = Entry(root, textvariable='Quel est la longueur des pétals de votre iris?')
PL_nbr.grid(row=1, column=0,padx=5,pady=5)

PW = Label(root, text='Quel est la largeur des pétals de votre iris?',bg = '#06B70E', fg='white')
PW.grid(row=0, column=1, padx=5,pady=5)
PW_nbr = Entry(root, textvariable='Quel est la largeur des pétals de votre iris?')
PW_nbr.grid(row=1, column=1,padx=5,pady=5)

SL = Label(root, text='Quel est la longueur des sépals de votre iris?',bg = '#06B70E', fg='white')
SL.grid(row=2, column=0, padx=5,pady=5)
SL_nbr = Entry(root, textvariable='Quel est la longueur des sépals de votre iris?')
SL_nbr.grid(row=3, column=0,padx=5,pady=5)

SW = Label(root, text='Quel est la largeur des sépals de votre iris?',bg = '#06B70E', fg='white')
SW.grid(row=2, column=1, padx=5,pady=5)
SW_nbr = Entry(root, textvariable='Quel est la largeur des sépals de votre iris?')
SW_nbr.grid(row=3, column=1,padx=5,pady=5)

K = Label(root,text='Combien de proches voisins voulez-vous prendre en compte?',bg = '#06B70E', fg='white')
K.grid(row=4, column = 0, padx=5, pady=5)
K_nbr = Spinbox(root, from_=1, to=20)
K_nbr.grid(row=5, column=0, padx=5,pady=5)

calculs = ['Euclidienne','Manhattan']
D = Label(root, text='Quel méthode de calcul de distance voulez-vous utilisez?',bg = '#06B70E', fg='white')
D.grid(row=4, column=1, padx=5,pady=5)
D_nbr = ttk.Combobox(root, value=calculs, width=10)
D_nbr.current(1)
D_nbr.grid(row=5, column=1, padx=5, pady=5)


def Start():
    global img
    InputPL = float(PL_nbr.get())
    InputPW = float(PW_nbr.get())
    InputSL = float(SL_nbr.get())
    InputSW = float(SW_nbr.get())
    InputK =  int(K_nbr.get())
    InputD = D_nbr.get()


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
        if InputD == 'Euclidienne':
            return math.sqrt(math.pow(xB-xA,2)+math.pow(yB-yA,2)+math.pow(zB-zA,2)+math.pow(tB-tA,2))
        elif InputD == 'Manhattan':
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
        #global iris
        temp  = iris[indice1]
        iris[indice1] = iris[indice2]
        iris[indice2] = temp

    def chercherPlusProches(uneFleur, k):
        #global iris
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

    types = Types(Voisins)
    rep = Label(root, text=f'Le type de votre iris est {types}', bg = '#06B70E',fg='white')
    rep.grid(row=6, column=1, padx=5, pady=5)

    imgsetosa = Image.open('Iris-setosa.png')
    setosa = ImageTk.PhotoImage(imgsetosa)
    imgversicolor = Image.open('Iris-versicolor.png')
    versicolor = ImageTk.PhotoImage(imgversicolor)
    imgvirginica = Image.open('Iris-virginica.png')
    virginica = ImageTk.PhotoImage(imgvirginica)

    if types == 'Iris-setosa':
        img = setosa
    elif types == 'Iris-versicolor':
        img = versicolor
    elif types == 'Iris-virginica':
        img = virginica

    image = Label(root, image=img)
    image.grid(row=7, column=1, padx=5, pady=5)

start = Button(root, text='Chercher', command=Start)
start.grid(row=6, column=0, padx=5, pady=5)

root.mainloop()
sys.exit()