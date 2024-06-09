"""

CONSTANTES :
-> Toutes les constantes sont écrits en majuscule
-> Les constantes sont définis au tout début du fichier après les importations

PROGRAMME PRINCIPAL:
-> Il contient la création des canevas
-> Il est défini à a fin des fichiers

FONCTIONS:
-> Le com de chaque fonction commence par une lettre majuscule
-> On utilise les underscores (tiret du 8) quand le nom est composé


COULEUR : = ["#318CE7", "#689EF9", "#29DCE9"]
0 -> #318CE7 : COULEUR du canevas
1 -> Blue clair #689EF9 : l'hexagone est affiché mais contient 0 point
2 -> Blue foncé #0C306B: l'hexagone est affiché et contient des points


HEXAGONES : 
-> Chaque hexagone est représenté par une liste : Hexa = [id, 0, 0] 
-> La liste contient l'Id de l'hexagone Hexa[0]
                    le nombre de point qu'il contient Hexa[1]
                    et sa COULEUR Hexa[2]
-> On ne peut générer plus de 3 points dans un hexagone

MATRICE M D’HEXAGONES :
-> contient des lignes représentées par L
-> Chaque L contient des hexagones L = [[id1, 0, 0], [id2, 0, 0]]
-> on a M = [   [[id1, 0, 0], [id2, 0, 0]]
                [[id3, 0, 0], [id4, 0, 0]]  ] 

LIGNE GRILLE
les lignes de la grille sont représentées par des listes L contenant :
-> L'état L[0] : validée 1 ou non 0
-> La direction : L[1]
    avec : *** 0 : l'horizontale -------
            ** 1 : une diognale en slash /
            ** 2 : une diagonale en anti slash \
-> la pondération : L[2]
-> les id des hexagones de la ligne

GRILLE DE NIVEAU :
La grille de chaque niveau est représentée par une matrice M_NIVEAU
contenant les listes L de chaque ligne de la grille
"""