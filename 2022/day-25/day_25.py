with open('day-25/input.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

digits = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

transform = {v: k for k, v in digits.items()}

# Convert the snafu string into an integer
def snafu_2_int(line: str):
    current = 0
    for char in line:
        current *= 5
        current += digits[char]
    return current

def int_2_snafu(val: int):
    if val == 0:
        return ''

    remainder = (val + 2) % 5 - 2
    new_val = (val + 2) // 5

    return int_2_snafu(new_val) + transform[remainder]

# Solve for part 1
def part1(snafu_list: list):
    total_int = sum(snafu_2_int(snafu_num) for snafu_num in snafu_list)

    return int_2_snafu(total_int)

print('Part 1:', part1(data))
