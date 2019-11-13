# -*- coding: utf-8 -*-

import time
from Reversi import Board
from random import randint
from playerInterface import *

class human(PlayerInterface):

    def __init__(self):
        self._board = Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "Human Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            return (-1,-1)
        moves = {}
        for m in self._board.legal_moves():
            key = str(m[1])+","+str(m[2])
            moves[key] = m
            print(key)
        print(self._board)
        correct = False
        while not correct:
            try:
                m = moves[input("Next move 'x,y' : ")]
                correct = True
            except:
                pass

        self._board.push(m)
        return (m[1],m[2]) 

    def playOpponentMove(self, x,y):
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        pass
