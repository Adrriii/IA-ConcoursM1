# -*- coding: utf-8 -*-

import time
from Reversi import Board
from random import randint,choice
from graphicalPlayer import *
from players.algorithms.simple import *

class miniMax(GraphicalPlayer):

    def getPlayerName(self):
        return "MiniMax"

    def nextMove(self):
        b = self._board
        if b.is_game_over():
            return (-1,-1)
        
        moves = {}
        best = -1000

        for m in b.legal_moves():
            b.push(m)
            value = minValue(b,heuristic1,-1000,1000,self._mycolor,0,3)
            b.pop()

            if value > best:
                best = value

            if str(value) in moves:
                moves[str(value)].append(m)
            else:
                moves[str(value)] = [m]

        m = choice(moves[str(best)])
        b.push(m)
        (c,x,y) = m

        return (x,y)

    def endGame(self, winner):
        pass
