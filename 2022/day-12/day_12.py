import numpy as np
from queue import PriorityQueue

with open('day-12/sample.txt', encoding='utf-8') as file:
    data = [list(j) for j in [i for i in file.read().strip().split("\n")]]
# print(data)

grid = np.array(data)
int_grid = np.zeros((len(grid), len(grid[0])), dtype=int)

start = end = (0,0)
for ind_row, row in enumerate(grid):
    for ind_col, col in enumerate(row):
        if col == 'S':
            start = (ind_row, ind_col)
            int_grid[ind_row][ind_col] = ord('a') - 96
        elif col == 'E':
            end = (ind_row, ind_col)
            int_grid[ind_row][ind_col] = ord('z') - 96
        else:
            int_grid[ind_row][ind_col] = ord(col) - 96
# print(start, end)
# print(grid)
print(int_grid)
