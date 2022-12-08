with open('day-8/input.txt', encoding='utf-8') as file:
    data = [j.split() for j in [i for i in file.read().strip().split("\n")]]
# print(data)


grid = []
for row in data:
  grid.append([int(x) for x in row[0]])
# print(grid)

# Check along the current row, from pos to left edge
def CheckToLeft(row, col):
    for i in range(0, col):
        if grid[row][i] >= grid[row][col]:
            return False
    return True

# Check along the current row, from pos to right edge
def checkToRight(row, col):
    for i in range(col+1, len(grid[0])):
        if grid[row][i] >= grid[row][col]:
            return False
    return True

# Check along the current col, from pos to top edge
def checkToTop(row, col):
    for i in range(0,row):
        if grid[i][col] >= grid[row][col]:
            return False
    return True

# Check along the current row, from pos to bottom edge
def checkToBottom(row, col):
    for i in range(row+1,len(grid)):
        if grid[i][col] >= grid[row][col]:
            return False
    return True

# Include outer edges at the start
visible = 2*(len(grid)+len(grid[0])-2)
for row in range(1, len(grid)-1):
  for col in range(1, len(grid[0])-1):
    if CheckToLeft(row, col) or checkToRight(row, col) or checkToTop(row, col) or checkToBottom(row, col):
      visible += 1

print('Part 1', visible)

# Part 2
# Count along the current row, from pos to left edge
def countToLeft(row, col):
  total = 0
  for i in range(col-1, -1, -1):
    if grid[row][i] < grid[row][col]:
      total += 1
    else:
      return total+1
  return total

# Count along the current row, from pos to right edge
def countToRight(row, col):
  total = 0
  for i in range(col+1, len(grid[0])):
    if grid[row][i] < grid[row][col]:
      total += 1
    else:
      return total+1
  return total

# Count along the current col, from pos to top edge
def countToTop(row, col):
  total = 0
  for i in range(row-1, -1, -1):
    if grid[i][col] < grid[row][col]:
      total += 1
    else:
      return total+1
  return total

# Count along the current col, from pos to bottom edge
def countToBottom(row, col):
  total = 0
  for i in range(row+1,len(grid)):
    if grid[i][col] < grid[row][col]:
      total += 1
    else:
      return total+1
  return total

maximum = 0
for row in range(1, len(grid)-1):
    for col in range(1, len(grid[0])-1):
        maximum = max(maximum, countToLeft(row, col) * countToRight(row, col) * countToTop(row, col) * countToBottom(row, col))
print('Part 2', maximum)
