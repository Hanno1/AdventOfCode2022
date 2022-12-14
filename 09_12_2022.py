import copy


def move_head_of_rope(direction_tmp, heads, tails):
    if direction_tmp == "R":
        heads[1] += 1
    elif direction_tmp == "L":
        heads[1] -= 1
    elif direction_tmp == "U":
        heads[0] -= 1
    else:
        heads[0] += 1
    return heads, move_rope(heads, tails)


def move_rope(heads, tails):
    head_row = heads[0]
    head_col = heads[1]
    tails_row = tails[0]
    tails_col = tails[1]

    if head_row == tails_row + 2:
        tails[0] += 1
        if tails_col == head_col - 1 or tails_col == head_col - 2:
            tails[1] += 1
        elif tails_col == head_col + 1 or tails_col == head_col + 2:
            tails[1] -= 1
    elif head_row == tails_row - 2:
        tails[0] -= 1
        if tails_col == head_col - 1 or tails_col == head_col - 2:
            tails[1] += 1
        elif tails_col == head_col + 1 or tails_col == head_col + 2:
            tails[1] -= 1
    elif head_row == tails_row:
        if tails_col == head_col - 2:
            tails[1] += 1
        elif tails_col == head_col + 2:
            tails[1] -= 1
    elif head_row == tails_row - 1:
        if tails_col == head_col - 2:
            tails[1] += 1
            tails[0] -= 1
        elif tails_col == head_col + 2:
            tails[1] -= 1
            tails[0] -= 1
    elif head_row == tails_row + 1:
        if tails_col == head_col - 2:
            tails[1] += 1
            tails[0] += 1
        elif tails_col == head_col + 2:
            tails[1] -= 1
            tails[0] += 1
    return tails


def display_matrix(matrix):
    for row in matrix:
        string_row = ""
        for col in row:
            string_row += col
        print(string_row)


commands = []
with open("input.txt") as file:
    for line in file:
        commands.append(line.replace("\n", "").split(" "))

# task 1
"""head_position = [5, 5]
tail_position = [5, 5]

positions = [[5, 5]]

#mat = [["." for i in range(-10, 10)] for j in range(-10, 10)]
#mat[tail_position[0]][tail_position[1]] = "s"

direction = None
steps_remaining = 0
for cmd in commands:
    direction = cmd[0]
    steps_remaining = int(cmd[1])
    for step in range(steps_remaining):
        head_position, tail_position = move_rope(direction, head_position, tail_position)

        add = True
        for el in positions:
            if tail_position[0] == el[0] and tail_position[1] == el[1]:
                add = False
                break
        if add:
            positions.append(copy.deepcopy(tail_position))
            # mat[tail_position[0]][tail_position[1]] = "#"
        #display_matrix(mat)
        #print("------------------------------")

print(len(positions))"""

# task 2
positions = [[0, 0]]
rope_positions = [[0, 0] for i in range(10)]
direction = None
steps_remaining = 0
for cmd in commands:
    direction = cmd[0]
    steps_remaining = int(cmd[1])
    for step in range(steps_remaining):
        # move all parts of the rope:
        # move the head
        rope_positions[0], rope_positions[1] = move_head_of_rope(direction, rope_positions[0], rope_positions[1])

        # move the rest after it
        for i in range(2, len(rope_positions)):
            early_position = copy.deepcopy(rope_positions[i])
            rope_positions[i] = move_rope(rope_positions[i - 1], rope_positions[i])
            if early_position[0] == rope_positions[0] and early_position[1] == rope_positions[1]:
                break
        tail_position = rope_positions[-1]
        add = True
        for el in positions:
            if tail_position[0] == el[0] and tail_position[1] == el[1]:
                add = False
                break
        if add:
            positions.append(copy.deepcopy(tail_position))

print(len(positions))
