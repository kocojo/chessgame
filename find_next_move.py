from chess_engine import info
import tree_save_posible_move
import random
import copy
points = {"p":1,"R":5,"N":3,"Q":10,"B":3,"K":100}
knight_scores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                 [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                 [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                 [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                 [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

bishop_scores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

queen_scores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

pawn_scores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
               [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
               [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

piece_position_scores = {"wN": knight_scores,
                         "bN": knight_scores[::-1],
                         "wB": bishop_scores,
                         "bB": bishop_scores[::-1],
                         "wQ": queen_scores,
                         "bQ": queen_scores[::-1],
                         "wR": rook_scores,
                         "bR": rook_scores[::-1],
                         "wp": pawn_scores,
                         "bp": pawn_scores[::-1]}
CHECKMATE_POINT = 1000
DEFTH = 2
kkk =0
kk=0
nextMove =()
def find_random_move(gs:info):
    a = gs.get_all_posible_move()
    b = random.choice(a)
    gs.change_Pieces(b)
def calculator_point(gs:info):
    score = 0
    if not gs.is_checkmate():
        for i in range(8):
            for j in range(8):
                piece = gs.board[i][j]
                if piece != "--":
                    piece_position_score = 0
                    if piece[1] != "K":
                        piece_position_score = piece_position_scores[piece][i][j]
                    if piece[0] == "w":
                        score += points[piece[1]] + piece_position_score
                    if piece[0] == "b":
                        score -= points[piece[1]] + piece_position_score
    elif gs.is_stalemate():
        score = 0
    elif gs.whiteToMove:
        score = -CHECKMATE_POINT
    else:
        score = CHECKMATE_POINT
    return score
def findBestMove(game_state, valid_moves):
    global nextMove
    nextMove = None
    random.shuffle(valid_moves)
    a = findmoveNegaMaxAlphaBeta(game_state, valid_moves, DEFTH, -CHECKMATE_POINT, CHECKMATE_POINT,1 if game_state.whiteToMove else -1)
    if nextMove == None:
        nextMove = find_random_move(game_state)
    print(nextMove)
    return nextMove
def findmoveNegaMaxAlphaBeta(gs,validMoves,depth,alpha,beta,turnMultiplier):
    global nextMove
    if depth == 0:
        return turnMultiplier*calculator_point(gs)
    else:
        maxScore = -CHECKMATE_POINT
        for move in validMoves:
                gs.change_Pieces(move)
                nextMoves = gs.get_all_posible_move()
                score = -findmoveNegaMaxAlphaBeta(gs,nextMoves,depth-1,-beta,-alpha,-turnMultiplier)
                if score > maxScore:
                    maxScore = score
                    if depth == DEFTH:
                        nextMove = move
                gs.undo()
                if maxScore>alpha:
                    alpha = maxScore
                if alpha >=beta:
                    break
    return maxScore
def make_tree(tree:tree_save_posible_move.tree,gs:info,move):
    if tree.goc == None:
        a=gs.get_all_posible_move()
        tree.goc = tree_save_posible_move.note(None,[],gs)
        for i in a:
            gs.change_Pieces(i)
            gs1 = copy.copy(gs)
            node = tree_save_posible_move.note(i,[],gs1)
            node.parent = tree.goc
            tree.goc.next.append(node)
            make_tree_child(node,defth=1)
            tree.goc.point = max(tree.goc.point,node.point)
            gs.undo()
    else:
        for i in tree.goc.next:
            if i.data == move:
                tree.goc = i
                tree.goc.parent = None
                tree.goc.point = -11000
                break
        b = tree.leaf(tree.goc)
        c = set()
        for i in b:
            i.point = -1100
            make_tree_child(i,DEFTH-1)
            c.add(i.parent)
        cal(c)
    random.shuffle(tree.goc.next)
    for i in tree.goc.next:
        if i.point == tree.goc.point:
            i.data
            return i.data
            break
def make_tree_child(node,defth):
    global kkk
    if defth == DEFTH:
        node.point = calculator_point(node.board)
        kkk = 1
    else:
        a = node.board.get_all_posible_move()
        for i in a:
            node.board.change_Pieces(i)
            araara = copy.copy(node.board)
            n = tree_save_posible_move.note(i,[],araara)
            n.parent = node
            node.next.append(n)
            make_tree_child(n,defth+1)
            node.point = max(node.point,n.point*kkk)
            node.board.undo()

def calculator(node:tree_save_posible_move.note):
    node.point = -1100
    for i in node.next:
        node.point = max(node.point,i.point)
def cal(list_of_parent):
    c= set()
    if len(list_of_parent) !=0:
        for i in list_of_parent:
          if i != None:
            c.add(i.parent)

            calculator(i)
        cal(c)
a = info()
b = tree_save_posible_move.tree()




