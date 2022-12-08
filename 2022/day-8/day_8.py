with open('day-8/sample.txt', encoding='utf-8') as file:
    data = [j.split() for j in [i for i in file.read().strip().split("\n")]]
# print(data)


grid = []
for row in data:
  grid.append([int(x) for x in row[0]])
# print(grid)

# Check along the current row, from pos to left edge
def leftCheck(row, col):
    for i in range(0, col):
        if grid[row][i] >= grid[row][col]:
            return False
    return True

# Check along the current row, from pos to right edge
def rightCheck(row, col):
    for i in range(col+1, len(grid[0])):
        if grid[row][i] >= grid[row][col]:
            return False
    return True

# Check along the current col, from pos to top edge
def upCheck(row, col):
    for i in range(0,row):
        if grid[i][col] >= grid[row][col]:
            return False
    return True

# Check along the current row, from pos to bottom edge
def downCheck(row, col):
    for i in range(row+1,len(grid)):
        if grid[i][col] >= grid[row][col]:
            return False
    return True

# Include outer edges at the start
visible = 2*(len(grid)+len(grid[0])-2)
for row in range(1, len(grid)-1):
  for col in range(1, len(grid[0])-1):
    if leftCheck(row, col) or rightCheck(row, col) or upCheck(row, col) or downCheck(row, col):
      visible += 1

print('Part 1', visible)
