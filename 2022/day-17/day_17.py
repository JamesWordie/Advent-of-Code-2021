from collections import defaultdict

with open('day-17/input.txt', encoding='utf-8') as file:
    data = [list(i) for i in file.read().strip().split("\n")][0]
# print(data)

ROCKS = [
    [(2, 0), (3, 0), (4, 0), (5, 0)], # Horizontal Line
    [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)], # Plus
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)], # L
    [(2, 0), (2, 1), (2, 2), (2, 3)], # Vertical Bar
    [(2, 0), (2, 1), (3, 0), (3, 1)], # Square
]

######## NOT SUBMITTED - TAKEN FROM https://github.com/morgoth1145/advent-of-code/blob/5a82bcfb40eb12025a3e635026643288aa14b887/2022/17/solution.py

def solve(s, CYCLE_COUNT):
    TOWER_WIDTH = 7

    tower = {(x, 0) for x in range(TOWER_WIDTH)}
    tower_height = 0

    cycle_idx = 0
    jet_idx = 0

    history = defaultdict(list)

    while cycle_idx < CYCLE_COUNT:
        current_cycle = cycle_idx
        cycle_idx += 1

        rock_idx = current_cycle % len(ROCKS)
        rock = ROCKS[rock_idx]
        y_off = tower_height + 4
        rock = [(x, y+y_off) for x, y in rock]

        cycle_key = (rock_idx, jet_idx)

        move_x, move_y = 0, 0

        # Make it rain!
        while True:
            jet = -1 if s[jet_idx] == '<' else 1
            jet_idx = (jet_idx + 1) % len(s)

            test_rock = [(x+jet, y) for x, y in rock]
            if any(x < 0 or x >= TOWER_WIDTH for x, y in test_rock):
                test_rock = rock
            elif any(c in tower for c in test_rock):
                test_rock = rock
            else:
                move_x += jet

            rock = test_rock
            test_rock = [(x, y-1) for x,y in rock]
            if any(c in tower for c in test_rock):
                # It settled
                tower.update(rock)
                tower_height = max(tower_height, max(y for x,y in rock))

                if history is None:
                    # We must be wrapping up at this point
                    break

                key = (cycle_key, move_x, move_y)

                cycle_history = history[key]

                if len(cycle_history) > 1:
                    last_y_diff = cycle_history[-1][0] - cycle_history[-2][0]
                    curr_y_diff = tower_height - cycle_history[-1][0]

                    if last_y_diff == curr_y_diff:
                        cycle_diff = current_cycle - cycle_history[-1][1]

                        remaining_cycles = CYCLE_COUNT - current_cycle - 1

                        supercycles = remaining_cycles // cycle_diff
                        skipped_cycles = supercycles * cycle_diff

                        height_mod = supercycles * curr_y_diff

                        tower = {(x, y+height_mod) for x, y in tower}
                        tower_height += height_mod

                        cycle_idx += skipped_cycles

                        # We jumped ahead once, no need to do it again!
                        history = None
                        break

                cycle_history.append((tower_height, current_cycle))
                break

            move_y -= 1
            rock = test_rock

    return tower_height

print('Part 1: ',solve(data, 2022))
print('Part 2: ',solve(data, 1000000000000))
