# with open('day-3/input.txt', encoding='utf-8') as file:
#     data = [i for i in file.read().strip().split("\n")]
# print(data)

sample = [
  "vJrwpWtwJgWrhcsFMMfFFhFp",
  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
  "PmmdzqPrVvPwwTWBwg",
  "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
  "ttgJtRGJQctTZtZT",
  "CrZsJsPPZsGzwwsLwLmpwMDw"
]

# print(sum(
#     (ord(x) - ord("a")) % 58 + 1
#     for l in data
#     for x in set(l[: len(l) // 2]) & set(l[len(l) // 2 :])
# ))

# print(sum(
#     (ord(x) - ord("a")) % 58 + 1
#     for a, b, c in zip(*[iter(data)] * 3)
#     for x in set(a) & set(b) & set(c)
# ))

file = open('day-3/input.txt')
total = 0

while True:
    line = file.readline()
    if not line:
        break

    half = int((len(line)-1)/2)
    left_half = line[0:half]
    right_half = line[half:-1]
    for char in left_half:
        if char in right_half:
            num_char = ord(char)-96
            if num_char < 0:
                num_char += 58
            total += num_char
            break

print(total)
file.close()
