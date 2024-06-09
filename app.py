from tkinter import *
from fonctionUtilitaire.Interface import *
from fonctionUtilitaire.Interactions import *
from fonctionUtilitaire.Generateur_niveaux import *
from fonctionUtilitaire.Solveur import *
from fonctionUtilitaire.Canevas import *
import pygame

pygame.mixer.init()
 
mon_audio=pygame.mixer.Sound("HEXOLOGIC_V3\HEXOLOGIC V2_3\HEXOLOGIC_VersionFinale\son\jeux.mp3")
mon_audio.set_volume(1)

Init_M(N_LIGNES, N_HEXA)

def lancer():
    "Permet de lancer la musique"
    mon_audio.set_volume(1)
    mon_audio.play()
     
def couper():
    "Permet de couper la musique"
    mon_audio.set_volume(0)

def Jouer():
    "Permet de démarrer le jeu/afficher grile"
    M_NIVEAU= Grille()
    #print("M_NIVEAU ", M_NIVEAU)
    Affiche_Grille(M_NIVEAU)


boutton1 = Button(Fenetre, text='JOUER', width=20, height=2, command = Jouer, bg="#0CBE44")
boutton1.pack(padx=50, pady=5)


Button(Fenetre,text="Son",command=lancer, width=40).pack(padx=50, pady=5)
Button(Fenetre,text="Couper",command=couper, width=40).pack(padx=50, pady=5)

boutton2 = Button(Fenetre, text='NIVEAU PRECEDENT', width=20, height=2, command = Niveau_prec, bg="#BE3EAA")
boutton2.pack(side=LEFT, padx=50, pady=5)

boutton3 = Button(Fenetre, text='NIVEAU SUIVANT', width=20, height=2, command = Niveau_suiv, bg="#983EBE")
boutton3.pack(side=RIGHT, padx=50, pady=5)


Fenetre.mainloop()  # reception événement