with open('day-13/input.txt', encoding='utf-8') as file:
    data = [[eval(j) for j in i.split('\n')] for i in file.read().strip().split("\n\n")]
# print(data)

def check_int(itm):
    return type(itm) is int

def check_list(itm):
    return type(itm) is list

# def itm_checks(left, right, ind):
#     # same list len and no diff
#     if len(left) <= ind >= len(right):
#         return None
#     # right list len < left list len
#     if ind >= len(right):
#         return False
#     # left list len < right list len
#     if ind >= len(left):
#         return True

def compare_val(left, right, ind):
    # print(left, right, ind)
    # itm_checks(left, right, ind)
        # same list len and no diff
    if len(left) <= ind >= len(right):
        return None
    # right list len < left list len
    if ind >= len(right):
        return False
    # left list len < right list len
    if ind >= len(left):
        return True

    l_val, r_val = left[ind], right[ind]

    # if both are integers
    if check_int(l_val) and check_int(r_val):
        if l_val == r_val:
            result = compare_val(left, right, ind + 1)
        else:
            return r_val > l_val
    # if both are lists
    elif check_list(l_val) and check_list(r_val):
        # set the index to zero again for eval
        result = compare_val(l_val, r_val, 0)
    else:
        if check_int(l_val):
            l_val = [l_val]
        else:
            r_val = [r_val]
        # compare both values now both are lists, with index 0
        result = compare_val(l_val, r_val, 0)

    if result is None:
        return compare_val(left, right, ind + 1)
    return result

result_list = []
itr_counter = 1

for pair in data:
    left_itm, right_itm = pair
    if compare_val(left_itm, right_itm, 0):
        result_list += [itr_counter]
    else:
        result_list += []
    itr_counter += 1

print('Part 1', sum(result_list))
