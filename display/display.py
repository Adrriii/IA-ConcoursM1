import pygame
from pygame.locals import *

from Reversi import Board

class Display():
    def __init__(self, board):
        self.board = board