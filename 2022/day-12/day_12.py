import numpy as np
from collections import deque

with open('day-12/input.txt', encoding='utf-8') as file:
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
            int_grid[ind_row][ind_col] = ord('z') - 96 + 1
        else:
            int_grid[ind_row][ind_col] = ord(col) - 96
# print(start, end)
# print(grid)
# print(int_grid)

def get_neighbours(height_arr, curr_x, curr_y, part_2=False):
    # current height
    curr_height = height_arr[curr_x][curr_y]
    
    all_neighbours = [
        (curr_x, curr_y + 1),
        (curr_x, curr_y - 1),
        (curr_x + 1, curr_y),
        (curr_x - 1, curr_y)
    ]
    if part_2:
        valid_neighbours = [
            ngbr for ngbr in all_neighbours
            if 0 <= ngbr[0] < len(height_arr)
            and 0 <= ngbr[1] < len(height_arr[0])
            and curr_height - height_arr[ngbr[0]][ngbr[1]] <= 1               
        ]
    else:
        valid_neighbours = [
            ngbr for ngbr in all_neighbours
            if 0 <= ngbr[0] < len(height_arr)
            and 0 <= ngbr[1] < len(height_arr[0])
            and height_arr[ngbr[0]][ngbr[1]] - curr_height <= 1               
        ]
    return valid_neighbours

def bfs(height_arr, start_pos, end_pos_val, part_2=False):
    start = {'curr': start_pos, 'cost': 0}
    
    edges = deque()
    visited = set()
    edges.append(start)
    
    while edges:
        # Unpack the next node
        node = edges.popleft()
        
        if node.get('curr') in visited:
            continue
        # Add state to the visited
        visited.add(node.get('curr'))
        
        # Return the cost if reached the end position
        curr_x, curr_y = node.get('curr')
        # if (curr_x, curr_y) == end_pos_val:
        if height_arr[curr_x][curr_y] == end_pos_val:
            return node.get('cost')
        
        # Add neighbours to the edges
        neighbours = get_neighbours(height_arr, curr_x, curr_y, part_2)
        for ngbr_state in neighbours:
            ngbr_node = {'curr': ngbr_state, 'cost': node.get('cost') + 1}
            edges.append(ngbr_node)
            
    # Return infinity if no path is found
    return float('inf')

# end_pos_val --> the value associated to the end position --> see line 19
print('Part 1', bfs(int_grid, start, end_pos_val=27))

# end_pos_val --> the value associated to the letter 'a' --> see line 21
print('Part 2', bfs(int_grid, start_pos=end, end_pos_val=1, part_2=True))
