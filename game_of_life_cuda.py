from collections import namedtuple, defaultdict
import time
import os
CLEAR = 'cls' if os.name == 'nt' else 'clear'
MAX_ITERATION = 150
# If you want a random board, here are the parameters
RANDOM_BOARD = False
SEED = None
RAND_LINES = 3
RAND_COLUMNS = 8
X_DRAW = 0.8

Cell = namedtuple("Cell", ["x", "y"])


def getNeighbors(cell):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                yield Cell(x, y)


def getNeighborCount(board):
    neighbor_counts = defaultdict(int)
    for cell in board:
        for neighbor in getNeighbors(cell):
            neighbor_counts[neighbor] += 1
    return neighbor_counts


def advanceBoard(board):
    new_board = set()
    for cell, count in getNeighborCount(board).items():
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)
    return new_board


def generateRandomBoard():
    global SEED, RAND_COLUMNS, RAND_LINES, X_DRAW
    import random
    random.seed(a=SEED)
    result = ""

    if (RAND_LINES <= 0):
        RAND_LINES = 3
    if (RAND_COLUMNS <= 0):
        RAND_COLUMNS = 8
    if (X_DRAW <= 0.0):
        X_DRAW = random.random()

    for _ in range(RAND_LINES):
        for _ in range(RAND_COLUMNS):
            result += "X" if random.random() < X_DRAW else "."
        result += '\n'
    return result


def generateBoard(desc):
    global RANDOM_BOARD
    if (RANDOM_BOARD):
        desc = generateRandomBoard()
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == "X":
                board.add(Cell(int(col), int(row)))
    return board


def boardToString(board, pad=0):
    if not board:
        return "empty"
    board_str = ""
    xs = [x for (x, _) in board]
    ys = [y for (_, y) in board]
    for y in range(min(ys) - pad, max(ys) + 1 + pad):
        for x in range(min(xs) - pad, max(xs) + 1 + pad):
            board_str += "X" if Cell(x, y) in board else "."
        board_str += "\n"
    return board_str.strip()


if __name__ == "__main__":
    f = generateBoard("......X.\nXX......\n.X...XXX")
    i = 1
    board = "start"
    while (i < MAX_ITERATION and board != "empty"):
        f = advanceBoard(f)        
        board = boardToString(f, 2)
        os.system(CLEAR)
        # f is the board, the second parameter is the size of the window
        print(f"Generation {i} :\n" + boardToString(f, 2))
        i += 1
        time.sleep(0.1)
    if (board != "empty"):
        print(f"Max iteration {MAX_ITERATION} was reached.")
