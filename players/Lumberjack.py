# -*- coding: utf-8 -*-

from Reversi import Board
from implementedPlayer import *
from players.algorithms.medium import *

from threading import Thread
from queue import Queue
from random import randint, choice

import copy
import time
import collections


def getTimeMillis():
    return int(round(time.time() * 1000))


def getEllapsedTime(initialTime):
    return getTimeMillis() - initialTime


# Maximum time for each move. Updated dynamically
MAX_TIME_MILLIS = 5000

INITIAL_CREDIT = 30

GOOD_MOVE_VALUE = 5
MEDIUM_MOVE_VALUE = 10
BAD_MOVE_VALUE = 20


MAX_VALUE = 999999999
MIN_VALUE = -MAX_VALUE

GAME_END = 30

def insertSort(l, datas, value):
    insertIndex = len(l)

    for i in range(insertIndex):
        if l[i][0] < value:
            insertIndex = i
            break

    l.insert(insertIndex, (value, datas))


def alphaBetaLauncher(board, startTime, alpha, beta, heuristic, player):
    ''' Start the alpha beta prunning'''
    currentCredit = INITIAL_CREDIT

    moves = board.legal_moves()

    if len(moves) == 1:
        return (0, moves[0])

    best_move = (MIN_VALUE - 1, moves[0])
    queue = list()


    # Initial search, initialize queue
    for i in moves:
        board.push(i)
        currentValue = MinValue(board, alpha, beta, heuristic, player, startTime, currentCredit, queue, i, 1)
        board.pop()

        if currentValue == MAX_VALUE:
            return (currentValue, i)

        if currentValue >= best_move[0]:
            best_move = (currentValue, i)

        if getEllapsedTime(startTime) > MAX_TIME_MILLIS:
            return best_move


    boardSave = board.encode()

    while (getEllapsedTime(startTime) < MAX_TIME_MILLIS and len(queue) > 0):

        (value, (boardData, initialMove, depth)) = queue.pop(0)
        board.decode(boardData)

        if board._nextPlayer == player:
            currentValue = MinValue(board, alpha, beta, heuristic, player, startTime, currentCredit, queue, initialMove, depth)
        else:    
            currentValue = MaxValue(board, alpha, beta, heuristic, player, startTime, currentCredit, queue, initialMove, depth)


        if currentValue >= best_move[0]:
            best_move = (currentValue, initialMove)
    
    # Reset board
    board.decode(boardSave)

    return best_move



def MaxValue(board, alpha, beta, heuristic, player, startTime, numberCredit, queue, initialMove, depth):

    if numberCredit < 0 or getEllapsedTime(startTime) > MAX_TIME_MILLIS:
        # End, put the board state in the queue
        value = heuristic(board, player)
        insertSort(queue, (board.encode(), initialMove, depth), value)

        return value


    if board.is_game_over():
        (nbWhite, nbBlack) = board.get_nb_pieces()
        if player is board._BLACK:
            return MAX_VALUE if nbBlack > nbWhite else MIN_VALUE

        if player is board._WHITE:
            return MAX_VALUE if nbBlack < nbWhite else MIN_VALUE


    dominationDiff = board.getCurrentDomination(player) - board.getInitialDomination(player)
    
    if dominationDiff < -0.1:
        numberCredit -= BAD_MOVE_VALUE
    elif dominationDiff < 0.2:
        numberCredit -= MEDIUM_MOVE_VALUE
    else:
        numberCredit -= GOOD_MOVE_VALUE

    for move in board.legal_moves():

        board.push(move)
        alpha = max(alpha, MinValue(board, alpha, beta, heuristic, player, startTime, numberCredit, queue, initialMove, depth + 1))
        board.pop()

        if alpha >= beta:
            return beta
    
    return alpha



def MinValue(board, alpha, beta, heuristic, player, startTime, numberCredit, queue, initialMove, depth):
    if numberCredit < 0 or getEllapsedTime(startTime) > MAX_TIME_MILLIS:
        value = heuristic(board, player)
        insertSort(queue, (board.encode(), initialMove, depth), value)

        return value

    if board.is_game_over():
        (nbWhite, nbBlack) = board.get_nb_pieces()
        if player is board._BLACK:
            return MAX_VALUE if nbBlack > nbWhite else MIN_VALUE if nbWhite > nbBlack else 0

        if player is board._WHITE:
            return MAX_VALUE if nbBlack < nbWhite else MIN_VALUE if nbBlack > nbWhite else 0


    dominationDiff = board.getCurrentDomination(player) - board.getInitialDomination(player)

    if dominationDiff < -0.1:
        numberCredit -= BAD_MOVE_VALUE
    elif dominationDiff < 0.2:
        numberCredit -= MEDIUM_MOVE_VALUE
    else:
        numberCredit -= GOOD_MOVE_VALUE

    
    for move in board.legal_moves():

        board.push(move)
        beta = min(beta, MaxValue(board, alpha, beta, heuristic, player, startTime, numberCredit, queue, initialMove, depth + 1))
        board.pop()

        if alpha >= beta:
            return alpha
    
    return beta


class Lumberjack(ImplementedPlayer):

    def __init__(self):
        super().__init__()

        self._BEGIN     = 0
        self._MIDDLE    = 1
        self._END       = 3

        self.state = self._BEGIN

        self.timeCount = 0
        self.timeMax = 300 * 1000 - 200 # Marge


    def newGame(self, color, board_size = 10):
        super().newGame(color, board_size)
        self.bookStack = self._board._stack.copy()


    def updateGameState(self):
        """ Function that estimate when we are in the game """
        boardArray = self._board.get_board()

        if self.state is self._MIDDLE:
            if self._board.get_board_size()**2 - self._board.get_total_pieces() <= GAME_END:
                self.state = self._END
                return

    
    def getPlayerName(self):
        return "Lumberjack"


    def nextMove(self):
        global MAX_TIME_MILLIS
        startTime = getTimeMillis()

        possibleMoves = self._board.legal_moves()
        numberPossibleMoves = len(possibleMoves)

        if numberPossibleMoves <= 0:
            self._board.push([self._mycolor, -1, -1])
            self.timeCount += getEllapsedTime(startTime)

            return (-1, -1)


        # Search in the book
        if (self.state == self._BEGIN):
            move = getBookMove(self.bookStack.copy())

            if move != -1:
                self.bookStack.append(move)
                (x, y) = move
                self._board.push([self._mycolor, x, y])

                return (x,y)
            else:
                # Can't use the book, switch to middle state
                self.state = self._MIDDLE
        else:
            self.updateGameState()
        

        self._board.setInitialDomination()

        MAX_TIME_MILLIS = (self.timeMax - self.timeCount)//((self._board.get_board_size()**2 - (self._board.get_total_pieces() - 1))//2)

        #Saving time for end
        if self.state is self._MIDDLE:
            MAX_TIME_MILLIS -= MAX_TIME_MILLIS//3

        elif self.state is self._END:
            MAX_TIME_MILLIS += (self.timeMax - self.timeCount - MAX_TIME_MILLIS)//5

        value = alphaBetaLauncher(self._board, startTime, MIN_VALUE, MAX_VALUE, heuristic_angle, self._mycolor)


        self._board.push(value[1])
        (_,x,y) = value[1]

        self.timeCount += getEllapsedTime(startTime)

        return (x,y)
        

    def endGame(self, color):
        """ Nothing to do """
        pass


    def playOpponentMove(self, x,y):
        super().playOpponentMove(x, y)

        self.bookStack.append((x, y))