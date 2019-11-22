import graphicalGame
import myPlayer
from players import *
import time

def vsRandom():
    return graphicalGame.GraphicalGame().play(myPlayer.myPlayer(),randomPlayer())

def compare(player1,player2,rounds):
    score = 0

    for r in range(0,rounds):
        score += graphicalGame.GraphicalGame().play(player1(),player2(),True)
        time.sleep(3.)   

    print(player1().getPlayerName() + " vs " + player2().getPlayerName() + " -> " +  str(score / rounds))

# compare(TestPlayer, NegaBetaCredit, 10)
compare(MetaPlayer, TestPlayer, 5)
