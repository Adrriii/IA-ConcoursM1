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

        if verbose: print(b.legal_moves())
        while not b.is_game_over():
            if verbose: 
                print("Referee Board:")
                print(b)
                print("Before move", nbmoves)
                print("Legal Moves: ", b.legal_moves())
            nbmoves += 1
            otherplayer = (nextplayer + 1) % 2
            othercolor = b._BLACK if nextplayercolor == b._WHITE else b._WHITE
            
            currentTime = time.time()
            move = players[nextplayer].getPlayerMove()
            totalTime[nextplayer] += time.time() - currentTime
            if verbose: print("Player ", nextplayercolor, players[nextplayer].getPlayerName(), "plays" + str(move))
            (x,y) = move 
            if not b.is_valid_move(nextplayercolor,x,y):
                if verbose or logging: 
                    print(otherplayer, nextplayer, nextplayercolor)
                    print("Problem: illegal move")
                break
            b.push([nextplayercolor, x, y])
            players[otherplayer].playOpponentMove(x,y)

            nextplayer = otherplayer
            nextplayercolor = othercolor

            if verbose: print(b)

        if verbose: print("The game is over")
        if verbose: print(b)
        (nbwhites, nbblacks) = b.get_nb_pieces()
        if verbose: print("Time:", totalTime)
        if verbose: print("Winner: ", end="")
        if nbblacks > nbwhites:
            if verbose or logging: print(player1.getPlayerName()+" wins in "+ str(totalTime[0]) + " seconds of reflexion (against " + str(totalTime[1]) + ")")
            return 3
        elif nbwhites > nbblacks:
            if verbose or logging: print(player2.getPlayerName()+" wins in "+ str(totalTime[1]) + " seconds of reflexion (against " + str(totalTime[0]) + ")")
            return -3
        else:
            if verbose or logging: print("Tie in "+ str(totalTime[0]) + " and " + str(totalTime[1]) + " seconds (Respectively "+player1.getPlayerName()+" and "+player2.getPlayerName()+")")
            return 0
