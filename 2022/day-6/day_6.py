sample = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

with open('day-6/input.txt', encoding='utf-8') as file:
    data = file.read().strip()

split = []
for i in data:
  split += i

# def check_unique(string):
  # for i in range(len(string)):
  #   for j in range(i + 1,len(string)):
  #     if(string[i] == string[j]):
  #       return False
  # return True

def solve(split_arr, skip):
  start = 0
  end = 0
  while start < len(split_arr):
    if len(set(split_arr[start:start + skip])) == skip:
    # if check_unique(split_arr[start:start + skip]):
      end = start + skip
      break
    else:
      start += 1

  return end

print('Part 1', solve(split, 4))
print('Part 2', solve(split, 14))

# Shortened solution from someone at Le Wagon AOC
# part_1 = next(i + 4 for i, _ in enumerate(split) if len(set(split[i:i + 4])) == 4)
# part_2 = next(i + 14 for i, _ in enumerate(split) if len(set(split[i:i + 14])) == 14)

# print(part_1)
# print(part_2)
