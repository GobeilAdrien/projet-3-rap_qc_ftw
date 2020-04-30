# -*- coding: utf-8 -*-
""" Programme permettant d'utiliser l'intelligence artificielle amélioré"""
import turtle
from quoridor import Quoridor


class QuoridorX(Quoridor):
    """ Classe quoridor graphique """
    def __init__(self, joueurs, murs=None):
        """Fonction contructeur"""
        super().__init__(joueurs, murs)
        self.fen = turtle.Screen()
        self.fen.title("Jeu Quoridor contre un serveur automatisé")
        self.fen.setup(width=600, height=600)
        self.curs = turtle.Turtle()
        self.fen.clearscreen()
        self.fen.tracer(0, 0)
        self.curs.hideturtle()
        self.curs_j1 = turtle.Turtle()
        self.curs_j2 = turtle.Turtle()
        self.curs_j1.hideturtle()
        self.curs_j2.hideturtle()
        self.curs_j1.penup()
        self.curs_j2.penup()
        self.curs.speed(0)
        self.fen.register_shape('bender.gif')
        self.fen.register_shape('rap.gif')
        self.fen.register_shape('rectangle', ((0, 0), (0, 50), (50, 50), (50, 0)))
        self.fen.register_shape('mur_h', ((0, 0), (0, 115), (8, 115), (8, 0)))
        self.fen.register_shape('mur_v', ((0, 0), (-115, 0), (-115, 8), (0, 8)))
        self.flag_mur_h = len(murs_h)
        self.flag_mur_v = len(murs_v)
        self.init_mur = 0
        if self.murs_h != [] or self.murs_v != []:
            self.init_mur = 1
        for i in range(9):
            y_cord = 285 - (i*(65))
            for j in range(9):
                self.curs.penup()
                x_cord = -285 + (j*(65))
                self.curs.goto(x_cord, y_cord)
                self.curs.fillcolor("#e5b5ff")
                self.curs.shape("rectangle")
                self.curs.stamp()
        self.afficher()
    
    def afficher(self):
            "Affiche l'état du jeu"
            self.fen.delay(100)
            self.curs.speed(2)
            self.placer_jeton(1)
            self.placer_jeton(2)
            if self.init_mur == 1:
                self.mur_horizontal()
                self.mur_vertical()
                self.init_mur = 0
            if len(self.murs_h) != self.flag_mur_h:
                self.mur_horizontal()
            if len(self.murs_v) != self.flag_mur_v:
                self.mur_vertical()
            self.flag_mur_h = len(self.murs_h)
            self.flag_mur_v = len(self.murs_v)
            self.fen.update()
            
    def placer_jeton(self, joueur):
        'Place les jetons'
        if joueur == 1:
            position = self.position1
            y_pos = -260 + 65 * (position[1]-1)
            x_pos = -260 + 65 * (position[0]-1)
            if self.curs_j1.position() != (x_pos, y_pos):
                self.curs_j1.hideturtle()
                self.curs_j1.shape('rap.gif')
                self.curs_j1.goto(x_pos, y_pos)
                self.curs_j1.showturtle()
        if joueur == 2:
            position = self.position2
            y_pos = -260 + 65 * (position[1]-1)
            x_pos = -260 + 65 * (position[0]-1)
            if self.curs_j2.position() != (x_pos, y_pos):
                self.curs_j2.hideturtle()
                self.curs_j2.shape('bender.gif')
                self.curs_j2.goto(x_pos, y_pos)
                self.curs_j2.showturtle()
