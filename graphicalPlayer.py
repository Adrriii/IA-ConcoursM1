
import time
from Reversi import Board
from playerInterface import *
from display import Display

class GraphicalPlayer(PlayerInterface):

    def __init__(self):
        self._board = Board(10)
        self._display = Display()
        self._mycolor = None

    # Redefine to chose next move
    def nextMove(self):
        return (-1,-1)

    def getPlayerMove(self):
        self._display.drawBoard()
        move = self.nextMove()
        self._display.performMove(self._mycolor, move[0], move[1])
        self._display.drawBoard()
        return move

    def playOpponentMove(self, x,y):
        self._board.push([self._opponent, x, y])
        self._display.performMove(self._opponent, x, y)
        self._display.drawBoard()

    def newGame(self, color):
        self._mycolor = color
        self._display.newGame(self._board, self.getPlayerName(), color)
        self._opponent = 1 if color == 2 else 2