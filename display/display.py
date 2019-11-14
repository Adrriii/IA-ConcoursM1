#!/usr/bin/env python3

import pygame
from pygame.locals import *

from Reversi import Board

class Display():
    """ Display the game """
    _WIDTH = 640
    _HEIGHT = 720

    _BOARD_OFFSET = 10
    _BOARD_WIDTH = _WIDTH - 2 * _BOARD_OFFSET

    # take on https://coolors.co/, from dark to light
    _COLORS_UGLY = [
        pygame.Color("#4e5340"),
        pygame.Color("#697268"),
        pygame.Color("#95a3a4"),
        pygame.Color("#b7d1da"),
        pygame.Color("#e2e8dd")
    ]

    _COLORS = [
        pygame.Color("#582c4d"),
        pygame.Color("#a26769"),
        pygame.Color("#d5b9b2"),
        pygame.Color("#ece2d0"),
        pygame.Color("#bfb5af")
    ]

    def __init__(self, board):
        self.initPygame()
        self.setBoard(board)
        self.create_window()

    def create_window(self):
        self.window = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
        

    def initPygame(self):
        pygame.init()
        pygame.font.init()

    
    def setBoard(self, board):
        self.board = board


    def drawBackground(self):
        pygame.draw.rect(self.window, self._COLORS[3], Rect((0, 0), (self._WIDTH, self._HEIGHT)))
    

    def drawBoardGrid(self):
        boardSize = self.board.get_board_size()
        caseSize = self._BOARD_WIDTH // boardSize

        for i in range(1, boardSize):
            pygame.draw.line(
                self.window,
                self._COLORS[0],
                (self._BOARD_OFFSET, self._BOARD_OFFSET + i * caseSize),
                (self._BOARD_WIDTH + self._BOARD_OFFSET , self._BOARD_OFFSET + i * caseSize),
                1
            )

            pygame.draw.line(
                self.window,
                self._COLORS[0],
                (self._BOARD_OFFSET + i * caseSize, self._BOARD_OFFSET),
                (self._BOARD_OFFSET + i * caseSize, self._BOARD_WIDTH + self._BOARD_OFFSET),
                1
            )


    def drawPiece(self, x, y, size, type):
        pygame.draw.circle(
            self.window, 
            self._COLORS[3 if type == self.board._WHITE else 1],
            (x + size//2, y + size//2),
            size//2,
            0 # fill the circle
        )


    def drawBoard(self):
        boardSize = self.board.get_board_size()
        boardArray = self.board.get_board()
        caseSize = self._BOARD_WIDTH // boardSize

        pygame.draw.rect(
            self.window,
            self._COLORS[4],
            Rect(
                (self._BOARD_OFFSET, self._BOARD_OFFSET),
                (self._BOARD_WIDTH, self._BOARD_WIDTH)
            )
        )

        self.drawBoardGrid()

        for x in range(boardSize):
            for y in range(boardSize):
                if boardArray[x][y] == self.board._EMPTY:
                    continue

                self.drawPiece(
                    x * caseSize + self._BOARD_OFFSET, 
                    y * caseSize + self._BOARD_OFFSET,
                    caseSize,
                    boardArray[x][y]
                )

    def refreshWindow(self):
        pygame.display.flip()