import re

with open('day-15/input.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

sensors = list()
beacons = list()
not_beacons = set()
ROW_INP = 2000000
# ROW_INP = 10

for index,pair in enumerate(data):
    x_vals = [int(val.replace('x=', '')) for val in re.findall('x=-?\d+', pair)]
    y_vals = [int(val.replace('y=', '')) for val in re.findall('y=-?\d+', pair)]
    x_sen, x_beac = x_vals
    y_sen, y_beac = y_vals

    # Manhattan Dist
    man_dist = (abs(x_sen - x_beac) + abs(y_sen - y_beac))

    # Max steps on the row in question (radius from sensor)
    row_steps = man_dist - abs(ROW_INP - y_sen)

    sensors.append((x_sen, y_sen, man_dist, row_steps))
    beacons.append((x_beac, y_beac))

# print(sensors)
# print(beacons)

for sensor in sensors:
    sen_x, sen_y, man_dis, steps = sensor

    if steps < 0:
        continue

    for x in range(sen_x - steps, sen_x + steps + 1):
        position = (x, ROW_INP)
        if position not in beacons:
            not_beacons.add(position)

print('Part 1', len(not_beacons))

X_MIN, Y_MIN = 0, 0
X_MAX, Y_MAX = 4_000_000, 4_000_000
