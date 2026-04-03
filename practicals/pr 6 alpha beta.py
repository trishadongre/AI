import math

board = [' ' for _ in range(9)]

def show():
    print()
    for i in range(3):
        print(board[i*3], '|', board[i*3+1], '|', board[i*3+2])
        if i < 2:
            print("---------")
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)

def draw():
    return ' ' not in board

def minimax(maxp, a, b):
    if win('O'): return 1
    if win('X'): return -1
    if draw(): return 0

    if maxp:
        best = -math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                val = minimax(False, a, b)
                board[i]=' '
                best = max(best, val)
                a = max(a, best)
                if b <= a: break
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                val = minimax(True, a, b)
                board[i]=' '
                best = min(best, val)
                b = min(b, best)
                if b <= a: break
        return best

def ai():
    best = -math.inf
    move = 0
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            val = minimax(False, -math.inf, math.inf)
            board[i]=' '
            if val > best:
                best = val
                move = i
    board[move]='O'

print("Tic Tac Toe (You = X, AI = O)")
show()

while True:
    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] != ' ':
        print("Invalid move")
        continue

    board[pos] = 'X'
    show()

    if win('X'):
        print("You Win ")
        break
    if draw():
        print("Draw ")
        break

    ai()
    print("AI Move:")
    show()

    if win('O'):
        print("AI Wins 💻")
        break
    if draw():
        print("Draw ")
        break
