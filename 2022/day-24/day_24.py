with open('day-24/input.txt', encoding='utf-8') as file:
    grid = [list(i) for i in file.read().strip().split("\n")]
# print(grid)

# Blizzard Class
class Blizzard:
    def __init__(self, row: int, col: int, direction: str):
        self.row = row
        self.col = col
        self.direction = direction

    # Return current position as a tuple
    def get_location(self):
        return (self.row, self.col)

    # Move the current blizzard
    def move(self):
        n_row, n_col = DIRS[self.direction]
        tmp_row = self.row + n_row
        tmp_col = self.col + n_col

        # If first row or last row, reset to wrap around the walls
        if tmp_row == 0:
            tmp_row = HEIGHT - 2
        elif tmp_row == HEIGHT - 1:
            tmp_row = 1

        # If first col or last col, reset to wrap around the walls
        if tmp_col == 0:
            tmp_col = WIDTH - 2
        elif tmp_col == WIDTH - 1:
            tmp_col = 1

        # Set the new row and col
        self.row = tmp_row
        self.col = tmp_col

class BlizzardMaze:
    def __init__(self, blizzards_list, start, end):
        self.blizzards = blizzards_list
        self.blizzard_locations = None
        self.get_locations()

        self.start = start
        self.end = end
        self.points = [start]

    # Set the current locations of the blizzard
    def get_locations(self):
        curr_locations = set()
        for blizzard in self.blizzards:
            curr_locations.add(blizzard.get_location())

        self.blizzard_locations = curr_locations

    # Move each of the blizzard instances to their next position
    def move_blizzard(self):
        for blizzard in self.blizzards:
            blizzard.move()

        # Set the new locations of the blizzards
        self.get_locations()

    # Get boundaries
    def boundaries(self, coords):
        x = coords[0]
        y = coords[1]

        if (x,y) == self.end:
            return True

        return x >= 1 and x < HEIGHT - 1 and y > 0 and y < WIDTH - 1

    # Calculate and return the manhatten distance
    def manhatten_dist(self, first, second):
        return sum(abs(v1 - v2) for v1,v2 in zip(first, second))

    def check_points(self, c_point: tuple):
        n_points = set()

        for direction in DIRS.values():
            x,y = direction
            point_x, point_y = c_point

            check_point = (point_x + x, point_y + y)
            if self.boundaries(check_point) and check_point not in self.blizzard_locations:
                n_points.add(check_point)

        return n_points

    # Solve using algo
    def solve(self):
        timer = 0

        while self.end not in self.points:
            self.move_blizzard()

            new_points = set()
            for point in self.points:
                # Stay still
                if point not in self.blizzard_locations and point != self.start:
                    new_points.add(point)

                # Check directions - up/down/left/right
                new_points.update(self.check_points(point))

            # No paths therefore restart
            if len(new_points) == 0:
                new_points.add(self.start)

            # Set the points for this round
            self.points = new_points

            timer += 1

        return timer

# Constants & variable
blizzards = []
HEIGHT = len(grid)
WIDTH = len(grid[0])
START =  (0, grid[0].index('.'))
END = (HEIGHT-1, grid[HEIGHT-1].index('.'))
DIRS = {
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0)
}

# Add the blizzard locations to the list
for x, row in enumerate(grid):
    for y, col in enumerate(row):
        if col in DIRS.keys():
            blizzards.append(Blizzard(x, y, col))

# Part 1 Solve
maze = BlizzardMaze(blizzards, START, END)
time = maze.solve()
print('Part 1:', time)

# Part 2 Solve
maze_2 = BlizzardMaze(blizzards, END, START)
time_2 = maze_2.solve()
maze_3 = BlizzardMaze(blizzards, START, END)
time_3 = maze_3.solve()
total = time + time_2 + time_3
print('Part 2:', total)
