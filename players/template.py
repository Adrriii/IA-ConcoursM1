# -*- coding: utf-8 -*-

import time
from Reversi import Board
from implementedPlayer import *

# used to easily create a new player
class template(ImplementedPlayer):

    def getPlayerName(self):
        return "Name"

    def nextMove(self):
        if self._board.is_game_over():
            return (-1,-1)
        
        move = None

        for m in self._board.legal_moves():
            # moves
            move = m

        self._board.push(m)
        (c,x,y) = move
        return (x,y)

    def endGame(self, winner):
        pass
