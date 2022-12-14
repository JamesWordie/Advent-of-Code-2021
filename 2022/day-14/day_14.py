with open('day-14/input.txt', encoding='utf-8') as file:
    data2 = [[j.strip() for j in i.split('->')] for i in file.read().strip().split("\n")]
# print(data2)

integer_list = [[list(int(n) for n in num.split(',')) for num in sublist] for sublist in data2]
# print(integer_list)

# Don't need a grid, just coords, therefore more efficient
blocked = set()
bottom_coord = 0

for line in integer_list:
    for (x1, y1), (x2, y2) in zip(line, line[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # complex number, x real and y imaginary
                blocked.add((x, y))
                # blocked.add(x + y * 1j)
                bottom_coord = max(bottom_coord, y + 1)

# print(blocked)
# print(bottom_coord)

counter = 0

while True:
    # New sand part at 500, 0j --> 500
    sand = (500,0)
    while True:
        # Hard exit program to exit, print the counter
        if sand[1] >= bottom_coord:
            print('Part 1', counter)
            exit(0)

        # If not blocked off down
        if (sand[0], sand[1] + 1) not in blocked:
            sand = (sand[0], sand[1] + 1)
            continue
        # If not blocked off down and left
        if (sand[0] - 1, sand[1] + 1) not in blocked:
            sand = (sand[0] - 1, sand[1] + 1)
            continue
        # If not blocked off down and right
        if (sand[0] + 1, sand[1] + 1) not in blocked:
            sand = (sand[0] + 1, sand[1] + 1)
            continue

        blocked.add(sand)
        counter += 1
        break

########## Part 2 ###########

while (500, 0) not in blocked:
    # New sand part at 500, 0j --> 500
    sand = (500,0)
    while True:
        # Hard exit program to exit, print the counter
        if sand[1] >= bottom_coord:
            break
        # If not blocked off down
        if (sand[0], sand[1] + 1) not in blocked:
            sand = (sand[0], sand[1] + 1)
            continue
        # If not blocked off down and left
        if (sand[0] - 1, sand[1] + 1) not in blocked:
            sand = (sand[0] - 1, sand[1] + 1)
            continue
        # If not blocked off down and right
        if (sand[0] + 1, sand[1] + 1) not in blocked:
            sand = (sand[0] + 1, sand[1] + 1)
            continue
        break
    blocked.add(sand)
    counter += 1

print('Part 2', counter)
