# -*- coding: utf-8 -*-

import time
from Reversi import Board
from random import randint,choice
from implementedPlayer import *
from players.algorithms.simple import *

from threading import Thread
from queue import Queue # Thread self data structure

import copy

class OneDirection(Thread):
    """ Simple thread for on specific move """

    def __init__(self, board, initialMove, queue, color):
        Thread.__init__(self)
        self.board = board
        self.initialMove = initialMove
        self.queue = queue
        self.color = color

    def run(self):

        # Do we need this ?
        if self.board.is_game_over():
            return (-1,-1)
        
        self.board.push(self.initialMove)
        value = minValue(self.board,heuristic1,-1000,1000,self.color,0,4)
        self.board.pop()

        self.queue.put((self.initialMove, value))



class miniMax_thread(ImplementedPlayer):

    def getPlayerName(self):
        return "MiniMax"

    def nextMove(self):

        b = self._board
        if b.is_game_over():
            return (-1,-1)
        
        moves = {}
        best = -1000

        resultQueue = Queue()

        possibleMoves = b.legal_moves()
        numberPossibleMoves = len(possibleMoves)
        threadList = list()

        for i in range(numberPossibleMoves):
            threadList.append(OneDirection(copy.deepcopy(self._board), possibleMoves[i], resultQueue, self._mycolor))
            threadList[i].start()

        # Ne pas attendre les autres si on a un résultat satisfesant ?
        for i in range(numberPossibleMoves):
            threadList[i].join()

        for i in range(numberPossibleMoves):
            (move, value) = resultQueue.get()

            if value > best:
                best = value
            
            if str(value) in moves:
                moves[str(value)].append(move)
            else:
                moves[str(value)] = [move]
                
        m = choice(moves[str(best)])
        b.push(m)
        (c,x,y) = m

        return (x,y)

    def endGame(self, winner):
        pass
