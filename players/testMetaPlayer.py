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

    (m, x, y) = board._last_move

    if (x, y) in board.get_corner_coord():
        return MAX_VALUE


    # score *= (board.getCurrentDomination(player) - board.getInitialDomination(player))

    return score


def heuristic_takeVictory(board, player):
    """ Heuristic for victory """
    (nbWhite, nbBlack) = board.get_nb_pieces()

    if player is board._BLACK:
        return 1 if nbBlack > nbWhite else -1

    return 1 if nbBlack < nbWhite else -1



# Maximum time for each move. Has to be update dynamically
MAX_TIME_MILLIS = 5000

INITIAL_CREDIT = 40


GOOD_MOVE_VALUE = 2
MEDIUM_MOVE_VALUE = 15
BAD_MOVE_VALUE = 35


# TODO: Mieux évaluer la valeur des pièces en fonction de leur position
# TODO: Changer l'heuristic au cours de l'exploration ? Plus précis mais prend du temps de calcul
class ThreadSearch(Thread):
    """ Simple thread for on specific move """

    def __init__(self, board, initialMove, queue, explorationAlgo, heuristic, startTime, alpha=-9999999, beta=9999999):
        Thread.__init__(self)

        self.heuristic = heuristic
        self.explorationAlgo = explorationAlgo

        self.board = board
        self.initialMove = initialMove
        self.queue = queue

        self.startTime = startTime

        self.alpha = alpha
        self.beta = beta

    def run(self):
        self.board.setInitialDomination()

        self.board.push(self.initialMove)
        value = self.explorationAlgo(self.board, self.startTime, self.alpha, self.beta, self.heuristic, self.board._nextPlayer)
        self.board.pop()


        self.queue.put((self.initialMove, value))


# Must be higher than any heuristic resutl
MAX_VALUE = 999999999
MIN_VALUE = -MAX_VALUE


def alphaBetaLauncher(board, startTime, alpha, beta, heuristic, player):
    currentCredit = INITIAL_CREDIT

    moves = board.legal_moves()

    indexes = [i for i in range(len(moves))]    
    
    # Will contain result (moveIndex, heuristicValue)
    resultList = list()

    best_move = MAX_VALUE # Enemy side, so badest value is MAX_VALUE

    # We are on enemy side in the function. We are looking for min value
    while (getEllapsedTime(startTime) < MAX_TIME_MILLIS):

        for i in indexes:

            board.push(moves[i])
            currentValue = MaxValue(board, alpha, beta, heuristic, board._nextPlayer, startTime, currentCredit, 2) # Already 2 moves 
            board.pop()

            ################################################
            # On insert les valeurs dans l'ordre croissant

            insertIndex = 0 

            for j in range(len(resultList)):
                if resultList[j][1] > currentValue:
                    insertIndex = j
                    break

            resultList.insert(insertIndex, (i, currentValue))

        ###########################
        # Permutation des indexes

        for i in range(len(resultList)):
            indexes[i] = resultList[i][0]

        if resultList[0][1] < best_move:
            best_move = resultList[0][1]

        resultList = list()
        currentCredit += 10

    # Return the best value, in enemy side is the min Value
    return best_move



def MaxValue(board, alpha, beta, heuristic, player, startTime, numberCredit, depth):
    if numberCredit < 0:
        print("Depth -> ", depth)
        return heuristic(board, player)

    if getEllapsedTime(startTime) > MAX_TIME_MILLIS:
        print("Depth -> ", depth)
        return heuristic(board, player)

    if board.is_game_over():
        print("Depth -> ", depth)
        (nbWhite, nbBlack) = board.get_nb_pieces()
        if player is board._BLACK:
            return MAX_VALUE if nbBlack > nbWhite else MIN_VALUE

        if player is board._WHITE:
            return MAX_VALUE if nbBlack < nbWhite else MIN_VALUE

    creditForNext = 0

    for move in board.legal_moves():

        board.push(move)

        # Decrement numberCredit !
        # Is it a good idea to use domination for this ?
        dominationDiff = board.getCurrentDomination(player) - board.getInitialDomination(player)

        
        if dominationDiff < -0.1:
            creditForNext = numberCredit - BAD_MOVE_VALUE
        elif dominationDiff < 0.2:
            creditForNext = numberCredit - MEDIUM_MOVE_VALUE
        else:
            creditForNext = numberCredit - GOOD_MOVE_VALUE

        alpha = max(alpha, MinValue(board, alpha, beta, heuristic, player, startTime, creditForNext, depth + 1))
        board.pop()

        if alpha >= beta:
            return beta
    
    return alpha



def MinValue(board, alpha, beta, heuristic, player, startTime, numberCredit, depth):
    if numberCredit < 0:
        print("Depth -> ", depth)
        return heuristic(board, player)

    if getEllapsedTime(startTime) > MAX_TIME_MILLIS:
        print("Depth -> ", depth)
        return heuristic(board, player)

    if board.is_game_over():
        print("Depth -> ", depth)
        (nbWhite, nbBlack) = board.get_nb_pieces()
        if player is board._BLACK:
            return MAX_VALUE if nbBlack > nbWhite else MIN_VALUE

        if player is board._WHITE:
            return MAX_VALUE if nbBlack < nbWhite else MIN_VALUE

    creditForNext = 0

    for move in board.legal_moves():

        board.push(move)

        # Decrement numberCredit !
        # Is it a good idea to use domination for this ?
        dominationDiff = board.getCurrentDomination(player) - board.getInitialDomination(player)

        
        if dominationDiff < -0.1:
            creditForNext = numberCredit - BAD_MOVE_VALUE
        elif dominationDiff < 0.2:
            creditForNext = numberCredit - MEDIUM_MOVE_VALUE
        else:
            creditForNext = numberCredit - GOOD_MOVE_VALUE

        beta = min(beta, MaxValue(board, alpha, beta, heuristic, player, startTime, creditForNext, depth + 1))
        board.pop()

        if alpha >= beta:
            return alpha
    
    return beta


class MetaPlayer(ImplementedPlayer):

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
                        print("Switch state to middle !")
                        self.state = self._MIDDLE
                        return

                    if boardArray[j][i] != self._board._EMPTY:
                        print("Switch state to middle !")
                        self.state = self._MIDDLE
                        return


        elif self.state is self._MIDDLE:
            nbPieces = self._board.get_total_pieces()

            if nbPieces >= self._board.get_board_size()**2 - ENDGAME:
                print("switch state to end !")
                self.state = self._END
                return


    
    def getPlayerName(self):
        return "Rob's algo para"


    def nextMove(self):
        if self._board.is_game_over():
            return (-1, -1)

        possibleMoves = self._board.legal_moves()
        numberPossibleMoves = len(possibleMoves)

        if numberPossibleMoves <= 0:
            self._board.push([self._mycolor, -1, -1])

            return (-1, -1)

        self.updateGameState()
        moves = {}
        best = -999999

        threadResultQueue = Queue()
        threadList = list()

        startTime = getTimeMillis()

        for i in range(numberPossibleMoves):
            # start Thread using default alpha/beta value. 
            # TODO: Change it for endGame !

            # self, board, initialMove, queue, explorationAlgo, heuristic, startTime, alpha=-9999999, beta=9999999)

            threadList.append(
                ThreadSearch(
                    copy.deepcopy(self._board),
                    possibleMoves[i],
                    threadResultQueue,
                    alphaBetaLauncher,
                    self.heuristic_dict[self.state],
                    startTime
                )
            )
            threadList[i].start()

        for i in range(numberPossibleMoves):
            (move, value) = threadResultQueue.get()

            if value > best:
                best = value
            
            # Peut être mieux fait ?
            if str(value) in moves:
                moves[str(value)].append(move)
            else:
                moves[str(value)] = [move]
                
        if(str(best) not in moves.keys()):
            self._board.push([self._mycolor,-1,-1])
            return (-1,-1)

        m = choice(moves[str(best)])
        self._board.push(m)
        (c,x,y) = m

        print("Value -> ", best)
        print("Ellapsed time for this move in millis -> ", getEllapsedTime(startTime))

        return (x,y)
        

    def endGame(self, color):
        """ Nothing to do """
        pass