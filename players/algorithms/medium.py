
import time
import random

from book.parse_opening import get_book

# book = {'65': {'46': {'33': {'43': {'34': {'23': {'35': {}, '36': {}, '47': {}}, '64': {'35': {'23': {'32': {'24': {'36': {'42': {'13': {}, '53': {}, '56': {'25': {'15': {}, '53': {'63': {'74': {}}}}}}, '56': {'25': {}, '53': {}}}, '53': {'56': {'36': {'66': {}, '74': {}}}}}, '53': {'42': {'24': {}, '36': {}}}, '56': {'24': {'66': {'36': {'26': {}}}}, '36': {'24': {'25': {'42': {'13': {}, '53': {'16': {'31': {'26': {}, '47': {}}, '37': {}, '63': {}, '66': {}}}, '67': {}}}}, '26': {'24': {'66': {'37': {'25': {}}, '73': {'25': {}}}}}}}}, '42': {'24': {}, '36': {'24': {}, '25': {}, '26': {}}, '53': {'24': {}, '32': {}}}, '52': {'36': {}, '53': {}}}, '24': {'23': {'25': {}, '32': {'47': {'36': {}, '37': {}}}, '36': {}, '56': {'36': {'25': {'53': {'32': {}, '62': {'16': {'15': {}}, '67': {}}}}}}}, '25': {'36': {'63': {'15': {}, '56': {'53': {'42': {}, '76': {'26': {}, '66': {'75': {'47': {'73': {'26': {}, '57': {}}}}}}}}, '66': {}}}, '56': {}}, '36': {'56': {'13': {}}}, '53': {}}}, '53': {'63': {'56': {'24': {'35': {}, '36': {}}, '36': {'35': {}, '74': {}}, '66': {'74': {'35': {}, '52': {}, '73': {}}}}, '74': {'52': {}, '66': {}, '73': {'66': {}, '75': {}}, '75': {}}}, '66': {'36': {'35': {'47': {'37': {}, '57': {'26': {}, '56': {'38': {}}}}, '56': {}}}}}, '56': {'23': {'32': {'53': {'42': {'24': {}, '35': {}}}}, '42': {'35': {}, '53': {}}, '52': {'35': {}, '53': {}}}, '66': {'53': {'35': {'36': {'25': {}, '26': {}}, '74': {}}}, '57': {}}}, '66': {'24': {'32': {'52': {}, '63': {}}, '63': {'56': {'53': {'75': {'25': {}, '76': {}}}}}}, '63': {'53': {'24': {}, '75': {'74': {}, '76': {}}}, '56': {'57': {'36': {'76': {'68': {'35': {}}, '75': {}}}, '47': {'35': {'26': {}, '36': {'76': {'48': {}, '75': {}}}}, '76': {'48': {}, '68': {}, '75': {}}}, '67': {'35': {'26': {'24': {}, '25': {}, '75': {}, '76': {}}}}}}, '74': {'73': {'35': {}, '56': {'23': {}}}, '75': {}}}, '75': {'36': {}, '53': {'63': {'74': {'52': {}, '83': {'36': {}, '37': {}, '56': {}, '73': {}}}, '76': {'52': {}, '67': {}}}}, '56': {'35': {}, '47': {}, '67': {'37': {}, '47': {'35': {'73': {'53': {}}}}, '53': {}, '76': {}, '85': {}}}, '63': {}, '76': {}}}}}, '35': {'64': {'53': {}, '63': {}}}}, '64': {}, '75': {}}, '34': {'43': {'35': {'24': {'33': {'42': {'26': {'36': {'25': {'56': {'13': {'15': {}}}}}}}}, '47': {'64': {'53': {'63': {}}}}}, '64': {'47': {}, '53': {'63': {'32': {'24': {'25': {'42': {'47': {'37': {'57': {'66': {}}}}}}}, '36': {'47': {}, '56': {'42': {'74': {'26': {'25': {'33': {'24': {'31': {'62': {'13': {'52': {'15': {}}}, '14': {}}}}}, '57': {}, '73': {'37': {'15': {'62': {}}}, '41': {'33': {}}}}}}}}}}, '74': {}}}}}, '56': {}}, '75': {}}, '35': {'64': {'43': {'34': {'33': {'36': {'53': {'25': {}, '66': {}}, '56': {'25': {}}}}, '53': {'33': {}, '56': {'66': {'75': {'33': {'57': {}, '76': {}}}}}}}, '53': {'74': {'73': {'52': {'34': {'56': {}}, '66': {'56': {}}}, '56': {'34': {'52': {}, '62': {}}}}, '75': {'52': {'34': {'63': {}}}, '56': {'34': {}, '66': {}}}}}}, '47': {}, '53': {'34': {}, '36': {'43': {'63': {}, '66': {'56': {'47': {'57': {'37': {'26': {}, '34': {'63': {'26': {}, '48': {'38': {'28': {'52': {'26': {'58': {}}}, '58': {'68': {'67': {'78': {'52': {'25': {'32': {}, '33': {}}}}}}}}, '67': {}}}}, '68': {'26': {}, '48': {}, '75': {}}}, '48': {'38': {'67': {'63': {}}}}}, '63': {'34': {'37': {'26': {}}}, '48': {}}}, '73': {'34': {'24': {'23': {'25': {'14': {}, '15': {}}, '26': {'13': {}, '25': {}, '33': {'25': {'16': {'75': {'15': {'14': {'13': {'67': {}}}}}}}}}, '75': {'33': {'25': {'15': {'14': {'13': {'26': {'16': {'67': {}}}}}}, '52': {}}}}}, '33': {}, '52': {}}, '57': {'33': {'74': {}, '75': {}}}, '75': {'33': {'24': {'23': {'25': {'15': {'14': {'13': {'26': {'16': {'32': {}, '48': {}, '67': {'52': {}, '62': {}}}, '37': {}}}}}, '52': {'42': {}, '63': {}}}}, '42': {'52': {}}, '52': {'23': {'42': {}, '76': {'63': {'42': {}, '85': {}}}}, '25': {'42': {'37': {'23': {}, '26': {'32': {}, '58': {}}, '76': {}}, '67': {}}, '76': {'37': {}, '62': {}}}, '42': {}, '63': {'42': {}, '76': {}}}}, '67': {'42': {'57': {'62': {'38': {}, '51': {'63': {'38': {'74': {}, '83': {}}}}, '52': {}}}}, '76': {}}}}, '76': {'33': {}, '75': {}}}}, '74': {'34': {'24': {'23': {'26': {'13': {}, '25': {}, '33': {}}}, '52': {}, '73': {'75': {}, '76': {}}}, '75': {'33': {'67': {'42': {'31': {'52': {'25': {'73': {'63': {'84': {}, '86': {}}}}, '62': {'61': {}, '76': {}, '83': {}}}}, '57': {'62': {'38': {'63': {'37': {'48': {'52': {}, '58': {'73': {'52': {'61': {}, '84': {}}}}}}}}, '52': {'61': {'38': {'63': {'31': {}, '37': {}}}}, '63': {'31': {'61': {}, '73': {}, '83': {}}}}}}}}}}, '76': {'33': {}, '75': {'57': {'33': {}, '68': {}}}, '86': {}}}, '73': {'57': {}, '75': {'84': {}}, '76': {'63': {}, '75': {'57': {}, '85': {}}, '83': {'57': {}, '75': {}}}}}}}}, '75': {}}, '47': {'56': {}}, '56': {}, '63': {'33': {'43': {'34': {'23': {}, '24': {}}}}, '43': {'34': {'24': {}, '52': {}}}, '75': {'56': {'66': {'47': {'25': {}, '43': {}}}}}, '76': {'56': {}, '66': {}}}}, '43': {}}}}, '36': {}}, '64': {}, '66': {'56': {'64': {'33': {'34': {'43': {}, '75': {}}, '46': {'63': {'34': {'35': {'24': {'15': {'13': {'36': {'23': {'53': {}, '75': {}}, '25': {'16': {'26': {'74': {}}, '53': {}}}}}}, '36': {}}, '26': {'36': {'25': {'57': {}}}, '74': {'73': {}, '83': {}}}, '62': {}}}, '53': {'43': {'35': {}, '36': {}}}}}, '47': {'53': {'46': {'57': {'34': {}, '35': {'34': {}, '36': {}}}}}, '63': {'46': {'75': {'53': {}, '74': {'53': {'52': {}, '73': {'76': {}, '84': {}}, '76': {'57': {'73': {'67': {'34': {}, '68': {}}}}, '86': {}}, '85': {'57': {}, '76': {}}}, '76': {}}}}}}, '57': {'63': {'53': {'43': {'52': {'75': {'35': {}}}}}}}}, '43': {}, '53': {'35': {'34': {'43': {}, '57': {'25': {'52': {'62': {}, '63': {}}}, '74': {'63': {}, '73': {}}}}, '75': {}}, '46': {}}, '63': {'35': {'67': {}}}, '73': {'63': {}, '74': {}}, '74': {}, '75': {'46': {'57': {'74': {'63': {'85': {'53': {}, '86': {'87': {}}}}}, '76': {'35': {'34': {}}}}, '67': {}}, '57': {'47': {}, '53': {'46': {'43': {'74': {'76': {'63': {}, '85': {}}}}}, '63': {'43': {'33': {}, '35': {}, '52': {}}}, '74': {'43': {'35': {'76': {'63': {}, '85': {'86': {'87': {'84': {'83': {}}}}}}}, '36': {'46': {}, '76': {'63': {}, '85': {}}}}, '63': {}}, '76': {'43': {'35': {'46': {'34': {}, '63': {'74': {'84': {}}}}}, '63': {'74': {'84': {}}}}, '46': {'34': {'35': {'25': {}}, '43': {}, '67': {}}, '63': {'67': {}}}, '63': {}}}, '67': {'35': {'63': {'73': {'83': {'85': {}}}, '74': {}}}, '76': {}, '85': {'43': {'36': {'47': {'34': {'74': {'84': {'33': {}, '46': {}, '53': {}}}}}}}, '53': {'43': {'63': {}, '74': {'76': {'63': {}}, '84': {'63': {}, '73': {}}}}}, '74': {'76': {'53': {'43': {'63': {}}, '63': {}, '68': {}, '84': {}}}, '84': {}}}}}, '76': {'74': {'57': {'63': {}}}}}, '76': {'35': {'74': {'75': {'53': {}, '63': {'53': {'34': {}, '85': {}}}, '84': {'83': {'63': {'73': {'53': {}, '85': {'86': {'53': {}}}}, '85': {}}}, '86': {'53': {}, '63': {}}}}}}, '36': {'35': {}, '75': {}}, '46': {'53': {'43': {'74': {'63': {'73': {}}}, '75': {}}, '63': {'74': {'75': {'43': {'52': {'35': {}}}, '62': {}}}}}, '43': {'75': {}}, '74': {'67': {}}}}, '77': {}}}}}}
book = get_book()

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

def heuristic_map(board, player):
    map_value = [
        2000, 800, 700, 600, 500, 500, 600, 700, 800, 2000,
        800,  700, 300, 200, 200, 200, 200, 300, 700, 800,
        700,  300, 200, 100, 100, 100, 100, 200, 300, 700,
        600,  200, 100,  50,  50,  50,  50, 100, 200, 600,
        500,  200, 100,  50,  25,  25,  50, 100, 200, 500,
        500,  200, 100,  50,  25,  25,  50, 100, 200, 500,
        600,  200, 100,  50,  50,  50,  50, 100, 200, 600,
        700,  300, 200, 100, 100, 100, 100, 200, 300, 700,
        800,  700, 300, 200, 200, 200, 200, 300, 700, 800,
        2000, 800, 700, 600, 500, 500, 600, 700, 800, 2000
    ]

    boardArray = board.get_board()
    boardSize = board.get_board_size()
    count = 0

    for x in range(boardSize):
        for y in range(boardSize):
            if boardArray[x][y] is player:
                count += map_value[x][y]

    return count

def heuristic_angle(board, player, cst=50):
    boardSize = board.get_board_size()
    boardArray = board.get_board()

    score = board.getCurrentDomination(player) * 1000

    oponent = board._BLACK if player is board._WHITE else board._WHITE

    if (boardArray[0][0] == player):
        score += cst * 100

    elif (boardArray[0][0] == oponent):
        score -= cst * 100

    for i in range(1, boardSize - 1):
        if boardArray[i][0] == player:
            score += cst * 5

    for i in range(1, boardSize - 1):
        if boardArray[0][i] == player:
            score += cst * 5

    for i in range(1, boardSize - 1):
        if boardArray[i][0] == oponent:
            score -= cst * 5

    for i in range(1, boardSize - 1):
        if boardArray[0][i] == oponent:
            score -= cst * 5





    if (boardArray[0][boardSize - 1] == player):
        score += cst * 100

    elif (boardArray[0][boardSize - 1] == oponent):
        score -= cst * 100

    for i in range(boardSize - 2, -1):
        if boardArray[0][i] == player:
            score += cst * 5

    for i in range(1, boardSize - 1):
        if boardArray[i][boardSize - 1] == player:
            score += cst * 5

    for i in range(boardSize - 2, -1):
        if boardArray[0][i] == oponent:
            score -= cst * 5


    for i in range(1, boardSize - 1):
        if boardArray[i][boardSize - 1] == oponent:
            score -= cst * 5


    



    if (boardArray[boardSize - 1][boardSize - 1] == player):
        score += cst * 100

    elif (boardArray[boardSize - 1][boardSize - 1] == oponent):
        score -= cst * 100

    for i in range(boardSize - 2, -1):
        if boardArray[board - 1][i] == player:
            score += cst * 5


    for i in range(boardSize - 2, -1):
        if boardArray[i][board - 1] == player:
            score += cst * 5



    for i in range(boardSize - 2, -1):
        if boardArray[board - 1][i] == oponent:
            score -= cst * 5


    for i in range(boardSize - 2, -1):
        if boardArray[i][board - 1] == oponent:
            score -= cst * 5

        
    
    if (boardArray[boardSize - 1][0] == player):
        score += cst * 100

    elif (boardArray[boardSize - 1][0] == oponent):
        score -= cst * 100
    for i in range(boardSize - 2, -1):
        if boardArray[i][0] == player:
            score += cst * 5


    for i in range(1, boardSize - 1):
        if boardArray[boardSize - 1][i] == player:
            score += cst * 5



    for i in range(boardSize - 2, -1):
        if boardArray[i][0] == oponent:
            score -= cst * 5


    for i in range(1, boardSize - 1):
        if boardArray[boardSize - 1][i] == oponent:
            score -= cst * 5


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


def negAlphaBetaDepth(board, alpha, beta, depth, heuristic, player):
    if depth == 0 or board.is_game_over():
        return heuristic(board, player)

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

# Fetch a random good move from the opening book
def getBookMove(playedMoves):
    current = book


    while True:
        if len(playedMoves) == 0:
            break
        nextMove = playedMoves.pop(0)
        nextStr = str(nextMove[0]) + str(nextMove[1])

        if nextStr in current.keys():
            current = current[nextStr]
        else:
            return -1

        if not nextMove:
            break

    possible_moves = [i for i in current.keys()]

    if len(possible_moves) > 0:
        to_return = random.choice(possible_moves)
 
        return (int(to_return[0]), int(to_return[1]))
    else:
        return -1
        
