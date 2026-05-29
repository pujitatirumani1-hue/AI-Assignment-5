import math

def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]

    for a, c, d in wins:
        if b[a] == b[c] == b[d] != '_':
            return b[a]

    return 'draw' if '_' not in b else None


def minimax(board, is_max):
    result = winner(board)

    if result == 'X': return 1
    if result == 'O': return -1
    if result == 'draw': return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == '_':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = '_'
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == '_':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = '_'
        return best


board = []
print("Enter the board (3 rows):")
for _ in range(3):
    board.extend(input().split())

turn = input("Whose turn? (X/O): ").upper()

score = minimax(board, turn == 'X')
print("Minimax Score =", score)
