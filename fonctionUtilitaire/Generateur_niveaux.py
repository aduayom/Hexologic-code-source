from tkinter import *
import tkinter.font as font
from fonctionUtilitaire.Interface import *
from fonctionUtilitaire.Canevas import *
from fonctionUtilitaire.Solveur import Tout_est_valide
from tkinter.messagebox import *
##################################  CONSTANTES ##################################
NUM_NIV=0
NIVEAU=[
        [[0, 0, 3, 22]],
        [[0, 0, 3,21,22]],
        [[0, 0, 4,21,22,23]],
        [[0, 2, 4, 12, 21, 29],[0, 0, 8, 20,21, 22,23],[0, 2, 4, 23, 31]],
        [[0, 0, 2, 21, 22],[0, 1, 4, 21,28],[0, 2, 4, 22, 30]],
        [[0, 0, 6, 2, 3, 4, 5],[0, 1, 5, 5, 12, 20],[0, 2, 5, 4, 12, 21]],
        [[0, 0, 4, 12, 13],[0, 1, 5, 12,20],[0, 2, 5, 13, 22],[0, 2, 5, 20,28],[0, 1, 5, 22, 29]]        
        ]
LIMITE=len(NIVEAU)

##################################  CONSTANTES ##################################   


def Grille():
    "Récupère et initialise la grille d'un niveau"
    global NIVEAU
    ENTER=NIVEAU[NUM_NIV]
    n=len(ENTER)
    #print(ENTER)
    if len(M_NIVEAU)!=0:
        del M_NIVEAU[:]
    #print(M_NIVEAU)
    for i in range(0,n):
        #print(ENTER[i])
        M_NIVEAU.append(ENTER[i])
    print("M_NIVEAU: ",M_NIVEAU)
    return M_NIVEAU

def Niveau_suiv():
    "Permet de passer au niveau suivant"
    global NUM_NIV,LIMITE
    #print(NUM_NIV)
    RESULTAT=Tout_est_valide(M_NIVEAU)
    if RESULTAT==True and NUM_NIV<LIMITE :
        NUM_NIV += 1
        #print(NUM_NIV)
        Clean_Canvas(M_NIVEAU)
        message="Niveau "+str(NUM_NIV+1)+"\n Appuyez sur ok pour continuer"
        showinfo("NIVEAU SUIVANT", message, default='ok')
    return NUM_NIV

def Niveau_prec():
    "Permet de passer au niveau précédent"
    global NUM_NIV
    #print(NUM_NIV)
    RESULTAT=Tout_est_valide(M_NIVEAU)
    if RESULTAT==True and NUM_NIV>0 :
        NUM_NIV -= 1
        #print(NUM_NIV)
        Clean_Canvas(M_NIVEAU)
        message="Niveau "+str(NUM_NIV+1)+"\n Appuyez sur ok pour continuer"
        showinfo("NIVEAU PRECEDENT", message, default='ok')
    return NUM_NIV

def Clean_Canvas(M_NIVEAU):
    "Permet d'effacer le canvas pour un nouveau niveau"
    global M
    n = len(M_NIVEAU)
    for i in range(n):
        p = len(M_NIVEAU[i])
        #print("p ", p)
        for j in range(3, p):
            id_Hexa = M_NIVEAU[i][j]   
            can1.itemconfig(id_Hexa, fill="", outline = "")
            num_L = (id_Hexa-1) // N_HEXA
            indice = ((id_Hexa-1) % N_HEXA) - 1
            M[num_L][indice][2] = 0
            M[num_L][indice][1] = 0
    can1.delete('my_tag')
    return M

def Affiche_Hexa(id_Hexa):
    "Affiche un hexagone à partir de son id"
    global M
    for i in range(N_LIGNES):
        for j in range(N_HEXA):           
            if M[i][j][0] == id_Hexa :
                M[i][j][2] = 1
                #print("color ", id_Hexa, M[i][j][2])
                can1.itemconfig(id_Hexa, fill= COULEUR[1], outline = CONTOUR, width=2)
                break
    return M

def Affiche_Grille(M_NIVEAU):
    "Affiche la grille d'un niveau donné "
    global M
    n = len(M_NIVEAU)
    for i in range(n):
        p = len(M_NIVEAU[i])
        #print("p ", p)
        for j in range(3, p):
            id_Hexa = M_NIVEAU[i][j]   
            Affiche_Hexa(id_Hexa)
    All_Triangle(M_NIVEAU)
    return M

def All_Triangle(M_NIVEAU):
    "Dessine tous les triangles nécessaires de la grille"
    n = len(M_NIVEAU)
    for i in range(n):
        L = M_NIVEAU [i]
        direction = L[1]
        ponderation = L[2]
        last_hexa = L[-1]
        Triangle(direction, ponderation, last_hexa)


def Triangle(direction, ponderation, last_hexa):
    """Dessine un triangle suivant la direction de la ligne, sa ponderation et 
    les coordonnées de son dernier hexagone"""

    if direction == 0:
        r = Triangle_LH(direction, ponderation, last_hexa)
    if direction == 1:
        r = Triangle_LS(direction, ponderation, last_hexa)
    if direction == 2:
        r = Triangle_LAS(direction, ponderation, last_hexa)
    x1,y1,x2,y2,x3,y3,x,y = r
    can1.create_polygon(x1, y1, x2, y2, x3, y3, fill="white", outline = CONTOUR, width=2,tags='my_tag')
    can1.create_text(x, y, font=('Arial',15,'bold'), text = ponderation,tags='my_tag')

def Triangle_LH(direction, ponderation, last_hexa):
    "Détermine les parametres de déssin pour une ligne horizontale"
    x1 = can1.coords(last_hexa)[0]
    y1 = can1.coords(last_hexa)[1]
    x2 = can1.coords(last_hexa)[2]
    y2 = can1.coords(last_hexa)[3]
    x3 = x1 + H
    y3 = y1 + C/2
    y = y3
    x = x3 - H/2
    return x1,y1,x2,y2,x3,y3,x,y

def Triangle_LS(direction, ponderation, last_hexa):
    "Détermine les parametres de déssin pour une ligne slash"
    x1 = can1.coords(last_hexa)[4]
    y1 = can1.coords(last_hexa)[5]
    x2 = can1.coords(last_hexa)[6]
    y2 = can1.coords(last_hexa)[7]
    x3 = x2
    y3 = y2 + C
    y = y3 - C/2
    x = x3 + H/2
    return x1,y1,x2,y2,x3,y3,x,y

def Triangle_LAS(direction, ponderation, last_hexa):
    "Détermine les parametres de déssin pour une ligne en anti slash"
    x1 = can1.coords(last_hexa)[2]
    y1 = can1.coords(last_hexa)[3]
    x2 = can1.coords(last_hexa)[4]
    y2 = can1.coords(last_hexa)[5]
    x3 = x1
    y3 = y1 + C
    y = y3 - C/2
    x = x3 - H/2
    return x1,y1,x2,y2,x3,y3,x,y



