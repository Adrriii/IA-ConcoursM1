
import time

def heuristic1(b,player): 
    # Simplest heuristic : difference in amount of tiles
    (nbwhites, nbblacks) = b.get_nb_pieces()
    return nbwhites - nbblacks if player == 1 else nbblacks - nbwhites

def heuristic2(b,player):

    score = 0

    (nbwhites, nbblacks) = b.get_nb_pieces()
    difference = nbwhites - nbblacks if player == 1 else nbblacks - nbwhites

    score += difference

    boardSize = b.get_board_size()
    boardEdgeIndex = boardSize - 1
    
    for x in range(0,boardSize):
        for y in [0,boardEdgeIndex]:
            if(b._board[x][y] == b._EMPTY):
                pass

            add = 1
            if(b._board[x][y] != player):
                add = -1

            if(x == 0 or x == boardEdgeIndex or y == 0 or y == boardEdgeIndex):
                add *= 3
                if((x == 0 or x == boardEdgeIndex) and (y == 0 or y == boardEdgeIndex)):
                    add *= 3
                    
            score += add
    
    for y in range(1,boardEdgeIndex):
        for x in [0,boardEdgeIndex]:
            if(b._board[x][y] == b._EMPTY):
                pass

            add = 1
            if(b._board[x][y] != player):
                add = -1

            if(x == 0 or x == boardEdgeIndex or y == 0 or y == boardEdgeIndex):
                add *= 3
                if((x == 0 or x == boardEdgeIndex) and (y == 0 or y == boardEdgeIndex)):
                    add *= 10

            score += add
            
    return score

def heuristic_angle(board, color, cst=50):
    boardSize = board.get_board_size()
    boardArray = board.get_board()

    (nbwhites, nbblacks) = board.get_nb_pieces()
    score = (nbblacks/(nbwhites + nbblacks)) * 100 if color == board._BLACK else (nbwhites/(nbblacks + nbwhites)) * 100


    if (boardArray[0][0] == color):
        score += cst * 100

        for i in range(1, boardSize - 1):
            if boardArray[i][0] == color:
                score += cst * 5
            else:
                break

        for i in range(1, boardSize - 1):
            if boardArray[0][i] == color:
                score += cst * 5
            else:
                break
            
    elif (boardArray[0][0] != board._EMPTY):
        score -= cst * 1000



    if (boardArray[0][boardSize - 1] == color):
        score += cst * 100

        for i in range(boardSize - 2, -1):
            if boardArray[0][i] == color:
                score += cst * 5
            else:
                break

        for i in range(1, boardSize - 1):
            if boardArray[i][boardSize - 1] == color:
                score += cst * 5
            else:
                break

    elif (boardArray[0][0] != board._EMPTY):
        score -= cst * 1000



    if (boardArray[boardSize - 1][boardSize - 1] == color):
        score += cst * 100

        for i in range(boardSize - 2, -1):
            if boardArray[board - 1][i] == color:
                score += cst * 5
            else:
                break

        for i in range(boardSize - 2, -1):
            if boardArray[i][board - 1] == color:
                score += cst * 5
            else:
                break
        
    elif (boardArray[0][0] != board._EMPTY):
        score -= cst * 1000


    if (boardArray[boardSize - 1][0] == color):
        score += cst * 100

        for i in range(boardSize - 2, -1):
            if boardArray[i][0] == color:
                score += cst * 5
            else:
                break

        for i in range(1, boardSize - 1):
            if boardArray[boardSize - 1][i] == color:
                score += cst * 5
            else:
                break

    elif (boardArray[0][0] != board._EMPTY):
        score -= cst * 1000

    # Take to much time
    # if board._nextPlayer != color:
    #     score -= len(board.legal_moves())
    # else:
    #     score += len(board.legal_moves())

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
            if player == b._BLACK and nbwhites > nbblacks:
                return -999 + depth
            elif nbblacks > nbwhites:
                return 999 - depth
            else:
                return 0
        else:
            return current_val

    next_player = -player

    diff = -current_val - val
    
    if diff < 200:
        # Uninteresting move
        credit -= 35
    elif diff>=250:
        credit -= 5
    elif diff>=230:
        credit -= 7
    else:
        credit -= 20

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


def negAlphaBetaDepth(board, alpha, beta, depth, heuristic, color):
    if depth == 0 or board.is_game_over():
        return heuristic(board, color)

    for move in board.legal_moves():

        board.push(move)
        value = -negAlphaBetaDepth(board, -beta, -alpha, depth - 1, heuristic, board._nextPlayer)
        #print(value)
        board.pop()

        if value > alpha:
            if value > beta:
                return value
            
            alpha = value
    
    return alpha