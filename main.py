import globalGame
import myPlayer
from players import *

def vsRandom():
    return globalGame.Game().play(myPlayer.myPlayer(),randomPlayer())

def compare(player1,player2,rounds):
    score = 0

    for r in range(0,rounds):
        score += globalGame.Game().play(player1,player2)

    print(player1.getPlayerName() + " vs " + player2.getPlayerName() + " -> " +  str(score / rounds))

compare(myPlayer.myPlayer(),randomPlayer(),100)