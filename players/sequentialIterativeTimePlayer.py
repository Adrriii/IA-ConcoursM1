# -*- coding: utf-8 -*-

from Reversi import Board
from implementedPlayer import *
from players.algorithms.medium import *

from threading import Thread
from queue import Queue
from random import randint, choice

import copy
import time


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


INITIAL_CREDIT = 40

GOOD_MOVE_VALUE = 2
MEDIUM_MOVE_VALUE = 15
BAD_MOVE_VALUE = 35




# Must be higher than any heuristic resutl
MAX_VALUE = 999999999
MIN_VALUE = -MAX_VALUE


def alphaBetaLauncher(board, startTime, alpha, beta, heuristic, player):
    currentCredit = INITIAL_CREDIT

    moves = board.legal_moves()

    indexes = [i for i in range(len(moves))]    
    
    # Will contain result (moveIndex, heuristicValue, move)
    resultList = list()

    best_move = (MIN_VALUE - 1, [board._nextPlayer, -1, -1]) # Ally side, so best value is MIN_VALUE

    # We are on ally side in the function. We are looking for max value
    while (getEllapsedTime(startTime) < MAX_TIME_MILLIS):

        for i in indexes:

            board.push(moves[i])
            currentValue = MinValue(board, alpha, beta, heuristic, player, startTime, currentCredit, 1)
            board.pop()


            ################################################
            # On insere les valeurs dans l'ordre croissant

            insertIndex = len(resultList)

            for j in range(insertIndex):
                if resultList[j][1] < currentValue:
                    insertIndex = j
                    break

            resultList.insert(insertIndex, (i, currentValue, moves[i]))

        ###########################
        # Permutation des indexes

        for i in range(len(resultList)):
            indexes[i] = resultList[i][0]

        if resultList[0][1] >= best_move[0]:
            best_move = (resultList[0][1], resultList[0][2])

        resultList = list()
        currentCredit += 10

    # Return the best value, in enemy side is the min Value
    return best_move



def MaxValue(board, alpha, beta, heuristic, player, startTime, numberCredit, depth):
    if numberCredit < 0:
        return heuristic(board, player)

    if getEllapsedTime(startTime) > MAX_TIME_MILLIS:
        return heuristic(board, player)

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
        alpha = max(alpha, MinValue(board, alpha, beta, heuristic, player, startTime, numberCredit, depth + 1))
        board.pop()

        if alpha >= beta:
            return beta
    
    return alpha



def MinValue(board, alpha, beta, heuristic, player, startTime, numberCredit, depth):
    if numberCredit < 0:
        return heuristic(board, player)

    if getEllapsedTime(startTime) > MAX_TIME_MILLIS:
        return heuristic(board, player)

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
        beta = min(beta, MaxValue(board, alpha, beta, heuristic, board._nextPlayer, startTime, numberCredit, depth + 1))
        board.pop()

        if alpha >= beta:
            return alpha
    
    return beta


class SequentialIterative(ImplementedPlayer):

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
        return "Rob's algo seq"


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
        value = alphaBetaLauncher(self._board, startTime, MIN_VALUE, MAX_VALUE, self.heuristic_dict[self.state], self._board._nextPlayer)

        self._board.push(value[1])
        (_,x,y) = value[1]

        return (x,y)
        

    def endGame(self, color):
        """ Nothing to do """
        pass