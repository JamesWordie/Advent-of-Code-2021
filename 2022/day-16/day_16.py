import re

with open('day-16/sample.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

valve_dict = {}
for line in data:
    rate = re.findall('rate=\d+', line)[0].replace('rate=', '')
    valves = re.findall('[A-Z]{2}', line)
    valve_dict[valves[0]] = {'rate': int(rate), 'ngbr': valves[1:]}
# print(valve_dict)

MAX_TIME = 30
pressure = 0
curr_time = 0
open_valves = set()

# def skip_valve(valve_rate):
#     return valve_rate == 0

# def move_ngbr(ngbr):
#     for val in ngbr:
#         if valve_dict[val] in open_valves:
#             continue
#         elif valve_dict[val] not in open_valves:
#             return val
#         else:
#             return None
#     return None

# while curr_time < MAX_TIME:
#     curr_pos =list(valve_dict.keys())[0]
#     # print(curr_pos)
#     if skip_valve(valve_dict[curr_pos]['rate']):
#         if
#         curr_pos = curr_pos['ngbr'][0]
#         curr_time += 1
#         break
#     else:
#         pressure += curr_time * valve_dict[curr_pos]['rate']

#     curr_time += 1

# https://gist.github.com/liampwll/351fb848f05e8efd257ac87c7d09d1b0

# Link above

# valves = {}
# valves['VR'] = {'flow': 11, 'tunnels': 'LH, KV, BP'.split(', '), 'paths': {}}
# valves['UV'] = {'flow': 0, 'tunnels': 'GH, RO'.split(', '), 'paths': {}}
# valves['OH'] = {'flow': 0, 'tunnels': 'AJ, NY'.split(', '), 'paths': {}}
# valves['GD'] = {'flow': 0, 'tunnels': 'TX, PW'.split(', '), 'paths': {}}
# valves['NS'] = {'flow': 0, 'tunnels': 'AJ, AA'.split(', '), 'paths': {}}
# valves['KZ'] = {'flow': 18, 'tunnels': 'KO, VK, PJ'.split(', '), 'paths': {}}
# valves['AH'] = {'flow': 0, 'tunnels': 'ZP, DI'.split(', '), 'paths': {}}
# valves['SA'] = {'flow': 0, 'tunnels': 'VG, JF'.split(', '), 'paths': {}}
# valves['VK'] = {'flow': 0, 'tunnels': 'RO, KZ'.split(', '), 'paths': {}}
# valves['GB'] = {'flow': 0, 'tunnels': 'XH, AA'.split(', '), 'paths': {}}
# valves['AJ'] = {'flow': 6, 'tunnels': 'IC, OH, ZR, NS, EM'.split(', '), 'paths': {}}
# valves['PJ'] = {'flow': 0, 'tunnels': 'KZ, SP'.split(', '), 'paths': {}}
# valves['KO'] = {'flow': 0, 'tunnels': 'KZ, LE'.split(', '), 'paths': {}}
# valves['AA'] = {'flow': 0, 'tunnels': 'TW, GB, TI, NS, UL'.split(', '), 'paths': {}}
# valves['TW'] = {'flow': 0, 'tunnels': 'TU, AA'.split(', '), 'paths': {}}
# valves['VG'] = {'flow': 25, 'tunnels': 'SA'.split(', '), 'paths': {}}
# valves['BP'] = {'flow': 0, 'tunnels': 'RO, VR'.split(', '), 'paths': {}}
# valves['XH'] = {'flow': 0, 'tunnels': 'GB, RI'.split(', '), 'paths': {}}
# valves['TX'] = {'flow': 0, 'tunnels': 'RI, GD'.split(', '), 'paths': {}}
# valves['IR'] = {'flow': 10, 'tunnels': 'TN, NY, JF'.split(', '), 'paths': {}}
# valves['TU'] = {'flow': 0, 'tunnels': 'JD, TW'.split(', '), 'paths': {}}
# valves['KC'] = {'flow': 0, 'tunnels': 'SP, RO'.split(', '), 'paths': {}}
# valves['LN'] = {'flow': 0, 'tunnels': 'EM, RI'.split(', '), 'paths': {}}
# valves['HD'] = {'flow': 0, 'tunnels': 'FE, SC'.split(', '), 'paths': {}}
# valves['KE'] = {'flow': 0, 'tunnels': 'OM, RI'.split(', '), 'paths': {}}
# valves['VY'] = {'flow': 0, 'tunnels': 'PW, BS'.split(', '), 'paths': {}}
# valves['LH'] = {'flow': 0, 'tunnels': 'OM, VR'.split(', '), 'paths': {}}
# valves['EM'] = {'flow': 0, 'tunnels': 'AJ, LN'.split(', '), 'paths': {}}
# valves['SO'] = {'flow': 22, 'tunnels': 'ZP, FE'.split(', '), 'paths': {}}
# valves['EC'] = {'flow': 0, 'tunnels': 'OM, UL'.split(', '), 'paths': {}}
# valves['KV'] = {'flow': 0, 'tunnels': 'SP, VR'.split(', '), 'paths': {}}
# valves['FE'] = {'flow': 0, 'tunnels': 'SO, HD'.split(', '), 'paths': {}}
# valves['TI'] = {'flow': 0, 'tunnels': 'AA, PW'.split(', '), 'paths': {}}
# valves['SC'] = {'flow': 14, 'tunnels': 'HD'.split(', '), 'paths': {}}
# valves['ZP'] = {'flow': 0, 'tunnels': 'SO, AH'.split(', '), 'paths': {}}
# valves['RO'] = {'flow': 19, 'tunnels': 'UV, BP, VK, KC'.split(', '), 'paths': {}}
# valves['ZR'] = {'flow': 0, 'tunnels': 'OM, AJ'.split(', '), 'paths': {}}
# valves['JL'] = {'flow': 21, 'tunnels': 'GN, TN'.split(', '), 'paths': {}}
# valves['PW'] = {'flow': 9, 'tunnels': 'TI, GN, VY, GD, IC'.split(', '), 'paths': {}}
# valves['UL'] = {'flow': 0, 'tunnels': 'EC, AA'.split(', '), 'paths': {}}
# valves['GN'] = {'flow': 0, 'tunnels': 'JL, PW'.split(', '), 'paths': {}}
# valves['TN'] = {'flow': 0, 'tunnels': 'JL, IR'.split(', '), 'paths': {}}
# valves['NV'] = {'flow': 0, 'tunnels': 'RI, JD'.split(', '), 'paths': {}}
# valves['DI'] = {'flow': 23, 'tunnels': 'LE, AH'.split(', '), 'paths': {}}
# valves['IC'] = {'flow': 0, 'tunnels': 'PW, AJ'.split(', '), 'paths': {}}
# valves['JF'] = {'flow': 0, 'tunnels': 'SA, IR'.split(', '), 'paths': {}}
# valves['LE'] = {'flow': 0, 'tunnels': 'DI, KO'.split(', '), 'paths': {}}
# valves['BS'] = {'flow': 0, 'tunnels': 'JD, VY'.split(', '), 'paths': {}}
# valves['JD'] = {'flow': 15, 'tunnels': 'NV, TU, BS'.split(', '), 'paths': {}}
# valves['SP'] = {'flow': 24, 'tunnels': 'KC, KV, PJ'.split(', '), 'paths': {}}
# valves['NY'] = {'flow': 0, 'tunnels': 'IR, OH'.split(', '), 'paths': {}}
# valves['OM'] = {'flow': 7, 'tunnels': 'EC, GH, KE, ZR, LH'.split(', '), 'paths': {}}
# valves['GH'] = {'flow': 0, 'tunnels': 'OM, UV'.split(', '), 'paths': {}}
# valves['RI'] = {'flow': 3, 'tunnels': 'NV, KE, LN, XH, TX'.split(', '), 'paths': {}}

# keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])

# def bfs(frontier, end):
#     depth = 1
#     while True:
#         next_frontier = set()
#         for x in frontier:
#             if x == end:
#                 return depth
#             for y in valves[x]['tunnels']:
#                 next_frontier.add(y)
#         frontier = next_frontier
#         depth += 1

# for k in keys + ['AA']:
#     for k2 in keys:
#         if k2 != k:
#             valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)

# def part1():
#     best = 0
#     def search(opened, flowed, current_room, depth_to_go):
#         nonlocal best
#         if flowed > best:
#             best = flowed

#         if depth_to_go <= 0:
#             return

#         if current_room not in opened:
#             search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1)
#         else:
#             for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
#                 search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k])

#     search(set(['AA']), 0, 'AA', 29)
#     print(best)

# part1()

# def part2():
#     best = 0
#     def search(opened, flowed, current_room, depth_to_go, elephants_turn):
#         nonlocal best
#         if flowed > best:
#             best = flowed

#         if depth_to_go <= 0:
#             return

#         if current_room not in opened:
#             search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
#             if not elephants_turn:
#                 search(set([current_room]).union(opened), flowed + valves[current_room]['flow'] * depth_to_go, 'AA', 25, True)
#         else:
#             for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
#                 search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k], elephants_turn)

#     search(set(['AA']), 0, 'AA', 25, False)
#     print(best)

# part2()
