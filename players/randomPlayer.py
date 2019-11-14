# -*- coding: utf-8 -*-

import time
from Reversi import Board
from random import randint
from graphicalPlayer import *

class randomPlayer(GraphicalPlayer):

    def getPlayerName(self):
        return "Random Player"

    def nextMove(self):
        if self._board.is_game_over():
            return (-1,-1)
        moves = [m for m in self._board.legal_moves()]
        move = moves[randint(0,len(moves)-1)]
        self._board.push(move)
        (c,x,y) = move
        assert(c==self._mycolor)
        return (x,y)

    def endGame(self, winner):
        pass
