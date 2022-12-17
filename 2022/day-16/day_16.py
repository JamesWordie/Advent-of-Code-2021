import re

with open('day-16/sample.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

valve_store = {}
for line in data:
    rate = re.findall('rate=\d+', line)[0].replace('rate=', '')
    valves = re.findall('[A-Z]{2}', line)
    valve_store[valves[0]] = {'rate': int(rate), 'tunnels': valves[1:], 'paths': {} }
# print(valve_store)

MAX_TIME = 30
pressure = 0
curr_time = 0
open_valves = set()

################# NOT SUBMITTED - TAKEN FROM https://gist.github.com/liampwll/351fb848f05e8efd257ac87c7d09d1b0

keys = sorted([x for x in list(valve_store.keys()) if valve_store[x]['rate'] != 0])
# print(keys)

def bfs(frontier, end):
    depth = 1
    while True:
        next_path = set()
        for x in frontier:
            if x == end:
                return depth
            for y in valve_store[x]['tunnels']:
                next_path.add(y)
        frontier = next_path
        depth += 1

for k in keys + ['AA']:
    for k2 in keys:
        if k2 != k:
            valve_store[k]['paths'][k2] = bfs(valve_store[k]['tunnels'], k2)

def part1():
    best = 0
    def search(opened, flowed, current_room, depth_to_go):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valve_store[current_room]['rate'] * depth_to_go, current_room, depth_to_go - 1)
        else:
            for k in [x for x in valve_store[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valve_store[current_room]['paths'][k])

    search(set(['AA']), 0, 'AA', 29)
    return best

print('Part 1:', part1())

def part2():
    best = 0
    def search(opened, flowed, current_room, depth_to_go, elephants_turn):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valve_store[current_room]['rate'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
            if not elephants_turn:
                search(set([current_room]).union(opened), flowed + valve_store[current_room]['rate'] * depth_to_go, 'AA', 25, True)
        else:
            for k in [x for x in valve_store[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valve_store[current_room]['paths'][k], elephants_turn)

    search(set(['AA']), 0, 'AA', 25, False)
    return best

print('Part 2:', part2())
