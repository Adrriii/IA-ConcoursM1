
import time

def heuristic1(b,player):
    # Simplest heuristic : difference in amount of tiles
    (nbwhites, nbblacks) = b.get_nb_pieces()
    return nbwhites - nbblacks if player == 1 else nbblacks - nbwhites

def heuristic2(b,player):
    score = 0

    (nbwhites, nbblacks) = b.get_nb_pieces()
    difference = nbwhites - nbblacks if player == 1 else nbblacks - nbwhites

    score += difference / 15

    return score

def now():
    return int(round(time.time() * 1000))

def NegaAlphaBetaCredit(b, heuristic, alpha, beta, player, credit, current_val, val, depth, credit_run_out_time, thinking_start):
    game_over = b.is_game_over()
    
    spent = now() - thinking_start
    
    if(spent >= credit_run_out_time /10):
        remove = int((spent / credit_run_out_time) * 10)
        credit -= remove

    if credit<0 or game_over:
        if game_over:
            (nbwhites, nbblacks) = b.get_nb_pieces()
            if nbwhites > nbblacks:
                return 999 - depth
            elif nbblacks > nbwhites:
                return -999 + depth
            else:
                return 0
        else:
            return current_val

    next_player = -player

    diff = -current_val - val
    if diff < 2:
        # Uninteresting move
        credit -= 35
    elif diff>=4:
        credit -= 5
    elif diff>=8:
        credit -= 2
    else:
        credit -= 10

    ms = []
    for m in b.legal_moves():
        b.push(m)
        val = heuristic(b,0 if player == -1 else 1)
        ms.append((val,m))
        b.pop()

    for m in sorted(ms, key=lambda x: x[0]):
        mv = m[1]
        b.push(mv)
        val = -NegaAlphaBetaCredit(b, heuristic, -beta, -alpha, next_player, credit, val, m[0], depth+1, credit_run_out_time, thinking_start)
        b.pop()

        if val>alpha:
            alpha = val
            if alpha>beta:
                return alpha

        
    return alpha