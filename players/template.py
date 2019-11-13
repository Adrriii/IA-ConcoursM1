# -*- coding: utf-8 -*-

import time
from Reversi import Board
from random import randint
from playerInterface import *

# used to easily create a new player
class template(PlayerInterface):

    def __init__(self):
        self._board = Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "Name"

    def getPlayerMove(self):
        if self._board.is_game_over():
            return (-1,-1)
        
        move = None

        for m in self._board.legal_moves():
            # moves
            move = m

        self._board.push(m)
        (c,x,y) = move
        return (x,y) 

    def playOpponentMove(self, x,y):
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        pass
