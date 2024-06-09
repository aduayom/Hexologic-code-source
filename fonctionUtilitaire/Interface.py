from tkinter import *
import math
from fonctionUtilitaire.Interactions import Polygon_Click
from fonctionUtilitaire.Canevas import *

##################################  CONSTANTES ##################################
POL = 0  # récupère l'Id de l'hexagone créé
##################################  CONSTANTES ##################################   



def Init_M(N_LIGNES, N_HEXA):
    "Permet d'initialiser la matrice des hexagones"
    global M, L, x0, y0
    x0, y0 = 150, 100
    cpt = 0  # pour alterner le positionnement des hexagones
    for i in range(N_LIGNES):
        if cpt % 2 == 0:
            Ligne_Hexagones(x0, y0, N_HEXA)
            x0 = x0 + H
            cpt += 1
        else:
            Ligne_Hexagones(x0, y0, N_HEXA)
            x0 = x0 - H
            cpt += 1
        y0 = y0 + 3*C/2
        M.append(L)
    # print("M fini ", M)
    return M


def Ligne_Hexagones(x, y, N_HEXA):
    "Permet de créer des lignes d'hexagones et de les ajouter dans une liste"
    global L, x0, y0
    x = x0
    y = y0
    L = []
    Hexagone(x, y, C, COULEUR) # on dessine l'hexagone de départ de la ligne
    Hexa = [POL, 0, 0]
    L.append(Hexa)
    for i in range(1, N_HEXA):
        Ajout_Hexagones(L)
    print("Liste L ",L)
    return L


def Ajout_Hexagones(L):
    "Permet d'ajouter un hexagone à une ligne"
    #global L

    Xp = can1.coords(POL)[4]  # on récupère le centre de l'hexagone précédent
    Yp = can1.coords(POL)[5] - C 
    x = Xp + 2*H     # on définit le centre du prochain hexagone
    y = Yp

    Hexagone(x, y, C, COULEUR)      # on procède au dessin

    # on met à jour L en ajoutant le nouveau hexagone dessiné
    Hexa = [POL, 0, 0]  # lorsqu'un hexagone est créé, il contient 0 points
    #print("Hexa : ", Hexa)
    L.append(Hexa)
    return L


def Hexagone(x, y, C, COULEUR):
    "permet de dessiner un hexagone à partir de son centre, côté et couleur"
    global POL
    X = []
    Y = []
    for i in range(6):
        angle = 100 + math.radians(i*360/6)
        X.append(int(x+C*math.cos(angle)))
        Y.append(int(y+C*math.sin(angle)))
    POL = can1.create_polygon(X[0], Y[0], X[1], Y[1], X[2], Y[2], X[3], Y[3],
                          X[4], Y[4], X[5], Y[5], fill="", outline ="")

    can1.tag_bind(POL,'<Button-1>', Polygon_Click)
    return POL

