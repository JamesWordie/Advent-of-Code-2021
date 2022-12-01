import copy

sample = [
  "1000",
  "2000",
  "3000",
  "",
  "4000",
  "",
  "5000",
  "6000",
  "",
  "7000",
  "8000",
  "9000",
  "",
  "10000"
]
# data = open('day-1/input', 'r', encoding='utf-8').read().splitlines()
# print(data)

with open('input', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

totals = []
counter  = 0
for i in data:
  if i == "":
    totals.append(counter)
    counter = 0
  else:
    counter += int(i)

# print(totals)
print('Part 1', max(totals))

rev_totals = totals.copy()
rev_totals.sort(reverse=True)
print('Part 2', sum(rev_totals[0:3]))
