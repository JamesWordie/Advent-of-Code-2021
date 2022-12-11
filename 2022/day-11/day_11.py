# Parse the input to create a monkey instance
# Loop through in range 1-20
## Starting with Money 0
## Loop through the monkeys items
## Run the calculation on the item
## Test the item score
## If true or false, pass item to said monkey
## Increment monkey id with an item counter
## Move to the next monkey
# Once gone through all monkeys, repeat 20 times
# Find the two most visited monkeys
# Multiply the score for PART 1


from math import floor, prod, lcm

with open('day-11/input.txt', encoding='utf-8') as file:
    data = [j.split('\n') for j in [i.rstrip() for i in file.read().strip().split("\n\n")]]

class Monkey:
    def __init__(self, monkey_id:int, items:list, operation:str, test_int:int, true_id:int, false_id:int, part_2:bool):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.true_id = true_id
        self.false_id = false_id
        self.test_int = test_int
        self.counter = 0
        self.part_2 = part_2

    def calculation(self, old:int, lcm_modulo:int):
        _, operator, arg2  = self.operation.split()
        second_arg = old if arg2 == 'old' else int(arg2)
        if operator == '+':
            if self.part_2:
                return ((old + second_arg) % lcm_modulo)
            return floor((old + second_arg) / 3)
        elif operator == '*':
            if self.part_2:
                return ((old * second_arg) % lcm_modulo)
            return floor((old * second_arg) / 3)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def test_item(self, item):
        if item % self.test_int == 0:
            return True
        else:
            return False

    def solve(self, item, lcm_modulo):
        new_item = self.calculation(item, lcm_modulo)
        test_new = self.test_item(new_item)
        self.remove_item(item)
        self.counter += 1
        if test_new:
            return (self.true_id, new_item)
        else:
            return (self.false_id, new_item)

    def get_id(self):
        return self.monkey_id

    def get_items(self):
        return self.items

    def get_counter(self):
        return self.counter

monkey_list = dict()

def solve_problem(rounds:int, part_2 = False):
    # sample_monkey_test_lcm = lcm(13, 17, 19, 23) # 96577
    monkey_test_lcm = lcm(7,2,19,3,13,11,5,17) # 9699690

    for monkey in data:
        monkey_id, items, operation, test, true_id, false_id = monkey
        int_id = int(monkey_id.replace('Monkey ', '').replace(':', ''))
        items_list = [int(i) for i in items.strip().replace('Starting items: ', '').replace(',', '').split()]
        operation_str = operation.split('= ')[1]
        test_int = int(test.split('by ')[1])
        true_id_int = int(true_id.split('monkey ')[1])
        false_id_int = int(false_id.split('monkey ')[1])

        monkey_list[int_id] = Monkey(int_id, items_list, operation_str, test_int, true_id_int, false_id_int, part_2)

    # Loop in range
    for _ in range(rounds):
        # Loop for monkey in each round
        for monkey in monkey_list.items():
            _, monkey_obj = monkey
            if len(monkey_obj.get_items()) == 0:
                continue
            # Loop items in each monkey
            for _ in range(len(monkey_obj.get_items())):
                item = monkey_obj.get_items()[0]
                move_id, new_item = monkey_obj.solve(item, monkey_test_lcm)
                monkey_list[move_id].add_item(new_item)

    monkey_counter = []
    # Get all monkey counter, add to list
    for monkey in monkey_list.values():
        monkey_counter.append(monkey.get_counter())

    # Get product of two greater and return
    monkey_product = prod(sorted(monkey_counter, reverse=True)[0:2])
    return monkey_product

print('Part 1: ', solve_problem(20))

print('Part 2: ', solve_problem(10000, part_2=True))
