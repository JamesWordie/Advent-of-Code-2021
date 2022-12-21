import re
from math import floor

with open('day-21/input.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

monkeys = {}
for line in data:
    monkey_id = re.findall('^\w+:', line)[0].replace(':', '')
    operations = re.findall('\w+ [+*-/] \w+', line)
    if len(operations) > 0:
        monkey1, operator, monkey2 = operations[0].split(' ')
        monkeys[monkey_id] = {
            'monkey1': monkey1,
            'monkey2': monkey2,
            'operator': operator,
            'number': None
        }
    number = re.findall('\d+', line)
    if len(number) > 0:
        monkeys[monkey_id] = {
        'monkey1': None,
        'monkey2': None,
        'operator': None,
        'number': int(number[0])
    }
# print(monkeys)

def monkey_math(curr, mnk_list):
    num = mnk_list[curr]['number']
    mon1 = mnk_list[curr]['monkey1']
    mon2 = mnk_list[curr]['monkey2']
    oper = mnk_list[curr]['operator']

    # If a number or float return the monkey
    if isinstance(num, int) or isinstance(num, float):
        return mnk_list[curr]['number']

    if oper == '+':
        return monkey_math(mon1, mnk_list) + monkey_math(mon2, mnk_list)
    elif oper == '-':
        return monkey_math(mon1, mnk_list) - monkey_math(mon2, mnk_list)
    elif oper == '/':
        return monkey_math(mon1, mnk_list) / monkey_math(mon2, mnk_list)
    elif oper == '*':
        return monkey_math(mon1, mnk_list) * monkey_math(mon2, mnk_list)

res1 = monkey_math('root', monkeys)
print('Part 1:', floor(res1))
