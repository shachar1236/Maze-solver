from copy import deepcopy
import math

class Node():
    def __init__(self, x, y, g, h):
        self.visited = False
        self.parent = None
        self.g = g
        self.h = h
        self.f = g + h
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Node(({self.x}, {self.y}), ({self.g}, {self.h}, {self.f}), {self.visited})"

    def __eq__(self, other):
        if isinstance(other, Node) and self.x == other.x and other.y == self.y:
            return True
        return False

    def __hash__(self):
        return 0

    def update(self, g=None, h=None):
        if not g:
            g = self.g
        if not h:
            h = self.h
        self.g = g
        self.h = h
        self.f = h + g

de_board = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", " ", "#"],
    ["#", " ", "#", " ", " ", "#"],
    ["#", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "E", "#"],
    ["#", "#", "#", "#", "#", "#"],
]

def getDistance(x1, x2, y1, y2):
    dy = abs(y1-y2) ** 2
    dx = abs(x1-x2) ** 2
    return round(10*math.sqrt(dx+dy))


def printBoard(board):
    for row in board:
        for let in row:
            print(let+" ", end="")
        print()

def getStartEnd(board):
    for row_index, row in enumerate(board):
        for let_index, let in enumerate(row):
            if let == "S":
                s = Node(let_index, row_index, 0, 0)
            elif let == "E":
                e = Node(let_index, row_index, 0, 0)
    d = getDistance(s.x, e.x, s.y, e.y)
    s.update(h=d)
    e.update(g=d)
    return (s, e)

def getNodes(board,x, y, s, e):
    nodes = []
    for move in (-1, 1):
        try:
            if board[y][x + move] == " " and x + move > 0:
                nodes.append(Node(x+move, y, getDistance(s.x, x+move, s.y, y), getDistance(e.x, x+move, e.y, y)))
        except:
            pass
        try:
            if board[y + move][x] == " " and y + move > 0:
                nodes.append(Node(x, y+move, getDistance(s.x, x, s.y, y+move), getDistance(e.x, x, e.y, y+move)))
        except:
            pass
        try:
            if board[y+move][x+move] == " " and y + move > 0 and x + move > 0:
                nodes.append(Node(x+move, y+move, getDistance(s.x, x+move, s.y, y+move), getDistance(e.x, x+move, e.y, y+move)))
        except:
            pass
        try:
            if board[y-move][x+move] == " " and y-move > 0 and x+move > 0:
                nodes.append(Node(x-move, y+move, getDistance(s.x, x+move, s.y, y-move), getDistance(e.x, x+move, e.y, y-move)))
        except:
            pass
    return nodes

board = deepcopy(de_board)
start, end = getStartEnd(board)
nodes = getNodes(board, start.x, start.y, start, end)
end_i = len(nodes)-1
printBoard(board)

lastNode = None
run = True
while run:
    m = Node(0,0,float("inf"), float("inf"))
    fs = []
    m_i = 0
    for node_index ,node in enumerate(nodes):
        if m.f > node.f and not node.visited:
            m = node
            m_i = node_index
        fs.append(node.f)
    fs.pop(m_i)
    f = m.f
    if m.f in fs:
        for node_index ,node in enumerate(nodes):
            if m.h > node.h and not node.visited and node.f == f:
                m = node
                m_i = node_index
    nodes[m_i].visited = True
    nodes[m_i].parent = lastNode
    board[m.y][m.x] = "+"
    nodes += getNodes(board, m.x, m.y, start, end)
    print()
    printBoard(board)
    nodes = list(set(nodes))
    lastNode = m


run = True
for node in nodes:
    print()
    printBoard(board)
    if node.visited:
        board[node.y][node.x] = "+"


print()
print()
printBoard(board)
