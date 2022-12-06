sample = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

with open('day-6/input.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]

split = []
for i in data:
  split += i

def check_unique(string):
  for i in range(len(string)):
    for j in range(i + 1,len(string)):
      if(string[i] == string[j]):
        return False
  return True

def solve(split_arr, skip):
  start = 0
  end = 0
  while start < len(split_arr):
    if check_unique(split_arr[start:start + skip]):
      end = start + skip
      break
    else:
      start += 1

  return end

print('Part 1', solve(split, 4))
print('Part 2', solve(split, 14))
