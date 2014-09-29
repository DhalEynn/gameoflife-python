from collections import namedtuple, defaultdict

Cell = namedtuple('Cell', ['x', 'y'])


def getNeighbours(cell):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                yield Cell(x, y)


def getNeighbourCount(board):
    neighbour_counts = defaultdict(int)
    for cell in board:
        for neighbour in getNeighbours(cell):
            neighbour_counts[neighbour] += 1
    return neighbour_counts


def advanceBoard(board):
    for cell, count in getNeighbourCount(board).iteritems():
        if count == 3 or (cell in board and count == 2):
            yield cell


def generateBoard(desc):
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == 'X':
                yield Cell(int(col), int(row))


def boardToString(board):
    if not board:
        return
    board_str = ""
    xs = [x for (x, y) in board]
    ys = [y for (x, y) in board]
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            board_str += 'X' if Cell(x, y) in board else '.'
        board_str += '\n'
    return board_str.strip()