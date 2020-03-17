from copy import deepcopy
from queue import Queue

de_board = [
    ["S", " ", " ", "#", " ", " ", "E"],
    [" ", " ", " ", "#", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", "#", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", "#", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
]

def printBoard(board):
    for row in board:
        for let in row:
            print(let+" ", end="")
        print()

def getStart(board):
    for row_index, row in enumerate(board):
        for let_index, let in enumerate(row):
            if let == "S":
                return (let_index, row_index)

def getEnd(board):
    for row_index, row in enumerate(board):
        for let_index, let in enumerate(row):
            if let == "E":
                return (let_index, row_index)

def followMoves(board, start, end, moves, getPos=False):
    pos = list(start)
    for move in moves:
        if move == "U":
            pos[1] = pos[1] - 1
        elif move == "D":
            pos[1] = pos[1] + 1
        elif move == "R":
            pos[0] = pos[0] + 1
        elif move == "L":
            pos[0] = pos[0] - 1
    if getPos:
        return pos
    for x in (1, -1):
        try:
            if board[pos[1]][pos[0] + x] == "E" and pos[0] + x >= 0:
                return True
        except:
            pass
        try:
            if board[pos[1]+x][pos[0]] == "E" and pos[1]+x >= 0:
                return True
        except:
            pass


    return False

def getMoves(board, x, y):
    nodes = []
    try:
        if board[y][x + 1] == " " and x + 1 >= 0:
            nodes.append("R")
    except:
        pass
    try:
        if board[y + 1][x] == " " and y + 1 >= 0:
            nodes.append("D")
    except:
        pass
    try:
        if board[y][x-1] == " " and x - 1 >= 0:
            nodes.append("L")
    except:
        pass
    try:
        if board[y-1][x] == " " and y-1 >= 0:
            nodes.append("U")
    except:
        pass
    return nodes

board = deepcopy(de_board)
start = getStart(board)
end = getEnd(board)
printBoard(board)
pos = Queue()
moves = getMoves(board, start[0], start[1])
for move in moves:
    pos.put(move)
run = True
while run:
    move = pos.get()
    move_pos = followMoves(board, start, end, move, getPos=True)
    moves = getMoves(board, *move_pos)
    run = not(followMoves(board, start, end, move))
    for m in moves:
        pos.put(move+m)

x = list(start)
for m in move:
    if m == "U":
        x[1] = x[1] - 1
    elif m == "D":
        x[1] = x[1] + 1
    elif m == "R":
        x[0] = x[0] + 1
    elif m == "L":
        x[0] = x[0] - 1
    board[x[1]][x[0]] = "+"

print()
printBoard(board)