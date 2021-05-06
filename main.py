#!/usr/bin/python
# -*- coding: UTF-8 -*-
# jeu de la vie

from tkinter import *
import tkinter.font as font
import random
import os
from math import sqrt
from time import *

cellSize = 20
window = Tk()

#Fonction de fermeture de la fenêtre
def close_window ():
    window.destroy()

def drawGrille ():
    global canva
    canva.delete("all")
    width = 750/sqrt(len(vie))
    for entry in vie.items():
        i = entry[0][0]
        j = entry[0][1]
        val = entry[1]
        if val==1:
            canva.create_rectangle(i*width,j*width,i*width+width,j*width+width,outline="black",fill="red",width=1)
        else:
            canva.create_rectangle(i*width,j*width,i*width+width,j*width+width,outline="black",fill="white",width=1)

def init():
    random.seed(a=None, version=2)
    global vie
    global MAX
    MAX = slider1.get()
    vie = {}
    for i in range(MAX):
        for j in range(MAX):
            if int(random.randint(0,100))<slider2.get() :
                vie[(i,j)] = 1
            else:
                vie[(i,j)] = 0
    drawGrille()

#########################################################################
# nom : effectuer
# valeurs entree : le damier et sa taille
# valeurs sortie : damier modifié : nouvelle génération
# fonction : applique l'algorithme pour allez à la génération T+1.
#########################################################################
def effectuer():  # on fait une copie.
    tmp = vie.copy()
    for i in range(MAX):
        for j in range(MAX):
            vivant = 0
            if (tmp[((j + MAX - 1) % MAX, i % MAX)]):
                vivant += 1
            if (tmp[((j + MAX - 1) % MAX, (i + MAX - 1) % MAX)]):
                vivant += 1
            if (tmp[((j + MAX - 1) % MAX, (i + 1) % MAX)]):
                vivant += 1
            if (tmp[((j + 1) % MAX, i % MAX)]):
                vivant += 1
            if (tmp[((j + 1) % MAX, (i + MAX - 1) % MAX)]):
                vivant += 1
            if (tmp[(j + 1) % MAX, (i + 1) % MAX]):
                vivant += 1
            if (tmp[j % MAX, (i + MAX - 1) % MAX]):
                vivant += 1
            if (tmp[j % MAX, (i + 1) % MAX]):
                vivant += 1

            if (tmp[j, i]):
                if vivant < 2 or vivant > 3:
                    vie[(j, i)] = 0
            elif (vivant == 3):
                vie[(j, i)] = 1
    drawGrille()


#########################################################################
# nom : lancer_jeu
# valeurs entree : nombre de case du tableau.
# valeurs sortie : aucune
# fonction : initialiser le jeu et l'organiser.
#########################################################################
# lancer animation
def lancer_jeu():
    global stop
    stop = False
    boucle()

# boucle generant les generations
def boucle():
    global stop
    if(not stop):
        effectuer()
        time = 1000//slider3.get()

        window.after(time,boucle)

# Arrete l'animation
def stop():
    global stop
    stop = True

### Definition des widgets ###

window.title("SR01 Jeu de la Vie")
canva = Canvas(window,width = 750,height=750)
canva.pack(side=LEFT)
frame = Frame(window,width=200)

# Boutons

ft = font.Font(size=15)
Lancer = Button(frame,text = "Lancer",fg="blue",command =lancer_jeu)
Lancer['font']= ft


Arreter = Button(frame,text = "Arreter",fg="crimson",command=stop)
Arreter['font']= ft


Initialiser = Button(frame,text = "Initialiser",fg="blue",command=lambda: init())
Initialiser['font']= ft
Quitter = Button(frame,text = "Quitter",fg="crimson",command=close_window)
Quitter['font']= ft

slider1 = Scale(frame, label='Taille de la grille :', from_=10, to=50,fg="blue", orient=HORIZONTAL, length=200)
slider2 = Scale(frame, label='Pourcentage de vie :', from_=0, to=99,fg="blue", orient=HORIZONTAL, length=200)
slider3 = Scale(frame, label='vitesse :', from_=1, to=10,fg="blue", orient=HORIZONTAL, length=200)

Lancer.pack(fill=X)
Arreter.pack(fill=X)
Initialiser.pack(fill=X)
Quitter.pack(side=BOTTOM,fill=X)
slider3.pack(side=BOTTOM)
slider2.pack(side=BOTTOM)
slider1.pack(side=BOTTOM)
frame.pack(side=RIGHT,fill=Y)

#Lance une première fois init pour avoir une grille au lancement
init()

# lancement
window.mainloop()
