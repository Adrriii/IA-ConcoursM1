import Reversi
import myPlayer
import time
from io import StringIO
import sys

class Game():

    def init(self,player1,player2):
        board_size = 8
        self.b = Reversi.Board(board_size)
        self.player1 = player1
        self.player2 = player2

        self.players = []
        self.player1.newGame(self.b._BLACK,board_size)
        self.players.append(self.player1)
        self.player2.newGame(self.b._WHITE,board_size)
        self.players.append(self.player2)

        self.totalTime = [0,0] # total real time for each player
        self.nextplayer = 0
        self.nextplayercolor = self.b._BLACK
        self.nbmoves = 1

        self.time_limit = 300

    def nextMove(self,logging=False):
        self.nbmoves += 1
        otherplayer = (self.nextplayer + 1) % 2
        othercolor = self.b._BLACK if self.nextplayercolor == self.b._WHITE else self.b._WHITE
            
        currentTime = time.time()
        move = self.players[self.nextplayer].getPlayerMove()
        self.totalTime[self.nextplayer] += time.time() - currentTime
            
        (x,y) = move 

        if not self.b.is_valid_move(self.nextplayercolor,x,y):
            print("ERROR: illegal move from "+ ("Black" if self.nextplayercolor == self.b._BLACK else "White"))
            return (-1,-1)
        self.b.push([self.nextplayercolor, x, y])
        self.players[otherplayer].playOpponentMove(x,y)

        self.nextplayer = otherplayer
        self.nextplayercolor = othercolor

        return [self.b._BLACK if self.nextplayercolor == self.b._WHITE else self.b._WHITE, x, y]

    def processGameEnd(self, logging = False):
        if self.b.is_game_over():

            (nbwhites, nbblacks) = self.b.get_nb_pieces()

            if nbblacks > nbwhites:
                if logging: print(self.player1.getPlayerName()+" wins in "+ str(self.totalTime[0]) + " seconds of reflexion (against " + str(self.totalTime[1]) + ")")
                return 3
            elif nbwhites > nbblacks:
                if logging: print(self.player2.getPlayerName()+" wins in "+ str(self.totalTime[1]) + " seconds of reflexion (against " + str(self.totalTime[0]) + ")")
                return -3
            else:
                if logging: print("Tie in "+ str(self.totalTime[0]) + " and " + str(self.totalTime[1]) + " seconds (Respectively "+self.player1.getPlayerName()+" and "+self.player2.getPlayerName()+")")
                return 0

        if(self.totalTime[0] > self.time_limit):
                if logging: print(self.player2.getPlayerName()+" wins by timeout in "+ str(self.totalTime[1]) + " seconds of reflexion")
                return -3

        if(self.totalTime[1] > self.time_limit):
                if logging: print(self.player1.getPlayerName()+" wins by timeout in "+ str(self.totalTime[0]) + " seconds of reflexion")
                return 3

        throw_player = self.players[self.nextplayer]

        if(throw_player == self.player1):
            if logging: print(self.player1.getPlayerName()+" is eliminated : Illegal move")
            return 3

        if(throw_player == self.player2):
            if logging: print(self.player2.getPlayerName()+" is eliminated : Illegal move")
            return -3

        if logging: print("Game was inconclusive.")
        return -3
        
    def play(self,player1,player2,logging=False):
        self.init(player1,player2)

        while not self.b.is_game_over() and self.totalTime[0] <= self.time_limit and self.totalTime[1] <= self.time_limit:
            nextmove = self.nextMove(logging)
            if( nextmove == (-1,-1) ):
                break

        return self.processGameEnd(logging)
