with open('day-9/input.txt', encoding='utf-8') as file:
    data = [j.split() for j in [i for i in file.read().strip().split("\n")]]

# with open('day-9/sample.txt', encoding='utf-8') as file:
    # data = [j.split() for j in [i for i in file.read().strip().split("\n")]]
# print(data)

def move_snake(pos, direct):
    if direct == 'R':
        return (pos[0] + 1, pos[1])
    elif direct == 'L':
        return (pos[0] - 1, pos[1])
    elif direct == 'U':
        return (pos[0], pos[1] + 1)
    elif direct == 'D':
        return (pos[0], pos[1] - 1)

def tail_move(tail, head):
    tail_x, tail_y = tail
    head_x, head_y = head
    next_tail_pos = tail

    move_vert = abs(tail_y - head_y) > 1
    move_hor = abs(tail_x - head_x) > 1

    if not move_vert and not move_hor:
        return tail

    # If head is further right than tail
    if head_x > tail_x:
        next_tail_pos = move_snake(next_tail_pos, "R")
    # If head is further left than tail
    elif head_x < tail_x:
        next_tail_pos = move_snake(next_tail_pos, "L")

    # If head is further up than tail
    if head_y > tail_y:
        next_tail_pos = move_snake(next_tail_pos, "U")
    # If head is further down than tail
    elif head_y < tail_y:
        next_tail_pos = move_snake(next_tail_pos, "D")

    return next_tail_pos

def count_seen(moves, tail_len = 1):
    start_pos = (0, 0)
    seen = set([start_pos])

    head = start_pos
    tail = [start_pos] * tail_len

    for (direct, spaces) in moves:
        for _ in range(int(spaces)):
            head = move_snake(head, direct)

            neighbour = head
            for i, tail_pos in enumerate(tail):
                tail[i] = tail_move(tail_pos, neighbour)
                neighbour = tail[i]

            seen.add(tail[-1])

    return len(seen)

# Refactored numerous times, following improved suggestions/more efficient practises...
print('Part 1', count_seen(data))
print('Part 2',count_seen(data, 9))
