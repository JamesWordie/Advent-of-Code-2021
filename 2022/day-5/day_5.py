with open('day-5/input.txt', encoding='utf-8') as file:
    moves = [i.replace('move ', '').replace('from ' , '').replace('to ', '').split(' ') for i in file.read().strip().split("\n")]
# print(moves)

start_pos = {
  1: ['R', 'S', 'L', 'F', 'Q'],
  2: ['N', 'Z', 'Q', 'G', 'P', 'T'],
  3: ['S', 'M', 'Q', 'B'],
  4: ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
  5: ['P', 'H', 'M', 'B', 'N', 'F', 'S'],
  6: ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'],
  7: ['W', 'C', 'F'],
  8: ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'],
  9: ['G', 'Z', 'D', 'L', 'C', 'N', 'R'],
}

sample = {
  1: ['Z', 'N'],
  2: ['M', 'C', 'D'],
  3: ['P']
}

sample_moves = [['1','2','1'], ['3','1','3'], ['2','2','1'], ['1','1','2']]

# move 1 from 2 to 6
for i in moves:
  move = int(i[0])
  start = int(i[1])
  end = int(i[2])

  for _ in range(move):
    if (len(start_pos[start]) != 0):
      start_pos[end].append(start_pos[start].pop())

# print(start_pos)

last_cont_pos = ""
for i in range(1,10):
  last_cont_pos += (start_pos[i][-1])

print('Part 1', last_cont_pos)

'''Part 2'''

start_pos = {
  1: ['R', 'S', 'L', 'F', 'Q'],
  2: ['N', 'Z', 'Q', 'G', 'P', 'T'],
  3: ['S', 'M', 'Q', 'B'],
  4: ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
  5: ['P', 'H', 'M', 'B', 'N', 'F', 'S'],
  6: ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'],
  7: ['W', 'C', 'F'],
  8: ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'],
  9: ['G', 'Z', 'D', 'L', 'C', 'N', 'R'],
}

for i in moves:
  move = int(i[0])
  start = int(i[1])
  end = int(i[2])

  tmp = []
  for _ in range(move):
    if (len(start_pos[start]) != 0):
      tmp.append(start_pos[start].pop())

  tmp.reverse()
  start_pos[end] += tmp
  tmp = []

last_cont_pos_p2 = ""
for i in range(1,10):
  last_cont_pos_p2 += (start_pos[i][-1])

print('Part 2', last_cont_pos_p2)
