with open('day-4/input.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

sample = [
  "2-4,6-8",
  "2-3,4-5",
  "5-7,7-9",
  "2-8,3-7",
  "6-6,4-6",
  "2-6,4-8"
]

split_pairs = []
overlaps = 0
partial_overlaps = 0

for x in data:
  split_pairs.append(x.split(','))
# print(split_pairs)


for i in split_pairs:
  first = i[0].split('-')
  second = i[1].split('-')

  first0 = int(first[0])
  first1 = int(first[1])
  second0 = int(second[0])
  second1 = int(second[1])

  #
  if ((first0 <= second0 and first1 >= second1) or (first0 >= second0 and first1 <= second1)):
    overlaps += 1

  if (first1 >= second0 and second1 >= first0):
    partial_overlaps += 1

print('part1', overlaps)
print('part2', partial_overlaps)
