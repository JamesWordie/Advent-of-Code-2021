
def get_data(key):
    with open('day-20/input.txt', encoding='utf-8') as file:
        numbers = [(ind, int(val) * key) for ind, val in enumerate(file.read().strip().split("\n"))]
        original_nums = [n[1] for n in numbers]
    return numbers, original_nums

# print(numbers)
# print(original_nums)

def mix(nums, original):
    for ind, num in enumerate(original):
        number = num
        find = (ind, num)

        # Find index of num
        index = nums.index(find)

        # Generate left and right lists
        left = nums[:index]
        right = nums[index + 1:]
        temp = left + right

        # Insert new pos
        new_pos = (index + number) % len(temp)
        if new_pos == 0:
            temp.append(find)
        else:
            temp.insert(new_pos, find)

        # Update nums
        nums = temp
    return nums

def get_coords(nums):
    counter = 0
    indices = [1000, 2000, 3000]

    # Find the zero index
    for ind, val in enumerate(nums):
        if val[1] == 0:
            break

    # Get coords
    for i in indices:
        counter += nums[(ind + i) % len(nums)][1]
    return counter

nums, orig_nums = get_data(1)
mixed = mix(nums, orig_nums)
print('Part 1:', get_coords(mixed))

nums, orig_nums = get_data(811589153)
for i in range(10):
    shuffled = mix(nums, orig_nums)
    nums = shuffled

print('Part 2:', get_coords(nums))
