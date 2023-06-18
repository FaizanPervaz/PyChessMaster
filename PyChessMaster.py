#20I0565 E Faizan
import math
import random
import chess

board = chess.Board()


def check():
    if board.is_checkmate() is True:
        return True
    else:
        return False


def stale():
    if board.is_stalemate() is True:
        return True
    else:
        return False


def draw1():
    if board.is_fivefold_repetition() is True:
        return True
    else:
        return False


def draw2():
    if board.is_seventyfive_moves() is True:
        return True
    else:
        return False


def GameOver():
    if board.is_game_over() is True:
        return True
    else:
        return False


def printBoard(board):
    print("   a b c d e f g h")
    print("  ----------------")
    rows = str(board).split("\n")
    for i, row in enumerate(rows):
        print(f"{8 - i}| {row} |{8 - i}")
    print("  ----------------")
    print("   a b c d e f g h\n")


def playerMove():
    while True:
        position = input("Input your Move: ")
        try:
            move = chess.Move.from_uci(position)
            if move in board.legal_moves:
                board.push(move)
                break
            else:
                print("Cannot Move this Piece")
        except ValueError:
            print("Please Input a Valid Chess Piece")
    return


def aiMove():
    best_score = -math.inf
    best_move = None

    allowed_moves = list(board.legal_moves)

    for move in board.legal_moves:
        if len(allowed_moves) > 0:
            move = random.choice(allowed_moves)
            board.push(move)
        score = minimax(board, 0, False)
        board.pop()
        if score > best_score:
            best_score = score
            best_move = move

    if best_move is not None:
        board.push(best_move)
    return


def minimax(board, depth, isMaximizing):
    if depth == 0 or GameOver():
        return evaluate(board)

    #our bot
    if isMaximizing:
        best_score = -math.inf

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, False)
            board.pop()
            best_score = max(score, best_score)
        return best_score

    #enemy bot
    else:
        best_score = math.inf

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, True)
            board.pop()
            best_score = min(score, best_score)
        return best_score


def evaluate(board):
    if check():
        if board.turn:
            print("Checkmate")
            return -1
        else:
            print("Checkmate")
            return 1
    elif stale() or draw1() or draw2():
        # draw
        print("Draw")
        return 0
    else:
        chessman = {
            chess.KING: 0,
            chess.QUEEN: 9,
            chess.ROOK: 5,
            chess.BISHOP: 3,
            chess.KNIGHT: 3,
            chess.PAWN: 1
        }
        score = 0
        for i in chess.SQUARES:
            chess_piece = board.piece_at(i)
            if chess_piece is not None:
                if chess_piece.color:
                    score -= chessman[chess_piece.piece_type]
                else:
                    score += chessman[chess_piece.piece_type]
        return score


print("\t Welcome To ")
print("\t\tChess ")
printBoard(board)
while not GameOver():
    legal = board.legal_moves
    playerMove()
    printBoard(board)
    if GameOver():
        break
    aiMove()
    printBoard(board)

print('Game Over')
