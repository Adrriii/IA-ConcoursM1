# -*- coding: utf-8 -*-

import time
from Reversi import Board
from random import randint,choice
from implementedPlayer import *
from players.algorithms.medium import *

class NegaBetaCredit(ImplementedPlayer):

    def __init__(self):
        super().__init__()
        self.credit_run_out_time = 30000
        self.game_start_time = now()
        self.game_time_max = 300000
        self.heuristic = heuristic2

    def getPlayerName(self):
        return "Adri"        
        

    def nextMove(self):
        b = self._board
        if b.is_game_over():
            return (-1,-1)
        
        moves = {}
        best = -1000

        current_val = self.heuristic(b,self._mycolor)
        thinking_start = now()
        i = 0
        mvs = b.legal_moves()

        if(len(mvs)<=0):
            return (-1,-1)

        for m in mvs:
            i += 1
            
            b.push(m) 
            val = self.heuristic(b,self._mycolor)
            remaining_time_percent = (now() - self.game_start_time) / self.game_time_max
            remaining_time_credits = self.credit_run_out_time * abs(1-remaining_time_percent)
            
            value = -NegaAlphaBetaCredit(b,self.heuristic,-1000,1000,self._mycolor,70,current_val,val, 1,remaining_time_credits, thinking_start)
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
