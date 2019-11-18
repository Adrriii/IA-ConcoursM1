# -*- coding: utf-8 -*-

import time
from Reversi import Board
from implementedPlayer import *
from display import Display

class human(ImplementedPlayer):

    def getPlayerName(self):
        return "Human Player"

    def nextMove(self):        
        moves = self._board.legal_moves()
        self._display.drawBoard("test", self._mycolor)
        print(moves)
        
        rep = ()

        if self._board.is_game_over() or (len(moves) == 1 and moves[0][1] == -1 and moves[0][2] == -1):
            rep = (-1,-1)
            
        while (rep == ()):
            rep = self._display.inputHandler()
        

        self._display.performMove(self._mycolor, rep[0],rep[1])
        self._board.push([self._mycolor, rep[0],rep[1]])

        return rep

    def playOpponentMove(self, x,y):
        self._display.performMove(self._opponent, x, y)
        self._board.push([self._opponent, x, y])
        

    def newGame(self, color, board_size = 10):
        super().newGame(color,board_size)

        self._display = Display()
        self._display.newGame(board_size)
        self._mycolor = color   
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        pass
