from copy import deepcopy

class Corner():
    def __init__(self, x, y, distance=float("inf")):
        self.visited = False
        self.parent = None
        self.distance = distance
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Corner(({self.x}, {self.y}), {self.distance}, {self.visited})"

    def __eq__(self, other):
        if isinstance(other, Corner) and self.x == other.x and other.y == self.y:
            return True
        return False

# 1, 1
# 4, 4
de_board = [
    ["#", "#", "#", "#", "#", "#"],
    [" ", "S", " ", " ", " ", "#"],
    [" ", "#", "#", " ", "#", "#"],
    [" ", " ", " ", "#", " ", "#"],
    [" ", "#", " ", " ", " ", "#"],
    ["#", "#", "E", "#", "#", "#"],
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

def isCorner(board, x, y):
    side = False
    up_down = False
    for move in (-1, 1):
        try:
            if board[y][x + move] in (" ", "S", "E") and not(board[y][x] in ("#", "S", "E")):
                side = True
                if board[y + move][x] in ("S", "E"):
                    up_down = True
        except:
            pass
        try:
            if board[y + move][x] in (" ", "S", "E") and not(board[y][x] in ("#", "S", "E")):
                up_down = True
                if board[y + move][x] in ("S", "E"):
                    side = True
        except:
            pass
    return side and up_down

def getCorners(board):
    corners = []
    for y, row in enumerate(board):
        for x, _ in enumerate(row):
            if isCorner(board, x, y):
                corners.append(Corner(x, y))
    return corners

board = deepcopy(de_board)
start = Corner(*getStart(board), distance=0)
end = Corner(*getEnd(board))
printBoard(board)
corners = [start]+getCorners(board)
corners.append(end)

for index, corner in enumerate(corners):
    if corner.x == start.x:
        corners[index].distance = abs(start.y-corner.y)
        corners[index].parent = start
    elif corner.y == start.y:
        corners[index].distance = abs(start.x-corner.x)
        corners[index].parent = start

corners[0].visited = True


run = True
while run:
    all = True
    for main_index, main_corner in enumerate(corners):
        if not main_corner.visited:
            all = False
        if not(main_corner.parent is None) and not main_corner.visited:
            for index, corner in enumerate(corners):
                if corner.x == main_corner.x and main_corner.distance + abs(main_corner.y-corner.y) < corner.distance:
                    can = True
                    for x in range(min(main_corner.y, corner.y), max(main_corner.y, corner.y)):
                        if board[x][corner.x] == "#":
                            can = False
                    if can:
                        corners[index].distance = main_corner.distance + abs(main_corner.y-corner.y)
                        corners[index].parent = main_corner
                elif corner.y == main_corner.y and main_corner.distance + abs(main_corner.x-corner.x) < corner.distance:
                    can = True
                    for x in range(min(main_corner.x, corner.x),max(main_corner.x, corner.x)):
                        if board[corner.y][x] == "#":
                            can = False
                    if can:
                        corners[index].distance = main_corner.distance + abs(main_corner.x-corner.x)
                        corners[index].parent = main_corner
            corners[main_index].visited = True
                
            break
    if all:
        run = False
        break

run = True
corner = corners[-1]
while run:
    if corner.x == corner.parent.x:
        for x in range(min(corner.parent.y, corner.y+1), max(corner.parent.y, corner.y+1)):
            board[x][corner.x] = "+"
    if corner.y == corner.parent.y:
        for x in range(min(corner.x, corner.parent.x+1), max(corner.x, corner.parent.x+1)):
            board[corner.y][x] = "+"
    corner = corner.parent
    if corner.parent == corner:
        run = False
        break

print()
print()
printBoard(board)
