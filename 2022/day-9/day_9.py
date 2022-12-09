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
    t_x, t_y = tail
    h_x, h_y = head
    next_tail = tail

    move_vert = abs(t_y - h_y) > 1
    move_hor = abs(t_x - h_x) > 1

    if not move_vert and not move_hor:
        return tail

    # If head is further right than tail
    if h_x > t_x:
        next_tail = move_snake(next_tail, "R")
    # If head is further left than tail
    elif h_x < t_x:
        next_tail = move_snake(next_tail, "L")

    # If head is further up than tail
    if h_y > t_y:
        next_tail = move_snake(next_tail, "U")
    # If head is further down than tail
    elif h_y < t_y:
        next_tail = move_snake(next_tail, "D")

    return next_tail

def count_seen(moves, tail_len = 1):
    start_pos = (0, 0)
    visited = set([start_pos])

    head = start_pos
    tail = [start_pos] * tail_len

    for (direct, spaces) in moves:
        for _ in range(int(spaces)):
            head = move_snake(head, direct)

            next_piece = head
            for i, tail_pos in enumerate(tail):
                tail[i] = tail_move(tail_pos, next_piece)
                next_piece = tail[i]

            visited.add(tail[-1])

    return len(visited)

# Refactored numerous times, following improved suggestions/more efficient practises...
print('Part 1', count_seen(data))
print('Part 2',count_seen(data, 9))
