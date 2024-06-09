from tkinter import *
import math
from fonctionUtilitaire.Canevas import *
from fonctionUtilitaire.Solveur import Verifier_Grille
import time
##################################  CONSTANTES ##################################

R = 10          # rayon des cercles dessinés dans les hexagones
COUL = "white"  # couleur des cercles dessinés dans les hexagones
L_CLIQUE = []   # liste des hexagones où on a déjà cliqué
                # il contient l'id de l'hexagone et des points qui se trouvent dedans L_CLIQUE = [ [figure, points] ]

##################################  CONSTANTES ##################################


def Polygon_Click(event):
    "Lance la mise à jour de la matrice, le changement de couleur et la génération des points au clic"
    global L_CLIQUE

    objectId = event.widget.find_withtag('current')[0]
    tps1 = time.process_time()
    Ajout_Hexa_Clique(objectId)
    #print("M Before update ", M)
    Update_M(objectId)
    #print("M after update ", M)  
    Generer_Points(objectId)
    Verifier_Grille(M_NIVEAU)
    Changer_Couleur()
    tps2 = time.process_time()
    print("temps:",tps2-tps1)


def Ajout_Hexa_Clique(figure):
    "Ajoute l'hexagone dans la liste des cliqués s'il n'y est pas encore"
    global L_CLIQUE

    n = len(L_CLIQUE)
    flag = 0     # Vérifie si l'hexagone où on a cliqué est déjà dans la liste
    for i in range(n):
        if L_CLIQUE[i][0] == figure:
            flag = 1
            #print("Déjà cliqué")
            break
    if flag == 0:
        L_CLIQUE.append([figure])

    return L_CLIQUE

def Update_M(figure):
    "Mets à jour la matrice des hexagones (nbre de pts et couleur) au clic"
    global M
    LINE, COL = Find_Hexa(figure)
    if M[LINE][COL][2] != 0:
        n_pts = M[LINE][COL][1]
        color = M[LINE][COL][2]
        #print("n_pts : ",n_pts )
        #print ("color : ",color)
        if n_pts < 3:
            n_pts += 1
            color = 2
        else :
            n_pts = 0
            color = 1

        M[LINE][COL][1] = n_pts
        M[LINE][COL][2] = color

        #print("New n_pts : ",n_pts )
        #print ("New color : ",color)   

    return M
    

def Changer_Couleur():
    "Permet de changer la couleur des hexagones à partir d'un parcours de la matrice"
    for i in range(N_LIGNES):
        for j in range(N_HEXA):
            if M[i][j][2] != 0:
                num_coul = M[i][j][2]
                colorier_en = COULEUR [num_coul]
                print ("colorier_en ",colorier_en)
                figure = M[i][j][0]
                can1.itemconfig(figure, fill= colorier_en)
                Valider(figure)
                

            """
            0 -> Blue #318CE7 : COULEUR du canevas
            1 -> Blue clair #689EF9 : l'hexagone est affiché mais contient 0 point
            2 -> Blue foncé #0C306B: l'hexagone est affiché et contient des points
            """


def Valider(figure):
    "Permet de changer la couleur d'un hexagone lorsque sa ligne est validée"
    n = len(M_NIVEAU)
    flag = 0
    for i in range(n):
        L = M_NIVEAU [i]
        p = len(L)
        for j in range(3, p):
            if figure == L[j] and L[0] == 1:
                flag = 1
                break
    if flag == 1:
        #print("validé")
        can1.itemconfig(figure, outline = "#3DC54F", width = 7)
    else:
        #print("non validé")
        can1.itemconfig(figure, outline = CONTOUR, width = 2)

def Generer_Points(figure):
    "Génère les points dans les hexagones à partir d'un parcours de la matrice"
    global L_CLIQUE
    LINE, COL = Find_Hexa(figure) 
    if M[LINE][COL][2] != 0:
        n_pts = M[LINE][COL][1]
        print("n_pts à dessiner hexa ", n_pts)
        Clean(figure, n_pts)
        if n_pts != 0:   
            create_oval(figure, n_pts)               
    return L_CLIQUE

    
def Clean (figure, n_pts):
    "efface le contenu d'un hexagone avant de dessiner"
    global L_CLIQUE

    #print("L_CLIQUE before cleaning ",L_CLIQUE)
    n = len(L_CLIQUE)
    for i in range(n):
        if L_CLIQUE[i][0] == figure:
            if n_pts == 0 :
                k = 3
            else :
                k = n_pts - 1

            for j in range(k):
                p = len(L_CLIQUE[i])
                can1.delete(L_CLIQUE[i][p-1]) # on efface tous les points dessinés dans l'hexagone
                L_CLIQUE[i].pop()   # on enlève les points effacés de la liste
            break
    #print("L_CLIQUE after cleaning ",L_CLIQUE)
    return L_CLIQUE


def create_oval(figure, n_pts):
    """Dessine et positionne les cercles suivant le nombre de points dans un hexagone.
    Mets à jour L_CLIQUE en y ajoutant les id des points dessinés dans chaque hexagone"""
    
    global L_CLIQUE

    coordonnees = can1.coords(figure)
    #print ("coordonnes ", coordonnees)
    x = coordonnees[4]
    y = coordonnees[5]

    n = len(L_CLIQUE)
    for i in range(n):
        if L_CLIQUE[i][0] == figure:

            if n_pts == 1:    
                C1 = Cercle(x, y-C, R, COUL)
                L_CLIQUE[i].append(C1)

            else:
                C1 = Cercle(x+H/2, y-C, R, COUL)
                C2 = Cercle(x-H/2, y-C, R, COUL)
                L_CLIQUE[i].append(C1)
                L_CLIQUE[i].append(C2)

                if n_pts == 3:    
                    C3 = Cercle(x, y-C/2, R, COUL)
                    L_CLIQUE[i].append(C3)
            break

    return L_CLIQUE


def Cercle(x, y, R, COUL):
    "Dessine un seul cercle à partir des coordonnées du centre et du rayon"
    C = can1.create_oval(x+R, y+R, x-R, y-R, width=2, fill= COUL, outline=CONTOUR,tags='my_tag')
    return C