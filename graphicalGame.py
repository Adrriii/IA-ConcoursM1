import Reversi
from globalGame import Game
from display import Display
import time
from io import StringIO
import sys
from time import sleep

class GraphicalGame(Game):

    def init(self,player1,player2):
        super().init(player1,player2)

        self._display = Display()
        self._display.newGame(self.b.get_board_size())
        
        self._fps = 1000
        self._last_frame = 0

    def now(self):
        return int(round(time.time() * 1000))

    def play(self,player1,player2,logging=False):
        self.init(player1,player2)

        self._display.drawBoard(self.players[self.nextplayer].getPlayerName(), self.nextplayercolor)
        
        while not self.b.is_game_over() and self.totalTime[0] <= self.time_limit and self.totalTime[1] <= self.time_limit:
            nextmove = self.nextMove(logging)
            if( nextmove == (-2,-2) ):
                break
            if( nextmove == (-1,-1) ):
                if(not self.skipped):
                    self.skipped = True
                else:
                    break
            else:
                self.skipped = False
            self._display.performMove(nextmove[0],nextmove[1],nextmove[2])

            if(self.now() - self._last_frame >= 1000 / self._fps):
                self._display.drawBoard(self.players[self.nextplayer].getPlayerName(), self.nextplayercolor)
                self._last_frame = self.now()
        
        return self.processGameEnd(logging)
