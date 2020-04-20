# -*- coding: utf-8 -*-
"""Jeu Quoridor

Ce programme permet de jouer au jeu Quoridor.

Examples:

    `> python3 main.py --help`

        usage: main.py [-h] [-l] idul

        Jeu Quoridor - phase 1

        positional arguments:
        idul          IDUL du joueur.

        optional arguments:
        -h, --help    show this help message and exit
        -l, --lister  Lister les identifiants de vos 20 dernières parties.

    `> python3 main.py josmi42`

        Légende: 1=josmi42, 2=robot
           -----------------------------------
        9 | .   .   .   .   2   .   .   .   . |
          |                                   |
        8 | .   .   .   .   .   .   .   .   . |
          |                                   |
        7 | .   .   .   .   .   .   .   .   . |
          |                                   |
        6 | .   .   .   .   .   .   .   .   . |
          |                                   |
        5 | .   .   .   .   .   .   .   .   . |
          |                                   |
        4 | .   .   .   .   .   .   .   .   . |
          |                                   |
        3 | .   .   .   .   .   .   .   .   . |
          |                                   |
        2 | .   .   .   .   .   .   .   .   . |
          |                                   |
        1 | .   .   .   .   1   .   .   .   . |
        --|-----------------------------------
          | 1   2   3   4   5   6   7   8   9

        Type de coup disponible :
        - D : Déplacement
        - MH: Mur Horizontal
        - MV: Mur Vertical

        Choisissez votre type de coup (D, MH ou MV) : D
        Définissez la colonne de votre coup : 5
        Définissez la ligne de votre coup : 2
"""
from api import lister_parties, initialiser_partie, jouer_coup
from quoridor_part_1 import afficher_damier_ascii, analyser_commande


if __name__ == '__main__':
    analyser_commande()

fonc = analyser_commande()
if fonc.lister == True:
    lister_parties(fonc.idul)

if fonc.lister == False:
    pass


tuple_id_état = initialiser_partie(analyser_commande().idul)
if len(tuple_id_état) > 1:
    afficher_damier_ascii(tuple_id_état[1])
    VAR = True
    while VAR:
        try:
            print("Type de coup disponible :\n- D : Déplacement\n- MH: Mur Horizontal\n- MV: Mur Vertical")
            a = input('Choisissez votre type de coup (D, MH ou MV) : ').upper()
            position_x = input('''Définissez la colonne de votre coup (axe x) : ''')
            position_y = input('''Définissez la ligne de votre coup (axe y) : ''')
            dico = jouer_coup(tuple_id_état[0], a, (position_x, position_y))
            if "message" in dico:
                raise RuntimeError
            if "gagnant" in dico:
                raise StopIteration
            if type(dico) == str:
                print(dico)
            afficher_damier_ascii(dico)
        except StopIteration as winner:
            VAR = False
            print(winner)
        except RuntimeError as err:
            print(err)
else:
    print(tuple_id_état)