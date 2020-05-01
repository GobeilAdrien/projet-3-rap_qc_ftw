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
from quoridor import Quoridor
from QuoridorX import QuoridorX
import argparse


def analyser_commande():
    """Génère un analyseur de ligne de commande
    En utilisant le module argparse, génère un analyseur de ligne de commande.
    L'analyseur offre (1) argument positionnel.
        idul: IDUL du joueur.
    Ainsi que les (2) arguments optionnel:
        help: show this help message and exit
        lister: Lister les identifiants de vos 20 dernières parties.
    Returns:
        Namespace: Retourne un objet de type Namespace possédant
            les clef «idul» et «lister».
    """
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 3')
    parser.add_argument(
        'idul', metavar='idul',
        help='IDUL du joueur.')
    parser.add_argument(
        '-l', '--lister',
        action='store_true',
        help='Lister les identifiants de vos 20 dernières parties.')
    parser.add_argument('-a', '--automatique', action="store_true",\
        help="Activer le mode automatique")
    parser.add_argument('-x', '--graphique', action="store_true",\
        help="Activer le mode graphique")
    return parser.parse_args()

def afficher_damier_ascii(grille):
    """Afficher le damier

    Ne faites preuve d'aucune originalité dans votre «art ascii»,
    car votre fonction sera testée par un programme et celui-ci est
    de nature intolérante (votre affichage doit être identique à
    celui illustré). Notez aussi que votre fonction sera testée
    avec plusieurs états de jeu différents.

    Args:
        grille (dict): Dictionnaire représentant l'état du jeu.

    Examples:
        >>> grille = {
                "joueurs": [
                    {"nom": "idul", "murs": 7, "pos": [5, 5]},
                    {"nom": "automate", "murs": 3, "pos": [8, 6]}
                ],
                "murs": {
                    "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
                    "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
                }
            }
        >>> afficher_damier_ascii(grille)

            Légende: 1=idul, 2=automate
                 -----------------------------------
              9 | .   .   .   .   .   .   .   .   . |
                |                                   |
              8 | .   .   .   .   .   . | .   .   . |
                |        ------- -------|-------    |
              7 | . | .   .   .   .   . | .   .   . |
                |   |                               |
              6 | . | .   .   .   .   . | .   2   . |
                |    -------            |           |
              5 | .   .   . | .   1   . | .   .   . |
                |           |                       |
              4 | .   .   . | .   .   .   .   .   . |
                |            -------                |
              3 | .   .   .   .   . | .   .   .   . |
                |                   |               |
              2 | .   .   .   .   . | .   .   .   . |
                |                                   |
              1 | .   .   .   .   .   .   .   .   . |
              --|-----------------------------------
                | 1   2   3   4   5   6   7   8   9`
    """

    # Construction du damier
    damier = [
        ['.' if x % 4 == 0 else ' ' for x in range(39)]
        if y % 2 == 0 else [' ' for x in range(39)] for y in range(17)
    ]
    for i, ligne in enumerate(damier[::2]):
        ligne[0] = str(9-i)
    for ligne in damier:
        ligne[2] = ligne[-1] = '|'
    # Position des joueurs
    for i in range(2):
        x, y = grille['joueurs'][i]['pos']
        damier[(9-y)*2][x*4] = str(i+1)
    # Murs horizontaux
    for x, y in grille['murs']['horizontaux']:
        for i in range(7):
            damier[(9-y)*2+1][x*4+i-1] = '-'
    # Murs verticaux
    for x, y in grille['murs']['verticaux']:
        damier[(9-y)*2][x*4-2] = \
            damier[(9-y)*2-1][x*4-2] = \
            damier[(9-y)*2-2][x*4-2] = '|'

    debut = '   {}'.format('-' * 35)
    milieu = '\n'.join(''.join(spot for spot in ligne) for ligne in damier)
    fin1 = '--|{}'.format('-' * 35)
    fin2 = '  | {}'.format('   '.join(str(x + 1) for x in range(9)))

    print('\n'.join([debut, milieu, fin1, fin2]))


if __name__ == '__main__':
    analyser_commande()

fonc = analyser_commande()
if fonc.lister == True:
    lister_parties(fonc.idul)

if fonc.lister == False:
    pass

def quoridorgame(arg):
    """ Fonction servant a jouer au jeu """
    idul = arg.idul
    # Mode manuel
    if not (arg.automatique or arg.graphique):
        etat_jeu = initialiser_partie(idul)
        print(afficher_damier_ascii(etat_jeu[1]))
        print('Quel coup désirer vous jouer ?')
        print("Deplacement pion: D , Mur Horizontal : MH, Mur Vertical : MV ")
        coup = input()
        print('Quel position sur le plateau désirer vous placer votre pièce?')
        print('(x,y)')
        position = input()
        etat_jeu_2 = jouer_coup(etat_jeu[0], coup, position)
        print(afficher_damier_ascii(etat_jeu_2))
        while 1:
            print('Quel coup désirer vous jouer ?')
            print("Deplacement pion: D , Mur Horizontal : MH, Mur Vertical : MV ")
            coup = input()
            print('Quel position sur le plateau désirer vous placer votre pièce?')
            print('(x,y)')
            position = input()
            etat_jeu_2 = jouer_coup(etat_jeu[0], coup, position)
            print(afficher_damier_ascii(etat_jeu_2))
    # mode automatique
    if arg.automatique and not arg.graphique:
        [identifiant, état] = initialiser_partie(idul)
        print(afficher_damier_ascii(état))
        joueur = [état['joueurs'][0]['nom'], état['joueurs'][1]['nom']]
        jeu = Quoridor(joueur)
        état = jeu.état_partie()
        while 1:
            (coup, pos) = jeu.jouer_coup(1)
            print(jeu)
            état = jouer_coup(identifiant, coup, tuple(pos))
            afficher_damier_ascii(état)
            joueur1 = état['joueurs']
            murs_j1 = état['murs']
            jeu = Quoridor(joueur1, murs_j1)
    # mode manuel avec affichage graphique
    if arg.graphique and not arg.automatique:
        [identifiant, état] = initialiser_partie(idul)
        joueur = état['joueurs']
        murs = état['murs']
        jeu = QuoridorX(joueur, murs)
        print('Quel coup désirer vous jouer ?')
        print("Deplacement pion: D , Mur Horizontal : MH, Mur Vertical : MV ")
        coup = input()
        print('Quel position sur le plateau désirer vous placer votre pièce?')
        print('(x,y)')
        position = input()
        état_2 = jouer_coup(identifiant, coup, position)
        while 1:
            joueur = état_2['joueurs']
            murs = état_2['murs']
            jeu = QuoridorX(joueur, murs)
            print('Quel coup désirer vous jouer ?')
            print("Deplacement pion: D , Mur Horizontal : MH, Mur Vertical : MV ")
            coup = input()
            print('Quel position sur le plateau désirer vous placer votre pièce?')
            print('(x,y)')
            position = input()
            état_2 = jouer_coup(identifiant, coup, position)
    # mode automatique avec affichage
    if arg.automatique and arg.graphique:
        [identifiant, état] = initialiser_partie(idul)
        joueur = [état['joueurs'][0]['nom'], état['joueurs'][1]['nom']]
        jeu = QuoridorX(joueur)
        while 1:
            (coup, pos) = jeu.jouer_coup(1)
            jeu.afficher()
            état = jouer_coup(identifiant, coup, tuple(pos))
            joueur1 = état['joueurs']
            murs_j1 = état['murs']
            jeu = QuoridorX(joueur1, murs_j1)

ARGS = analyser_commande()
quoridorgame(ARGS)
