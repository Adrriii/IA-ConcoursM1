# -*- coding: utf-8 -*-

from Reversi import Board
from implementedPlayer import *

from threading import Thread
from queue import Queue
from random import randint, choice

import copy

def heuristic_takeAllPiece(board, player):
    """ Simple heuristic that just want to take all pieces """
    if player is board._WHITE:
        return board._nbWHITE - board._nbBLACK
    
    return board._nbBLACK - board._nbWHITE


def heuristic_takeCorner(board, player):
    boardArray = board.get_board()
    boardSize = board.get_board_size()

    score = heuristic_takeAllPiece(board, player)
    cst = score

    for corner in board.get_corner():
        score += cst if corner is player else -cst

    for i in [0, boardSize]:
        for j in range(boardSize):
            if boardArray[i][j] is player:
                score += cst//2

            if boardArray[j][i] is player:
                score += cst//2

    return score


def heuristic_takeVictory(board, player):
    (nbWhite, nbBlack) = board.get_nb_pieces()

    if player is board._BLACK:
        return 1 if nbBlack > nbWhite else -1

    return 1 if nbBlack < nbWhite else -1



class MetaPlayer(ImplementedPlayer):

    def __init__(self):
        super().__init__()

        self._BEGIN     = 0
        self._MIDDLE    = 1
        self._END       = 2

        self.heuristic_dict = {
            self._BEGIN:    heuristic_takeAllPiece,
            self._MIDDLE:   heuristic_takeCorner,
            self._END:      heuristic_takeVictory
        }

        self.state = self._BEGIN


    def chooseHeuristic(self):
        nbPieces = self._board.get_total_pieces()
        
        if self.state is self._BEGIN:
            if nbPieces > 10: # Find better value
                self.state = self._MIDDLE
            

    def getPlayerName(self):
        return "Rob's big brain algo"

    def nextMove(self):
        pass

    def endGame(self, color):
        """ Nothing to do """
        pass