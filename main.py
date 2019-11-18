import graphicalGame
import myPlayer
from players import *

def vsRandom():
    return graphicalGame.GraphicalGame().play(myPlayer.myPlayer(),randomPlayer())

def compare(player1,player2,rounds):
    score = 0

    for r in range(0,rounds):
        score += graphicalGame.GraphicalGame().play(player1(),player2(),True)

    print(player1().getPlayerName() + " vs " + player2().getPlayerName() + " -> " +  str(score / rounds))

compare(NegaBetaCredit,TestPlayer,100)
