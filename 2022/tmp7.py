with open('sample.txt', encoding='utf-8') as file:
    data = [i.strip() for i in file.read().strip().split("\n")]
# print(data)

file_system = {}
dir_names = []
curr_dir = ''

for cmd in data:
    # if moving into a directory, NOT up!
    if '$ cd' in cmd and '..' not in cmd:
        dir = cmd.removeprefix('$ cd ')
        curr_dir += dir
        if curr_dir not in file_system:
            file_system[curr_dir] = []
        dir_names.append(dir)
    
    # moving up from directory to a parent
    elif '$ cd' in cmd and '..' in cmd:
        up_dir = len(curr_dir) - 1
        curr_dir = curr_dir.removesuffix(dir_names[up_dir])
        dir_names.pop(up_dir)
        
    # any command/statement that isn't ls or cd
    elif '$ cd' not in cmd and '$ ls' not in cmd:
        if 'dir' in cmd:
            dir = cmd.removeprefix('dir ')
            file_system[curr_dir + dir] = []
        else:
            size, name = cmd.split()
            file_system[curr_dir].append((int(size), name))
            
# print(dir_names)
# print(file_system)

total_size = {fs: 0 for fs in file_system}

# add the size for each file, with key of it's directory
for dir in file_system:
    for itm in file_system[dir]:
        total_size[dir] += itm[0]
        
# Add subdirectory size to parent directory
for key in total_size.keys():
    for dir in file_system:
        if key in dir and key != dir:
            total_size[key] += total_size[dir]
# print(total_size)

total = 0
for score in total_size.values():
    if score <= 100_000:
        total += score
        
print(total)
