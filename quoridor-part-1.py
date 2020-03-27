# -*- coding: utf-8 -*-
"""Module d'interface utilisateur de Quoridor

Ce module permet d'interagir avec le joueur
en offrant un interface en ligne de commande.

Functions:
    * analyser_commande - Retourne la liste des parties reçues du serveur
    * afficher_damier_ascii - Affiche la représentation graphique
                                du damier en ligne de commande.
"""
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
    parser = argparse.ArgumentParser(description = 'Jeu Quoridor - phase 1')
    parser.add_argument(
        'idul', metavar = 'idul', 
        help = 'IDUL du joueur.'
    )
    
    parser.add_argument(
        '-l', '--lister', 
        action = 'store_true', 
        help = 'Lister les identifiants de vos 20 dernières parties.'
    )
    return parser.parse_args()


def afficher_damier_ascii(grille):
    #création du damier
    damier = []
    for i in range(9):
        lignes = [f'{9 - i}'] + [' '] + ['|']
        for k in range(1, 10):
            if k == 9:
                lignes += ' . '
            else:
                lignes += ' .  '
        damier.append(lignes)
        if i == 8:
            lignes = []
        else:
            lignes = [' '] + [' '] + ['|']
            for n in range(1, 10):
                if n == 9:
                    lignes += '   '
                else:
                    lignes += '    '
        damier.append(lignes)
    #murs horizontaux
    for x, y in grille["murs"]["horizontaux"]:
        for q in range(7):
            damier[19 - 2 * y][4 * x - 1 + q] = '-'
    #murs verticaux
    for x, y in grille["murs"]["verticaux"]:
        for q in range(3):
            damier[16 - 2 * y + q][4 * x - 2] = '|'
    #position des joueurs
    for z in range(2):
        a = grille["joueurs"][z]["pos"]
        damier[18 - 2 * a[1]][4 * a[0]] = f'{z + 1}'
    print(f'Légende: 1={grille["joueurs"][0]["nom"]}, 2={grille["joueurs"][1]["nom"]}\n   -----------------------------------\n' + '|\n'.join(''.join(k for k in ligne) for ligne in damier) + '--|-----------------------------------\n  | 1   2   3   4   5   6   7   8   9')
        
        
    
    
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
              | 1   2   3   4   5   6   7   8   9  
    """
