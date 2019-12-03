import graphicalGame
import globalGame
import myPlayer
from players import *
import time

def vsRandom():
    return graphicalGame.GraphicalGame().play(myPlayer.myPlayer(),randomPlayer())

def compare(player1,player2,rounds,graphical=False):
    score = 0

    for r in range(0,rounds):
        if(graphical):
            score += graphicalGame.GraphicalGame().play(player1(),player2(),True) 
        else:
            score += globalGame.Game().play(player1(),player2(),True) 

    print(player1().getPlayerName() + " (black) vs " + player2().getPlayerName() + " (white) -> " +  str(((score/3) / rounds)*100) + "%")

# compare(MetaPlayer, human, 10)
compare(SequentialIterative, SequentialIterativeRandom, 1000, False)
# compare(MetaPlayer, randomPlayer, 5)
# compare(MetaPlayer, TestPlayer, 5)

