# -*- coding: utf-8 -*-

import time
from Reversi import Board
from playerInterface import *
from display import Display

class human(PlayerInterface):
    
    def __init__(self):
        self._board = Board(10)
        self._display = Display(self._board)
        self._mycolor = None

    def getPlayerName(self):
        return "Human Player"

    def getPlayerMove(self):
        self._display.drawBoard()
        
        if self._board.is_game_over():
            return (-1,-1)
        
        rep = ()
        while (rep == ()):
            rep = self._display.inputHandler()

        self._display.performMove(self._mycolor, rep[0], rep[1])
        self._display.drawBoard()
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
