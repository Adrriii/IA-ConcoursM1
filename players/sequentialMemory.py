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

# Number of empty slots on the board to switching in EndGame mode
ENDGAME = 9



############################################
#       Time Managment
############################################

def getTimeMillis():
    return int(round(time.time() * 1000))


def getEllapsedTime(initialTime):
    return getTimeMillis() - initialTime

 

############################################
#       Heuristics
############################################

def heuristic_takeAllPiece(board, player):
    """ Simple heuristic that just want to take all pieces """

    if player is board._WHITE:
        return board._nbWHITE - board._nbBLACK
    
    return board._nbBLACK - board._nbWHITE


def heuristic_takeDomination(board, player):
    """ Heuristic that try to take corner, with an advantage if it takes border """

    boardArray = board.get_board()
    boardSize = board.get_board_size()

    otherPlayer = board._WHITE if player is board._BLACK else board._BLACK

    score = (board.getCurrentDomination(player) - board.getInitialDomination(player)) * 100
    cst = 30

    for corner in board.get_corner():
        if corner is player:
            score += score
        else:
            score -= score



    return score


def heuristic_takeVictory(board, player):
    """ Heuristic for victory """
    (nbWhite, nbBlack) = board.get_nb_pieces()

    if (board.is_game_over()):
        if player is board._BLACK:
            if nbBlack > nbWhite:
                return MAX_VALUE
            return MIN_VALUE
        
        if player is board._WHITE:
            if nbWhite > nbWhite:
                return MAX_VALUE
            return MIN_VALUE

    return board.getCurrentDomination(player)



# Maximum time for each move. Has to be updated dynamically
MAX_TIME_MILLIS = 5000


INITIAL_CREDIT = 30

GOOD_MOVE_VALUE = 5
MEDIUM_MOVE_VALUE = 10
BAD_MOVE_VALUE = 20




# Must be higher than any heuristic resutl
MAX_VALUE = 999999999
MIN_VALUE = -MAX_VALUE

def insertSort(l, datas, value):
    insertIndex = len(l)

    for i in range(insertIndex):
        if l[i][0] < value:
            insertIndex = i
            break

    l.insert(insertIndex, (value, datas))

def alphaBetaLauncher(board, startTime, alpha, beta, heuristic, player):
    currentCredit = INITIAL_CREDIT

    moves = board.legal_moves()

    if len(moves) == 1:
        return moves[0]

    best_move = (MIN_VALUE - 1, [board._nextPlayer, -1, -1]) # Ally side, so best value is MIN_VALUE by default
    queue = list()


    # Initial search, initialize queue
    for i in moves:
        board.push(i)
        currentValue = MinValue(board, alpha, beta, heuristic, player, startTime, currentCredit, queue, i, 1)
        board.pop()

        if currentValue >= best_move[0]:
            best_move = (currentValue, i)

        # Maybe useless
        if getEllapsedTime(startTime) > MAX_TIME_MILLIS:
            return best_move


    boardSave = board.encode()
    # We are on ally side in the function. We are looking for max value
    while (getEllapsedTime(startTime) < MAX_TIME_MILLIS):
        while (getEllapsedTime(startTime) < MAX_TIME_MILLIS and len(queue) > 0):

            (value, (boardData, initialMove, depth)) = queue.pop(0)
            board.decode(boardData)

            # TODO is it the good function to call ?
            if board._nextPlayer == player:
                currentValue = MinValue(board, alpha, beta, heuristic, player, startTime, currentCredit, queue, initialMove, depth)
            else:    
                currentValue = MaxValue(board, alpha, beta, heuristic, player, startTime, currentCredit, queue, initialMove, depth)


            if currentValue >= best_move[0]:
                best_move = (currentValue, initialMove)


    board.decode(boardSave)

    return best_move



def MaxValue(board, alpha, beta, heuristic, player, startTime, numberCredit, queue, initialMove, depth):
    if numberCredit < 0 or getEllapsedTime(startTime) > MAX_TIME_MILLIS:
        value = heuristic(board, player)
        insertSort(queue, (board.encode(), initialMove, depth), value)

        return value


    if board.is_game_over():

        (nbWhite, nbBlack) = board.get_nb_pieces()
        if player is board._BLACK:
            return MAX_VALUE if nbBlack > nbWhite else MIN_VALUE

        if player is board._WHITE:
            return MAX_VALUE if nbBlack < nbWhite else MIN_VALUE

    # Decrement numberCredit !
    # Is it a good idea to use domination for this ?
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


    # Decrement numberCredit !
    # Is it a good idea to use domination for this ?
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


class SequentialMemory(ImplementedPlayer):

    def __init__(self):
        super().__init__()

        self._BEGIN     = 0
        self._MIDDLE    = 1
        self._END       = 2

        # À la base l'heuristique takeVictory était utilisée, mais dans le cas
        # ou la victoire n'est pas évidente, retourne un coup aléatoire 
        # parmis les coups à -1.... Commencer plus tôt endGame avec takeVitory ?

        self.heuristic_dict = {
            self._BEGIN:    heuristic_takeAllPiece,
            self._MIDDLE:   heuristic_angle,
            self._END:      heuristic_takeAllPiece
        }

        self.state = self._BEGIN



    def updateGameState(self):
        """ Function that estimate when we are in the game """
        boardArray = self._board.get_board()
        
        if self.state is self._BEGIN:

            for i in [1, self._board.get_board_size() - 2]:
                for j in range(1, self._board.get_board_size() - 1):

                    if boardArray[i][j] != self._board._EMPTY:
                        self.state = self._MIDDLE
                        return

                    if boardArray[j][i] != self._board._EMPTY:
                        self.state = self._MIDDLE
                        return


        elif self.state is self._MIDDLE:
            nbPieces = self._board.get_total_pieces()

            if nbPieces >= self._board.get_board_size()**2 - ENDGAME:
                self.state = self._END
                return


    
    def getPlayerName(self):
        return "Memory"


    def nextMove(self):
        if self._board.is_game_over():
            return (-1, -1)

        possibleMoves = self._board.legal_moves()
        numberPossibleMoves = len(possibleMoves)

        if numberPossibleMoves <= 0:
            self._board.push([self._mycolor, -1, -1])

            return (-1, -1)

        self.updateGameState()
        self._board.setInitialDomination()

        startTime = getTimeMillis()
        value = alphaBetaLauncher(self._board, startTime, MIN_VALUE, MAX_VALUE, self.heuristic_dict[self.state], self._mycolor)

        self._board.push(value[1])
        (_,x,y) = value[1]


        return (x,y)
        

    def endGame(self, color):
        """ Nothing to do """
        pass