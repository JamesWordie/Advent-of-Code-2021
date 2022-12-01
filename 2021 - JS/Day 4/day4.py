import numpy as np

data = open('Day 4/input.txt', encoding='utf-8').read().splitlines()
drawn = [int(x) for x in data[0].split(',')]

boards_count = (len(data) - 1) // 6
boards = []
for i in range(boards_count):
    board = [(list(int(x) for x in data[i*6+j+2].split())) for j in range(5)]
    boards.append(np.array(board))

def is_win(board):
    return np.any(np.sum(board, axis=1) == -board.shape[0]) or np.any(np.sum(board, axis=0) == -board.shape[1])


def score(board):
    return np.sum(board[board != -1])


for d in drawn:
    for i, b in enumerate(boards):
        X, Y = b.shape
        for x in range(X):
            for y in range(Y):
                if b[x, y] == d:
                    b[x, y] = -1
                    if is_win(b):
                        print("board", i, "win", "score", score(b))
                        print("solution", score(b) * d)
                        exit()

# board 63 win score 539
# solution 41503
