from os.path import abspath, join

# Sample Output
# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)

with open('day-7/input.txt', encoding='utf-8') as file:
    data = [i for i in file.read().strip().split("\n")]
# print(data)

# with open('day-7/sample.txt', encoding='utf-8') as file:
#     data = [i for i in file.read().strip().split("\n")]
# print(data)

file_system = {
  '/': 0
}
curr_dir = '/'
for cmd in data:
  if cmd.startswith('$ cd'):
    curr_dir = abspath(join(curr_dir, cmd[5:]))
  elif cmd.startswith('dir'):
    file_system[join(curr_dir,cmd[4:])+'/'] = 0
  elif cmd[0] != '$':
    size, name = cmd.split()
    file_system[join(curr_dir,name)] = int(size)

# print(file_system)

directories = [key for key in file_system if key.endswith('/')]
# print(directories)

sizes = sorted(
  [sum([size for name,size in file_system.items() if name.startswith(d)]) for d in directories]
)
# print(sizes)

counter = 0
for size in sizes:
  if size < 100000:
    counter += size

print('part 1', counter)
