from tkinter import *

##################################  CONSTANTES ##################################
x0 = 150   # on initialise le centre d'un hexagone
y0 = 100
C = 50   # coté d'un hexagone
COULEUR = ["#318CE7", "#689EF9", "#29DCE9"]
CONTOUR = "white"
H = (C/2)*(3)**(1/2)
N_HEXA = 8
N_LIGNES = 5
M = []
L = []
M_NIVEAU = [] # représente la grille de chaque niveau
COL = 0        # colonne et ligne de l'emplacement d'un hexagone dans la matrice M
LINE = 0
##################################  CONSTANTES ##################################

def Find_Hexa(id_Hexa):
    "Permet de retrouver un hexagone dans la matrice M à partir de son id"
    global COL, LINE
    LINE = (id_Hexa-1) // N_HEXA
    COL = ((id_Hexa-1) % N_HEXA) - 1
    return LINE, COL

Fenetre = Tk()
Fenetre.title('Hexologic')

label = Label(Fenetre, text="BIENVENUE DANS HEXOLOGIC !", bg="#F6F9C4")
label.pack()
image = PhotoImage(file='HEXOLOGIC_V3\HEXOLOGIC V2_3\HEXOLOGIC_VersionFinale\images\hexologic.png', master=Fenetre) #id = 1
can1 = Canvas(Fenetre, width=1000, height=500, bg='#318CE7')
can1.create_image((500, 300), image=image)
can1.pack(side=TOP, padx=5, pady=5)