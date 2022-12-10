with open('day-10/input.txt', encoding='utf-8') as file:
    data = [j.split() for j in [i for i in file.read().strip().split("\n")]]
# print(data)

cycle = 0
score_dict = {}
V = 1

for cmd in data:
    if cmd[0].startswith('noop'):
        cycle += 1
        score_dict[cycle] = V
    elif cmd[0].startswith('addx'):
        cycle += 1
        score_dict[cycle] = V
        cycle += 1
        score_dict[cycle] = V
        V += int(cmd[1])

# print(score_dict)
DELIMITER = [20, 60, 100, 140, 180, 220]
counter = 0
for score in score_dict.items():
    key, val = score
    # print('key: ', key, 'val: ', val)
    if key in DELIMITER:
        counter += (key * int(val))

print('Part 1', counter)

crt_string = ""
for cyc in range(1, 241):
    if score_dict[cyc] - 1 <= (cyc % 40 - 1) % 40 <= score_dict[cyc] + 1:
        crt_string += '#'
    else:
        crt_string += '.'
    if cyc % 40 == 0:
        crt_string += '\n'
print('Part 2:')
print(crt_string)
