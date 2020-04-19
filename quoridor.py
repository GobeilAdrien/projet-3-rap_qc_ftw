# -*- coding: utf-8 -*-
""" Programme permettant d'utiliser l'intelligence artificielle"""
import networkx as nx


class QuoridorError(Exception):
    """Classe QuorridorError"""

class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Attributes:
        état (dict): état du jeu tenu à jour.
        TODO: Identifiez les autres attribut de votre classe

    Examples:
        >>> q.Quoridor()
    """
    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Args:
            joueurs (list): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie. Un joueur est soit une chaîne de caractères soit un dictionnaire.
                Dans le cas d'une chaîne, il s'agit du nom du joueur. Selon le rang du joueur dans
                l'itérable, sa position est soit (5,1) soit (5,9), et chaque joueur peut
                initialement placer 10 murs. Dans le cas où l'argument est un dictionnaire,
                celui-ci doit contenir une clé 'nom' identifiant le joueur, une clé 'murs'
                spécifiant le nombre de murs qu'il peut encore placer, et une clé 'pos' qui
                spécifie sa position (x, y) actuelle.
            murs (dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions (x, y) des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions (x, y) des murs verticaux. Par défaut, il
                n'y a aucun mur placé sur le jeu.

        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """
        self.joueurs = joueurs
        if murs is None:
            self.murs = {}
        else:
            self.murs = murs
        try:
            self.joueurs_iter = iter(self.joueurs)
        except QuoridorError:
            print("L'argument joueur n'est pas itérable.")
        if len(self.joueurs) != 2:
            raise QuoridorError("L'itérable de joueurs ne contient pas deux joueurs.")
        if not isinstance(self.murs, dict):
            raise QuoridorError("L'argument murs n'est pas un dictionnaire.")
        if isinstance(self.joueurs[0], dict) and self.murs != {}:
            if 0 < self.joueurs[0]['murs'] > 10 or\
                0 < self.joueurs[1]['murs'] > 10:
                raise QuoridorError("Nombre de murs invalide.")
            if (self.joueurs[0]['murs'] + self.joueurs[1]['murs']\
                + len(self.murs['horizontaux']) + \
                    len(self.murs['verticaux'])) != 20:
                raise QuoridorError("Le dictionnaire contient trop de murs.")
            self.position1 = joueurs[0]['pos']
            self.position2 = joueurs[1]['pos']
            for i in self.position1:
                if not 1 <= i <= 9:
                    raise QuoridorError("Position invalide.")
            for j in self.position2:
                if not 1 <= j <= 9:
                    raise QuoridorError("Position invalide.")
            self.murs_h = murs["horizontaux"]
            self.murs_v = murs["verticaux"]
            for m in self.murs_h:
                if not 1 <= m[0] <= 8:
                    raise QuoridorError("Emplacement de mur invalide.")
                if not 2 <= m[1] <= 9:
                    raise QuoridorError("Emplacement de mur invalide.")
            for k in self.murs_v:
                if not 2 <= k[0] <= 9:
                    raise QuoridorError("Emplacement de mur invalide.")
                if not 1 <= k[1] <= 8:
                    raise QuoridorError("Emplacement de mur invalide.")
        if not isinstance(self.joueurs[0], dict):
            self.joueur1 = joueurs[0]
            self.joueur2 = joueurs[1]
            self.murs_j1 = 10
            self.murs_j2 = 10
            self.position1 = (5, 1)
            self.position2 = (5, 9)
            self.murs_h = []
            self.murs_v = []
            self.gamestate = {'joueurs': [{'nom': self.joueur1, 'murs':self.murs_j1, \
                'pos':self.position1}, {'nom':self.joueur2, \
                    'murs':self.murs_j2, 'pos':self.position2}], \
                        'murs':{'horizontaux': self.murs_h, 'verticaux': self.murs_v}}
        else:
            self.joueur1 = joueurs[0]['nom']
            self.joueur2 = joueurs[1]['nom']
            self.murs_j1 = joueurs[0]['murs']
            self.murs_j2 = joueurs[1]['murs']
            self.murs_h = murs["horizontaux"]
            self.murs_v = murs["verticaux"]
            self.gamestate = {"joueurs": [{'nom': self.joueur1, 'murs': self.murs_j1, \
                'pos': self.position1}, {"nom": self.joueur2, \
                    "murs": self.murs_j2, "pos": self.position2}], \
                        "murs": {"horizontaux": self.murs_h, "verticaux": self.murs_v}}

    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation.
        """
        nom1 = f'1={self.gamestate["joueurs"][0]["nom"]}, '
        nom2 = f'2={self.gamestate["joueurs"][1]["nom"]}'
        haut = f'Légende:' + nom1 + nom2 + '\n'
        haut += '   -----------------------------------\n'
        bas = '--|-----------------------------------\n'
        bas += '  | 1   2   3   4   5   6   7   8   9\n'
        liste_vide = []
        for i in range(18, 1, -1):
            style_damier_1 = list(f"{i//2} | .   .   .   .   .   .   .   .   . |")
            style_damier_2 = list("  |                                   |")
            if i%2 == 0:
                liste_vide.append(style_damier_1)
            else:
                liste_vide.append(style_damier_2)
        for i in range(2):
            x = 18-2*self.gamestate["joueurs"][i]["pos"][1]
            y = 4*self.gamestate["joueurs"][i]["pos"][0]
            liste_vide[x][y] = f'{i+1}'
        for i in range(len(self.gamestate["murs"]["horizontaux"])):
            for j in range(7):
                x = 19-2*self.gamestate["murs"]["horizontaux"][i][1]
                y = 4*self.gamestate["murs"]["horizontaux"][i][0]+j-1
                liste_vide[x][y] = '-'
        for i in range(len(self.gamestate["murs"]["verticaux"])):
            for j in range(3):
                x = 18-2*self.gamestate["murs"]["verticaux"][i][1]-j
                y = 4*self.gamestate["murs"]["verticaux"][i][0]-2
                liste_vide[x][y] = '|'
        damier = []
        for ligne in liste_vide:
            damier += ligne + ['\n']
        milieu = ''.join(damier)

        return haut + milieu + bas

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (tuple): Le tuple (x, y) de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        pos = position
        état = self.gamestate
        coup_droit, coup_gauche, coup_avant, coup_arrière = False, False, False, False
        if joueur == 1:
            joueur_dep = self.position1
        else:
            joueur_dep = self.position2
        graphe_joueurs = construire_graphe([joueur['pos'] for joueur in état['joueurs']], \
            état['murs']['horizontaux'], état['murs']['verticaux'])
        if joueur not in (1, 2):
            raise QuoridorError("Le numéro du joueur spécifié n'existe pas.")
        if not 1 <= pos[0] <= 9 or not 1 <= pos[1] <= 9:
            raise QuoridorError("Position invalide (en dehors du damier).")
        if position[0] == pos[0] + 1:
            coup_droit = True
        if position[0] == pos[0] - 1:
            coup_gauche = True
        if position[1] == pos[1] + 1:
            coup_avant = True
        if position[1] == pos[1] - 1:
            coup_arrière = True
        for k in self.gamestate['murs']['horizontaux']:
            if coup_avant and ((k[0] == joueur_dep[0] and k[1] + 1 == joueur_dep[1]) or\
                (k[0]-1 == joueur_dep[0] and k[1] + 1 == joueur_dep[1])):
                raise QuoridorError("Un mur empêche votre coup.")
            if coup_arrière and ((k[0] == joueur_dep[0] and k[1] == joueur_dep[1]) or\
                (k[0]-1 == joueur_dep[0] and k[1] == joueur_dep[1])):
                raise QuoridorError("Un mur empêche votre coup.")
        for m in self.gamestate['murs']['verticaux']:
            if coup_droit and ((m[0] + 1 == joueur_dep[0] and m[1] - 1 == joueur_dep[1]) or\
                (m[0] + 1 == joueur_dep[0] and m[1] == joueur_dep[1])):
                raise QuoridorError("Un mur empêche votre coup.")
            if coup_gauche and ((m[0] == joueur_dep[0] and m[1] - 1 == joueur_dep[1]) or\
                (m[0] == joueur_dep[0] and m[1] == joueur_dep[1])):
                raise QuoridorError("Un mur empêche votre coup.")
        if joueur == 1:
            coup_permis = list(graphe_joueurs.successors(self.position1))
            flag1 = 0
            for n in coup_permis:
                if pos == n:
                    flag1 += 1
            if flag1 != 1:
                raise QuoridorError("Coup invalide.")
            self.position1 = pos
            self.gamestate['joueurs'][0]['pos'] = pos
        if joueur == 2:
            coup_permis = list(graphe_joueurs.successors(self.position2))
            flag2 = 0
            for j in coup_permis:
                if pos == j:
                    flag2 += 1
            if flag2 != 1:
                raise QuoridorError("Coup invalide.")
            self.position2 = pos
            self.gamestate['joueurs'][1]['pos'] = pos

    def état_partie(self):
        """Produire l'état actuel de la partie.

        Returns:
            dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.

        Examples:

            {
                'joueurs': [
                    {'nom': nom1, 'murs': n1, 'pos': (x1, y1)},
                    {'nom': nom2, 'murs': n2, 'pos': (x2, y2)},
                ],
                'murs': {
                    'horizontaux': [...],
                    'verticaux': [...],
                }
            }

            où la clé 'nom' d'un joueur est associée à son nom, la clé 'murs' est associée
            au nombre de murs qu'il peut encore placer sur ce damier, et la clé 'pos' est
            associée à sa position sur le damier. Une position est représentée par un tuple
            de deux coordonnées x et y, où 1<=x<=9 et 1<=y<=9.

            Les murs actuellement placés sur le damier sont énumérés dans deux listes de
            positions (x, y). Les murs ont toujours une longueur de 2 cases et leur position
            est relative à leur coin inférieur gauche. Par convention, un mur horizontal se
            situe entre les lignes y-1 et y, et bloque les colonnes x et x+1. De même, un
            mur vertical se situe entre les colonnes x-1 et x, et bloque les lignes y et y+1.
        """
        return self.gamestate

    def jouer_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.

        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.
        """
        if joueur not in (1, 2):
            raise QuoridorError("Le numéro du joueur spécifié n'existe pas.")
        if self.partie_terminée() is not False:
            raise QuoridorError("La partie est déjà terminée.")
        état = self.gamestate
        graphe_joueurs = construire_graphe([joueur['pos'] for joueur in état['joueurs']], \
            état['murs']['horizontaux'], état['murs']['verticaux'])
        shortest_pathj1 = nx.shortest_path(graphe_joueurs, self.position1, 'B1')
        shortest_pathj2 = nx.shortest_path(graphe_joueurs, self.position2, 'B2')
        if joueur == 1:
            nouvelle_position = (shortest_pathj1[1])
            self.déplacer_jeton(joueur, nouvelle_position)
        if joueur == 2:
            nouvelle_position = (shortest_pathj2[1])
            self.déplacer_jeton(joueur, nouvelle_position)
        return ('D', nouvelle_position)

    def partie_terminée(self):
        """Déterminer si la partie est terminée.
            Returns:
                str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        for i in range(9):
            if self.position1 == [i+1, 9]:
                return self.joueur1
            if self.position2 == [i+1, 1]:
                return self.joueur2
        return False

    def placer_mur(self, joueur: int, position: tuple, orientation: str):
        """Placer un mur.
        Pour le joueur spécifié, placer un mur à la position spécifiée.
        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (tuple): le tuple (x, y) de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        if joueur not in [1, 2]:
            raise QuoridorError('le numéro du joueur doit être 1 ou 2')

        if joueur == 1:
            if self.gamestate['joueurs'][0]['murs'] == 0:
                raise QuoridorError('le joueur a déjà placé tous ses murs')

        if joueur == 2:
            if self.gamestate['joueurs'][1]['murs'] == 0:
                raise QuoridorError('le joueur a déjà placé tous ses murs')

        self._vérifier_placer_mur_vertical(position, orientation)
        self._vérifier_placer_mur_horizontal(position, orientation)

        self.gamestate['joueurs'][joueur-1]['murs'] -= 1

    def _vérifier_placer_mur_vertical(self, position: tuple, orientation: str):
        murs_verticaux = self.gamestate['murs']['verticaux']

        for i in murs_verticaux:
            self.position_interdite_verticale.append((i[0], i[1] - 1))
            self.position_interdite_verticale.append((i[0], i[1]))
            self.position_interdite_verticale.append((i[0], i[1] + 1))

        if orientation == 'vertical':
            if position in self.position_interdite_verticale:
                raise QuoridorError('un mur occupe déjà cette position')
            self.gamestate['murs']['verticaux'].append(position)

        for i in self.gamestate['murs']['verticaux']:
            if i[0] < 2 or i[1] > 8:
                self.gamestate['murs']['verticaux'].pop()
                raise QuoridorError("Position mur vertical invalide")
            if i not in list(product(range(1, 10), repeat=2)):
                self.gamestate['murs']['verticaux'].pop()
                raise QuoridorError("Position mur vertical invalide")

    def _vérifier_placer_mur_horizontal(self, position: tuple, orientation: str):
        murs_horizontaux = self.gamestate['murs']['horizontaux']

        for i in murs_horizontaux:
            self.position_interdite_horizontale.append((i[0] - 1, i[1]))
            self.position_interdite_horizontale.append((i[0], i[1]))
            self.position_interdite_horizontale.append((i[0] + 1, i[1]))

        if orientation == 'horizontal':
            if position in self.position_interdite_horizontale:
                raise QuoridorError('un mur occupe déjà cette position')
            self.gamestate['murs']['horizontaux'].append(position)

        for i in self.gamestate['murs']['horizontaux']:
            if i[0] > 8 or i[1] < 2:
                self.gamestate['murs']['horizontaux'].pop()
                raise QuoridorError("Position mur horizontal invalide")
            if i not in list(product(range(1, 10), repeat=2)):
                self.gamestate['murs']['horizontaux'].pop()
                raise QuoridorError("Position mur horizontal invalide")


# FONCTION FOURNIE
def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """Construire un graphe de la grille.

    Crée le graphe des déplacements admissibles pour les joueurs.
    Vous n'avez pas à modifer cette fonction.

    Args:
        joueurs (list): une liste des positions (x,y) des joueurs.
        murs_horizontaux (list): une liste des positions (x,y) des murs horizontaux.
        murs_verticaux (list): une liste des positions (x,y) des murs verticaux.

    Returns:
        DiGraph: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # s'assurer que les positions des joueurs sont bien des tuples (et non des listes)
    j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])

    # traiter le cas des joueurs adjacents
    if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):

        # retirer les liens entre les joueurs
        graphe.remove_edge(j1, j2)
        graphe.remove_edge(j2, j1)

        def ajouter_lien_sauteur(noeud, voisin):
            """
            :param noeud: noeud de départ du lien.
            :param voisin: voisin par dessus lequel il faut sauter.
            """
            saut = 2*voisin[0]-noeud[0], 2*voisin[1]-noeud[1]

            if saut in graphe.successors(voisin):
                # ajouter le saut en ligne droite
                graphe.add_edge(noeud, saut)

            else:
                # ajouter les sauts en diagonale
                for saut in graphe.successors(voisin):
                    graphe.add_edge(noeud, saut)

        ajouter_lien_sauteur(j1, j2)
        ajouter_lien_sauteur(j2, j1)

    # ajouter les destinations finales des joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe
