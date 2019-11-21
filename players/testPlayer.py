# -*- coding: utf-8 -*-

import time
from Reversi import Board
from implementedPlayer import *

from threading import Thread
from queue import Queue
from random import randint,choice

from players.algorithms.medium import *

import copy

class OneDirection(Thread):
    """ Simple thread for on specific move """

    def __init__(self, board, initialMove, queue, color, algo, heuristic, depth, alpha=-1000, beta=1000):
        Thread.__init__(self)

        self.heuristic = heuristic
        self.algo = algo
        self.depth = depth

        self.board = board
        self.initialMove = initialMove
        self.queue = queue
        self.color = color

        self.alpha = alpha
        self.beta = beta

    def run(self):
        # Assume that game is not over when this function is called.
        self.board.push(self.initialMove)
        value = self.algo(self.board, self.alpha, self.beta, self.depth, self.heuristic, self.color)
        self.board.pop()

        self.queue.put((self.initialMove, value))


class TestPlayer(ImplementedPlayer):

    def getPlayerName(self):
        return "Rob's test player"

    
    def nextMove(self):
        b = self._board
        if b.is_game_over():
            return (-1,-1)
        
        moves = {}
        best = -9999

        resultQueue = Queue()

        possibleMoves = b.legal_moves()
        numberPossibleMoves = len(possibleMoves)

        if (numberPossibleMoves <= 0):
            return (-1, -1)
        
        threadList = list()

        for i in range(numberPossibleMoves):
            threadList.append(
                OneDirection(
                    copy.deepcopy(self._board),
                    possibleMoves[i],
                    resultQueue,
                    self._mycolor,
                    negAlphaBetaDepth,
                    heuristic_angle,
                    4
                )
            )
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
                
        if(str(best) not in moves.keys()):
            print(moves)
            b.push([self._mycolor,-1,-1])
            return (-1,-1)

        m = choice(moves[str(best)])
        b.push(m)
        (c,x,y) = m

        return (x,y)
        

    def endGame(self, color):
        pass