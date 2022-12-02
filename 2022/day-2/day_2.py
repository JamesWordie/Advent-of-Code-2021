with open('input', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

sample = [
  'A Y',
  'B X',
  'C Z'
]
# Part 1 --> 15
# Part 2 --> 12

# AX - rock
# BY - paper
# CZ - scissor

''' COMP & PLAY
rock & rock == 4
rock & paper == 8
rock & scissor == 3
paper & paper == 5
paper & scissor == 9
paper & rock == 1
scissor & scissor == 6
scissor & rock == 7
scissor & paper == 2
'''

def compare(comp, play):
  # A & X == 4
  if (comp == 'A' and play == 'X'):
    return 4
  # A & Y == 8
  elif (comp == 'A' and play == 'Y'):
    return 8
  # A & Z == 3
  elif (comp == 'A' and play == 'Z'):
    return 3
  # B & Y == 5
  elif (comp == 'B' and play == 'Y'):
    return 5
  # B & Z == 9
  elif (comp == 'B' and play == 'Z'):
    return 9
  # B & X == 1
  elif (comp == 'B' and play == 'X'):
    return 1
  # C & Z == 6
  elif (comp == 'C' and play == 'Z'):
    return 6
  # C & X == 7
  elif (comp == 'C' and play == 'X'):
    return 7
  # C & Y == 2
  elif (comp == 'C' and play == 'Y'):
    return 2

split_data = []
for i in data:
  j = i.split(' ')
  split_data.append([j[0], j[1]])

score = 0

for game in split_data:
  score += compare(game[0], game[1])

print('Part 1', score)

# Part 2

# X --> loss
# Y --> draw
# Z --> win

'''COMP & PLAY-RESULT
A & X == 3
A & Y == 4
A & Z == 8
B & X == 1
B & Y == 5
B & Z == 9
C & X == 2
C & Y == 6
C & Z == 7
'''

new_score = 0

def new_compare(comp, play):
    # A & X == 3
  if (comp == 'A' and play == 'X'):
    return 3
  # A & Y == 4
  elif (comp == 'A' and play == 'Y'):
    return 4
  # A & Z == 8
  elif (comp == 'A' and play == 'Z'):
    return 8
  # B & Y == 5
  elif (comp == 'B' and play == 'Y'):
    return 5
  # B & Z == 9
  elif (comp == 'B' and play == 'Z'):
    return 9
  # B & X == 1
  elif (comp == 'B' and play == 'X'):
    return 1
  # C & Z == 7
  elif (comp == 'C' and play == 'Z'):
    return 7
  # C & X == 2
  elif (comp == 'C' and play == 'X'):
    return 2
  # C & Y == 6
  elif (comp == 'C' and play == 'Y'):
    return 6

for game in split_data:
  new_score += new_compare(game[0], game[1])

print('Part 2', new_score)
