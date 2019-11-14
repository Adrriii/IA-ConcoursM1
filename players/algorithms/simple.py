def heuristic1(b,player):
    # Simplest heuristic : difference in amount of tiles
    (nbwhites, nbblacks) = b.get_nb_pieces()
    return nbwhites - nbblacks if player == 1 else nbblacks - nbwhites

def heuristic2(b,player):
    score = 0

    (nbwhites, nbblacks) = b.get_nb_pieces()
    difference = nbwhites - nbblacks if player == 1 else nbblacks - nbwhites

    score += difference / 15

def maxValue(b,heuristic,alpha,beta, player,depth, max_depth):

    game_over = b.is_game_over()
    if depth>=max_depth or game_over:
        if game_over:
            (nbwhites, nbblacks) = b.get_nb_pieces()
            if nbwhites > nbblacks:
                return 999 - depth
            elif nbblacks > nbwhites:
                return -999 + depth
            else:
                return 0
        else:
            return heuristic(b,player)
            
    for m in b.legal_moves():
        b.push(m)
        val = minValue(b,heuristic,alpha,beta,player,depth+1,max_depth)
        b.pop()
        if(alpha < val):
            alpha = val
        if(alpha >= beta):
            return beta
    return alpha
            
def minValue(b,heuristic,alpha,beta, player, depth, max_depth):
    
    game_over = b.is_game_over()
    if depth>=max_depth or game_over:
        if game_over:
            (nbwhites, nbblacks) = b.get_nb_pieces()
            if nbwhites > nbblacks:
                return 999 - depth
            elif nbblacks > nbwhites:
                return -999 + depth
            else:
                return 0
        else:
            return heuristic(b,player)
            
    for m in b.legal_moves():
        b.push(m)
        val = maxValue(b,heuristic,alpha,beta,player,depth+1,max_depth)

        b.pop()
        if(beta > val):
            beta = val
        if(alpha >= beta):
            return alpha
    return beta
