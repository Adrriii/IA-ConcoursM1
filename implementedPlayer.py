
import time
from Reversi_perso import MyBoard
from playerInterface import *
from display import Display

class ImplementedPlayer(PlayerInterface):

    def __init__(self):
        self._mycolor = None

    # Redefine to chose next move
    def nextMove(self):
        return (-1,-1)

    def getPlayerMove(self):
        move = self.nextMove()
        return move

    def playOpponentMove(self, x,y):
        self._board.push([self._opponent, x, y])

    def newGame(self, color, board_size = 10):
        self._board = MyBoard(board_size)
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2