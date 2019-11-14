#!/usr/bin/env python3

from display import Display
from Reversi import Board

import time

board = Board(10)
display = Display(board)
display.drawBackground()
display.drawBoard()
display.refreshWindow()

time.sleep(4)