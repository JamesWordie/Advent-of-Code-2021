from collections import deque

cubes = {}

with open('day-18/input.txt', encoding='utf-8') as file:
    for line in file.read().strip().split('\n'):
        coord = tuple(map(int, line.split(',')))
        cubes[coord] = 6
# print(cubes)

def neighbours(x,y,z):
    """Yield generator function to find neighbours of x,y,z

    Yields:
        tuple: neighbours of x,y,z for each +/- 1
    """
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)

for cube in cubes:
    cubes[cube] -= sum(n in cubes for n in neighbours(*cube))
# print(cubes)

edges = sum(cubes.values())
print('Part 1:', edges)

# Setup for external box/edges to perform a search later
min_x = min_y = min_z = float('inf')
max_x = max_y = max_z = 0

# Set the min and max values for x, y, z
for x, y, z in cubes:
    min_x, max_x = min(x, min_x), max(x, max_x)
    min_y, max_y = min(y, min_y), max(y, max_y)
    min_z, max_z = min(z, min_z), max(z, max_z)

def escape_box(all_cubes, curr_cube):
    """DFS function for flood fill of the outer box

    Args:
        all_cubes (dict): dictionary, key of the coords, and value of the number of faces
        curr_cube (tuple): current cube

    Return:
        edges_touched: return 0 if able to escape, eg an external area, or the counter if stuck
        visited: a set of the visited coords
    """
    visited = set()
    queue = deque([curr_cube])
    edges_touched = 0

    while queue:
        p = queue.pop()
        if p in visited:
            continue

        visited.add(p)
        x, y, z, = p

        # Did we escape the bounding box?
        if not (min_x <= x <= max_x) or not (min_y <= y <= max_y) or not (min_z <= z <= max_z):
            # If so, we are not trapped in an internal pocket
            return 0, visited

        # Try exploring all 6 directions
        for n in neighbours(x, y, z):
            # If we are blocked in this direction, it means we touched an internal face
            if n in all_cubes:
                edges_touched += 1
            else:
                # Otherwise, keep going
                if n not in visited:
                    queue.append(n)

    # We ran out of free space to visit, which means we are trapped in an internal pocket
    return edges_touched, visited

all_visited = set()

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        for z in range(min_z, max_z + 1):
            cube = (x, y, z)
            # this is an empty unit cube of space
            if cube not in cubes:
                # this is not in an internal pocket we already found
                if cube not in all_visited:
                    touched, visited = escape_box(cubes, cube)
                    all_visited |= visited

                    if touched > 0:
                        edges -= touched

print('Part 2:', edges)
