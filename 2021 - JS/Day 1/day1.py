# Part 1
data = open('Day 1/input', 'r', encoding='utf-8').read().splitlines()
depths = [int(x) for x in data]
increases = sum(x < y for x, y in zip(depths, depths[1:]))
print(increases)
# 1602

# Part 2
depths = [int(x) for x in data]
increases = sum(x < y for x, y in zip(depths, depths[3:]))
print(increases)
# 1633
