from tkinter import *
from fonctionUtilitaire.Interactions import *
from fonctionUtilitaire.Canevas import *
from time import *
##################################  CONSTANTES ##################################
M_NIVEAU = [] # représente la grille de chaque niveau
##################################  CONSTANTES ##################################  


def Verifier_Grille(M_NIVEAU):
    "Vérifie si toute la grille est soldée"
    print("Verifier_Grille(M_NIVEAU) ", M_NIVEAU)
    n = len(M_NIVEAU)
    for i in range(n):
        L = M_NIVEAU [i]
        Verifier_Ligne(L)


def Verifier_Ligne(L):
    """Vérifie la correspondance entre la pondération d'une ligne 
    et le nombre de points qu'elle contient """
    #print("L ", L)
    somme = 0
    n = len(L)
    for i in range(3, n):
        LINE, COL = Find_Hexa(L[i])
        pts = M[LINE][COL][1]
        somme += pts
        #print ("somme ", somme)

    print("somme total ligne ", somme)
    print("somme attendu ", L[2])
    if somme == L[2] :
        L[0] = 1    # état = validé
    else:
        L[0] = 0    # état = non validé
    #print("L ", L)
    return L

def Tout_est_valide(M_NIVEAU):
    "Permet de vérifier si toute la grille est validée"
    cpt=0
    for i in range (0,len(M_NIVEAU)):
        if M_NIVEAU[i][0]==1:
            cpt=cpt+1
    if cpt==len(M_NIVEAU):
        print("Tout est validé")
        return True
    else:
        return False
