with open('day-23/input.txt', encoding='utf-8') as file:
    data = [list(i) for i in file.read().strip().split("\n")]
# print(data)

# Elf class, stores location and proposal
# class Elf:
#     def __init__(self, location: tuple):
#         self.location = location
#         self.proposal = None

#     def make_proposal(self, new_pos: tuple):
#         self.proposal = new_pos

# Constants/variables
elves = set()
neighbours = {
    'N': (0,-1),
    'NE': (1,-1),
    'E': (1,0),
    'SE': (1,1),
    'S': (0,1),
    'SW': (-1,1),
    'W': (-1,0),
    'NW': (-1,-1)
}

# Track the starting pos of elves
for x, row in enumerate(data):
    for y, col in enumerate(row):
        if col == '#':
            elves.add((y,x))
# print(elves)
elves_p2 = elves

# Return neighbour coords --> return list of tuple coords
def neighbour_coords(elf: tuple, ngbr: list) -> list:
    ngbr_coords = []

    for n in ngbr:
        cur_x, cur_y = elf
        ngbr_x, ngbr_y = neighbours[n]

        new_x = cur_x + ngbr_x
        new_y = cur_y + ngbr_y

        ngbr_coords.append((new_x, new_y))

    return ngbr_coords

def solve(elf_set, part2 = False):
    tmp_eleves = elf_set
    counter = 0

    while True:
        proposals = {}
        new_elves = set()
        i = counter % 4
        counter += 1

        for elf in tmp_eleves:
            x, y = elf
            north_check = neighbour_coords(elf, ['NW', 'N', 'NE'])
            south_check = neighbour_coords(elf, ['SW', 'S', 'SE'])
            west_check = neighbour_coords(elf, ['NW', 'W', 'SW'])
            east_check = neighbour_coords(elf, ['NE', 'E', 'SE'])
            check = [item for sublist in [north_check, south_check, west_check, east_check] for item in sublist]
            # print(check)

            # stationary end goal
            if all([x not in tmp_eleves for x in check]):
                new_elves.add(elf)
                continue

            # Check the north direction
            if i == 0 and all([x not in tmp_eleves for x in north_check]):
                proposals[elf] = (x, y-1)
                continue

            # Check the south direction
            if i <= 1 and all([x not in tmp_eleves for x in south_check]):
                proposals[elf] = (x, y+1)
                continue

            # Check the west direction
            if i <= 2 and all([x not in tmp_eleves for x in west_check]):
                proposals[elf] = (x-1, y)
                continue

            # Check the east direction
            if i <= 3 and all([x not in tmp_eleves for x in east_check]):
                proposals[elf] = (x+1, y)
                continue

            # Second checks to emulate the list wrap

            # Check the north direction
            if all([x not in tmp_eleves for x in north_check]):
                proposals[elf] = (x, y-1)
                continue

            # Check the south direction
            if all([x not in tmp_eleves for x in south_check]):
                proposals[elf] = (x, y+1)
                continue

            # Check the west direction
            if all([x not in tmp_eleves for x in west_check]):
                proposals[elf] = (x-1, y)
                continue

            # Check the east direction
            if all([x not in tmp_eleves for x in east_check]):
                proposals[elf] = (x+1, y)
                continue

            # No movements
            new_elves.add(elf)

        # invert dictionary
        tmp = {}
        for k, v in proposals.items():
            if v not in tmp: tmp[v] = [k]
            else: tmp[v].append(k)

        for k, v in tmp.items():
            if len(v) == 1:
                new_elves.add(k)
            else:
                new_elves.update(v)

        if part2:
            if len(tmp_eleves & new_elves) == len(tmp_eleves):
              break

        # Set the elves set for next iteration
        tmp_eleves = new_elves

        # If counter == 10, ie part 1, and not part 2 exact and return the elves set
        if counter == 10 and not part2:
            break

    # If part 2 return the counter for the number of rounds till they are stationary
    if part2:
        return counter

    # Return the elves set for part 1
    return tmp_eleves

# Solve for part 1
elves = solve(elves)

# Find box area for part 1
x_min = min(elves, key=lambda t: t[0])[0]
x_max = max(elves, key=lambda t: t[0])[0]
y_min = min(elves, key=lambda t: t[1])[1]
y_max = max(elves, key=lambda t: t[1])[1]
area = (1 + x_max - x_min) * (1 + y_max - y_min)

# Answer for part 1
print('Part 1:', area - len(elves))

# Solve and answer for part 2
print('Part 2:', solve(elves_p2, part2=True))
