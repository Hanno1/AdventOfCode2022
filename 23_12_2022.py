import copy


def get_adjacent_elves(pos, elf_pos):
    adjacent_tiles = [[pos[0] + i, pos[1] + j] for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    for tile in adjacent_tiles:
        if tile in elf_pos:
            return True
    return False


def get_adjacent_elves_direction(pos, direction, elf_pos):
    if direction == "N":
        adjacent_tiles = [[pos[0] - 1, pos[1] + i] for i in range(-1, 2)]
        new_pos = [pos[0] - 1, pos[1]]
    elif direction == "S":
        adjacent_tiles = [[pos[0] + 1, pos[1] + i] for i in range(-1, 2)]
        new_pos = [pos[0] + 1, pos[1]]
    elif direction == "W":
        adjacent_tiles = [[pos[0] + i, pos[1] - 1] for i in range(-1, 2)]
        new_pos = [pos[0], pos[1] - 1]
    else:
        adjacent_tiles = [[pos[0] + i, pos[1] + 1] for i in range(-1, 2)]
        new_pos = [pos[0], pos[1] + 1]
    for tile in adjacent_tiles:
        if tile in elf_pos:
            return pos, False
    return new_pos, True


def get_all_new_elf_pos(elf_pos, move_order):
    new_elf_pos = []
    unique_pos = []
    for position in elf_pos:
        new_position = copy.deepcopy(position)
        # check first condition
        if get_adjacent_elves(position, elf_pos):
            # move the elf
            for direction in move_order:
                new_position, moved_res = get_adjacent_elves_direction(copy.deepcopy(position), direction, elf_pos)
                if moved_res:
                    break
        if new_position in unique_pos:
            new_elf_pos.append(position)
            try:
                index = new_elf_pos.index(new_position)
                new_elf_pos[index] = elf_pos[index]
            except ValueError:
                pass
        else:
            unique_pos.append(copy.deepcopy(new_position))
            new_elf_pos.append(copy.deepcopy(new_position))
    return new_elf_pos


def move_elves_final(turns):
    elf_pos = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == "#":
                elf_pos.append([row, col])
    move_order = ["N", "S", "W", "E"]
    for i in range(turns):
        new_elf_pos = get_all_new_elf_pos(elf_pos, move_order)
        for old_tile in elf_pos:
            mat[old_tile[0]][old_tile[1]] = "."
        for new_tile in new_elf_pos:
            mat[new_tile[0]][new_tile[1]] = "#"
        print(f"Turns: {i}")
        moving_elves = len(elf_pos)
        for counter in range(len(new_elf_pos)):
            if new_elf_pos[counter] == elf_pos[counter]:
                moving_elves -= 1
        print(f"Moving Elves: {moving_elves}")
        for line in mat:
            print(line)
        print("----------------")
        elf_pos = copy.deepcopy(new_elf_pos)
        tmp = move_order.pop(0)
        move_order.append(tmp)


def move_elves_final_2():
    elf_pos = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == "#":
                elf_pos.append([row, col])
    move_order = ["N", "S", "W", "E"]
    turn = 1
    while True:
        print(f"Turn {turn}")
        new_elf_pos = get_all_new_elf_pos(elf_pos, move_order)
        done = True
        for el_counter in range(len(new_elf_pos)):
            if elf_pos[el_counter] != new_elf_pos[el_counter]:
                done = False
                break
        if done:
            print(turn)
            break
        elf_pos = copy.deepcopy(new_elf_pos)
        tmp = move_order.pop(0)
        move_order.append(tmp)
        turn += 1


def count_points():
    top_index = 0
    bot_index = 0
    left_index = 0
    right_index = 0
    # check top
    for row_counter in range(len(mat)):
        line_ = mat[row_counter]
        if line_.count("#") > 0:
            top_index = row_counter
            break
    # check bot
    for row_counter in range(len(mat) - 1, 0, -1):
        line_ = mat[row_counter]
        if line_.count("#") > 0:
            bot_index = row_counter
            break
    # check left
    for col_counter in range(len(mat[0])):
        current_col = [mat[i][col_counter] for i in range(len(mat))]
        if current_col.count("#") > 0:
            left_index = col_counter
            break
    # check right
    for col_counter in range(len(mat[0]) - 1, 0, -1):
        current_col = [mat[i][col_counter] for i in range(len(mat))]
        if current_col.count("#") > 0:
            right_index = col_counter
            break
    new_mat = [mat[i][left_index:right_index + 1] for i in range(top_index, bot_index + 1)]
    return new_mat


padding = 0
mat = []
with open("input.txt") as file:
    for line in file:
        mat.append([c for c in line.replace("\n", "")])

length = len(mat[0])
for line in mat:
    for _ in range(padding):
        line.insert(0, ".")
        line.append(".")
for _ in range(padding):
    mat.insert(0, ["." for _ in range(length + 2 * padding)])
for _ in range(padding):
    mat.append(["." for _ in range(length + 2 * padding)])

# false 929 - too low
# 930 - too low
move_elves_final_2()
# move_elves_final(20)
