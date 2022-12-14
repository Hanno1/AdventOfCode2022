lines = []

directory_sizes = dict()
sub_directories = dict()

count = 0
stack = ["/"]

with open("input.txt") as file:
    all_dirs = []
    current_dir = stack[0]
    for line in file:
        if line[0] == "$" and line[2:4] == "cd" and not line.__contains__(".."):
            all_dirs.reverse()
            for entry in all_dirs:
                stack.append(entry)
            all_dirs = []

            name = stack.pop(-1)
            current_name = name

            directory_sizes[name] = 0
            sub_directories[name] = []
            lines.append("$ cd " + name)

            continue
        elif line[0:3] == "dir":
            name = line.replace("\n", "").split(" ")[1]
            new_name = name + "_" + str(count)
            count += 1

            all_dirs.append(new_name)
            sub_directories[current_name].append(new_name)
            lines.append("dir " + new_name)
            continue
        lines.append(line.replace("\n", ""))

count = 0
read = False
current_dir = None
for line in lines:
    if line[0] == "$":
        read = False
    if line[0] == "$" and not read and line[2:4] == "cd":
        current_dir = line.split(" ")[2]
    elif line[0] == "$" and not read and line[2:4] == "ls":
        read = True
    else:
        if read:
            file = line.split(" ")
            if not file[0] == "dir":
                directory_sizes[current_dir] += int(file[0])
            else:
                # sub_directories[current_dir].append(file[1])
                pass


def rek(current_dir, directory_sizes, sub_directories, already_computed):
    subs = sub_directories[current_dir]
    if subs:
        for sub in subs:
            if sub in already_computed:
                directory_sizes[current_dir] += already_computed[already_computed[sub]]
            else:
                res = rek(sub, directory_sizes, sub_directories, already_computed)
                directory_sizes[current_dir] += res
                already_computed[sub] = res
        return directory_sizes[current_dir]
    else:
        return directory_sizes[current_dir]


print(sub_directories)
print(directory_sizes)
rek("/", directory_sizes, sub_directories, dict())
print(directory_sizes)

# task 1
"""total_sum = 0
for entry in directory_sizes:
    if directory_sizes[entry] <= 100000:
        total_sum += directory_sizes[entry]

print(total_sum)"""

# task 2
total_space = 70000000
needed_space = 30000000

occupied_space = total_space - directory_sizes["/"]

print(occupied_space)

have_to_delete_size = needed_space - occupied_space
print(have_to_delete_size)

mini = total_space
mini_dir = None

for key in directory_sizes:
    entry = directory_sizes[key]
    if have_to_delete_size <= entry < mini:
        mini = entry
        mini_dir = key

print(mini)
print(mini_dir)
