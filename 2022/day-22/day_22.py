import re

# Score dictionary for the end
# ROW * 1000 + COL * 4 + direction_score == Result
# '>': 0, 'v': 1, '<': 2, '^': 3

# Setup the input
with open('day-22/input.txt', encoding='utf-8') as file:
    maps, moves = [i for i in file.read().split("\n\n")]
    moves =  [i for i in re.split('(\d+)([A-Z]+)', moves.strip()) if i != '']
    maps = maps.split('\n')

# Set variables, for max rows and cols
MAX_COLS = max(map(len, maps))
MAX_ROWS = len(maps)
RIGHT, DOWN, LEFT, UP = range(4) # right = 0, down = 1, left = 2, up = 3
POSITION = [0, maps[0].index('.'), 0]
P_ROW = 0
P_COL = maps[0].index('.')
P_DIR = 0
dir_map = [
    (0, 1), # RIGHT
    (1, 0), # DOWN
    (0, -1), # LEFT
    (-1, 0) # UP
]

# Setup the grid of the map, adjusting the length's to being equal
grid = []
for row in maps:
    if len(row) < MAX_COLS:
        for _ in range(MAX_COLS - len(row)):
            row += ' '
    grid.append(row)

# First column from the left with . or #
def first_col_left(row):
    for col in range(MAX_COLS):
        if grid[row][col] != ' ' :
            return col

# First column from the right with . or #
def first_col_right(row):
    for col in range(MAX_COLS -1, -1, -1):
        if grid[row][col] != ' ':
            return col

# First row from the top with . or #
def first_row_top(col):
    for row in range(MAX_ROWS):
        if grid[row][col] != ' ':
            return row

# First row from the bottom with . or #
def first_row_bottom(col):
    for row in range(MAX_ROWS -1, -1, -1):
        if grid[row][col] != ' ':
            return row

for ind, move in enumerate(moves):
    if ind % 2 == 0:
        move = int(move)
        mv_row, mv_col = dir_map[P_DIR]

        for i in range(move):
            # Add on the direction to simulate the first step
            new_row = P_ROW + mv_row
            new_col = P_COL + mv_col

            # If new_row or new_col are greater than respective MAX's, find first from top or left
            if new_row >= MAX_ROWS:
                new_row = first_row_top(new_col)
            if  new_col >= MAX_COLS:
                new_col = first_col_left(new_row)

            # If an empty space, get first from top/bottom/left/right
            if grid[new_row][new_col] == ' ':
                if P_DIR == RIGHT:
                    new_col = first_col_left(new_row)
                elif P_DIR == LEFT:
                    new_col = first_col_right(new_row)
                elif P_DIR == DOWN:
                    new_row = first_row_top(new_col)
                elif P_DIR == UP:
                    new_row = first_row_bottom(new_col)

            # If a wall break the loop
            if grid[new_row][new_col] == '#':
                break

            # Reset the current position
            P_ROW = new_row
            P_COL = new_col

    else:
        # Change the direction
        if move == 'R':
            P_DIR = (P_DIR + 1) % 4
        else:
            P_DIR = (P_DIR - 1) % 4

# Add one to row and col and both start at 1,1 however I used index 0,0 throughout
end_row, end_col = P_ROW + 1, P_COL + 1
part1 = end_row * 1000 + end_col * 4 + P_DIR
print('Part 1:', part1)
