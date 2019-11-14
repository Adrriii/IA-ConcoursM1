# -*- coding: utf-8 -*-

import time
from Reversi import Board
from graphicalPlayer import *
from display import Display

class human(GraphicalPlayer):

    def getPlayerName(self):
        return "Human Player"

    def nextMove(self):        
        if self._board.is_game_over():
            return (-1,-1)
        
        rep = ()
        while (rep == ()):
            rep = self._display.inputHandler()

        return rep

    def playOpponentMove(self, x,y):
        self._board.push([self._opponent, x, y])
        self._display.performMove(self._opponent, x, y)
        self._display.drawBoard()

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        pass
