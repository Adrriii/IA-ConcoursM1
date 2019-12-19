import graphicalGame
import globalGame
import myPlayer
from players import *
import time
import cProfile

def vsRandom():
    return graphicalGame.GraphicalGame().play(myPlayer.myPlayer(),randomPlayer())

def compare(player1,player2,rounds,graphical=False):
    score = 0

    for r in range(0,rounds):
        if(graphical):
            score += graphicalGame.GraphicalGame().play(player1(),player2(),True) 
        else:
            score += globalGame.Game().play(player1(),player2(),True)
        
        time.sleep(5)

    print(player1().getPlayerName() + " (black) vs " + player2().getPlayerName() + " (white) -> " +  str(((score/3) / rounds)*100) + "%")

# compare(MetaPlayer, human, 10)
# cProfile.run('compare(SequentialMemory, randomPlayer, 1, False)')
compare(SequentialMemory, randomPlayer, 5, True)
# compare(MetaPlayer, randomPlayer, 5)
# compare(MetaPlayer, TestPlayer, 5)

