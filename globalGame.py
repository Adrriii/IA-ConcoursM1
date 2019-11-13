import Reversi
import myPlayer
import time
from io import StringIO
import sys

class Game():

    def __init__(self):
        pass

    def play(self,player1,player2,verbose=False,logging=False):
        b = Reversi.Board(10)

        players = []
        player1.newGame(b._BLACK)
        players.append(player1)
        player2.newGame(b._WHITE)
        players.append(player2)

        totalTime = [0,0] # total real time for each player
        nextplayer = 0
        nextplayercolor = b._BLACK
        nbmoves = 1

        outputs = ["",""]
        sysstdout= sys.stdout
        stringio = StringIO()

        if logging: print(b.legal_moves())
        while not b.is_game_over():
            if logging: 
                print("Referee Board:")
                print(b)
                print("Before move", nbmoves)
                print("Legal Moves: ", b.legal_moves())
            nbmoves += 1
            otherplayer = (nextplayer + 1) % 2
            othercolor = b._BLACK if nextplayercolor == b._WHITE else b._WHITE
            
            currentTime = time.time()
            sys.stdout = stringio
            move = players[nextplayer].getPlayerMove()
            sys.stdout = sysstdout
            playeroutput = "\r" + stringio.getvalue()
            stringio.truncate(0)
            if logging: print(("[Player "+str(nextplayer) + "] ").join(playeroutput.splitlines(True)))
            outputs[nextplayer] += playeroutput
            totalTime[nextplayer] += time.time() - currentTime
            if logging: print("Player ", nextplayercolor, players[nextplayer].getPlayerName(), "plays" + str(move))
            (x,y) = move 
            if not b.is_valid_move(nextplayercolor,x,y):
                if logging: 
                    print(otherplayer, nextplayer, nextplayercolor)
                    print("Problem: illegal move")
                break
            b.push([nextplayercolor, x, y])
            players[otherplayer].playOpponentMove(x,y)

            nextplayer = otherplayer
            nextplayercolor = othercolor

            if logging: print(b)

        if logging: print("The game is over")
        if logging: print(b)
        (nbwhites, nbblacks) = b.get_nb_pieces()
        if logging: print("Time:", totalTime)
        if verbose: print("Winner: ", end="")
        if nbwhites > nbblacks:
            return 3
        elif nbblacks > nbwhites:
            return -3
        else:
            return 0
