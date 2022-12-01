data = open('Day 2/input', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data]
commands = [(x[0], int(x[1])) for x in data]

h, d = 0, 0

for cmd, val in commands:
    if cmd == 'forward':
        h += val
    elif cmd == 'down':
        d += val
    elif cmd == 'up':
        d -= val
    else:
        raise ValueError('Invalid command')

print(h * d)
# 1484118

aim, h, d = 0, 0, 0

for cmd, val in commands:
    if cmd == 'forward':
        h += val
        d += val * aim
    elif cmd == 'down':
        aim += val
    elif cmd == 'up':
        aim -= val
    else:
        raise ValueError('Invalid command')

print(h * d)
# 1463827010
