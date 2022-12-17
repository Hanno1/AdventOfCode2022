import copy


def display_matrix(matrix_tmp):
    for line_tmp in matrix_tmp:
        print(line_tmp)


def move_rock_left(current_matrix_tmp, all_rock_positions_tmp):
    new_rock_positions = []
    current_matrix_copy = copy.deepcopy(current_matrix_tmp)

    # move all tiles
    for tile in all_rock_positions_tmp:
        new_tile = (tile[0], tile[1] - 1)
        # we hit a rock or we are out of the chamber
        if new_tile[1] < 0 or current_matrix_tmp[new_tile[0]][new_tile[1]] == "#":
            return current_matrix_tmp, all_rock_positions_tmp
        else:
            new_rock_positions.append(new_tile)
            current_matrix_copy[new_tile[0]][new_tile[1]] = "@"
            current_matrix_copy[tile[0]][tile[1]] = "."
    return current_matrix_copy, new_rock_positions


def move_rock_right(current_matrix_tmp, all_rock_positions_tmp):
    new_rock_positions = []
    current_matrix_copy = copy.deepcopy(current_matrix_tmp)

    # move all tiles
    for tile in all_rock_positions_tmp:
        new_tile = (tile[0], tile[1] + 1)
        # we hit a rock or we are out of the chamber
        if new_tile[1] >= 7 or current_matrix_tmp[new_tile[0]][new_tile[1]] == "#":
            return current_matrix_tmp, all_rock_positions_tmp
        else:
            new_rock_positions.append(new_tile)
            current_matrix_copy[new_tile[0]][new_tile[1]] = "@"
            current_matrix_copy[tile[0]][tile[1]] = "."
    return current_matrix_copy, new_rock_positions


def move_rock_down(current_matrix_tmp, all_rock_positions_tmp):
    new_rock_positions = []
    current_matrix_copy = copy.deepcopy(current_matrix_tmp)

    # move all tiles
    for tile in all_rock_positions_tmp:
        new_tile = (tile[0] + 1, tile[1])
        # we hit a rock or we are at the end
        if new_tile[0] == len(current_matrix_tmp) or current_matrix_tmp[new_tile[0]][new_tile[1]] == "#":
            # set tiles to "#"
            for x_pos, y_pos in all_rock_positions_tmp:
                current_matrix_tmp[x_pos][y_pos] = "#"
            return current_matrix_tmp, None, len(current_matrix_tmp) - all_rock_positions_tmp[0][0]
        else:
            new_rock_positions.append(new_tile)
            current_matrix_copy[new_tile[0]][new_tile[1]] = "@"
            current_matrix_copy[tile[0]][tile[1]] = "."
    return current_matrix_copy, new_rock_positions, None


jet_stream = []
jet_stream_index = 0
with open("input.txt") as file:
    for line in file:
        jet_stream = line.replace("\n", "")

current_rock_index = 0
rocks = [[[["@", "@", "@", "@"]], [(0, 2), (0, 3), (0, 4), (0, 5)]],
         [[[".", "@", ".", "."],
           ["@", "@", "@", "."],
           [".", "@", ".", "."]], [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)]],
         [[[".", ".", "@", "."],
           [".", ".", "@", "."],
           ["@", "@", "@", "."]], [(0, 4), (1, 4), (2, 2), (2, 3), (2, 4)]],
         [[["@", ".", ".", "."],
           ["@", ".", ".", "."],
           ["@", ".", ".", "."],
           ["@", ".", ".", "."]], [(0, 2), (1, 2), (2, 2), (3, 2)]],
         [[["@", "@", ".", "."],
           ["@", "@", ".", "."]], [(0, 2), (0, 3), (1, 2), (1, 3)]]]

simulation_steps = 1000000000000

current_matrix = []
current_tower_height = 0

visited_signatures = []
visited_signatures_add_values = []

count_height_outside = 0

cut_index = 100


def get_signature_matrix(matrix_tmp):
    return matrix_tmp[0:cut_index]


new_simulation = 0
for s in range(simulation_steps):

    print(f"Simulation step: {s}")

    rock = rocks[current_rock_index][0]
    rock_height = len(rock)

    height_over_top = len(current_matrix) - current_tower_height

    if height_over_top <= 3:
        for _ in range(3 - height_over_top):
            current_matrix.insert(0, ["." for _ in range(7)])
    else:
        for _ in range(height_over_top - 3):
            current_matrix.pop(0)
    for _ in range(rock_height):
        current_matrix.insert(0, ["." for _ in range(7)])

    if len(current_matrix) > cut_index:
        count_height_outside += len(current_matrix) - cut_index
        current_tower_height = current_tower_height - (len(current_matrix) - cut_index)
        current_matrix = get_signature_matrix(current_matrix)

        new_entry = (current_rock_index, jet_stream_index, current_matrix)
        if new_entry in visited_signatures:
            new_entry_index = visited_signatures.index(new_entry)
            height_diff = (count_height_outside + current_tower_height) - visited_signatures_add_values[new_entry_index][1]
            sim_diff = s - visited_signatures_add_values[new_entry_index][0]
            repeat = simulation_steps - s
            repeat_for = repeat // sim_diff

            count_height_outside += repeat_for * height_diff
            new_simulation = simulation_steps - (repeat % sim_diff)
            print(f"New Simulation {s}")
            break
        else:
            visited_signatures.append(new_entry)
            visited_signatures_add_values.append((s, count_height_outside + current_tower_height))

    all_rock_positions = rocks[current_rock_index][1]
    current_rock_index = (current_rock_index + 1) % 5

    while all_rock_positions:
        stream = jet_stream[jet_stream_index]
        jet_stream_index = (jet_stream_index + 1) % len(jet_stream)

        if stream == "<":
            current_matrix, all_rock_positions = move_rock_left(current_matrix, all_rock_positions)
        else:
            current_matrix, all_rock_positions = move_rock_right(current_matrix, all_rock_positions)
        current_matrix, all_rock_positions, tile_height = move_rock_down(current_matrix, all_rock_positions)
        if tile_height and tile_height > current_tower_height:
            current_tower_height = tile_height


for s in range(new_simulation, simulation_steps):

    print(f"Simulation step: {s}")

    rock = rocks[current_rock_index][0]
    rock_height = len(rock)

    height_over_top = len(current_matrix) - current_tower_height

    if height_over_top <= 3:
        for _ in range(3 - height_over_top):
            current_matrix.insert(0, ["." for _ in range(7)])
    else:
        for _ in range(height_over_top - 3):
            current_matrix.pop(0)
    for _ in range(rock_height):
        current_matrix.insert(0, ["." for _ in range(7)])

    if len(current_matrix) > cut_index:
        count_height_outside += len(current_matrix) - cut_index
        current_tower_height = current_tower_height - (len(current_matrix) - cut_index)
        current_matrix = get_signature_matrix(current_matrix)

    all_rock_positions = rocks[current_rock_index][1]
    current_rock_index = (current_rock_index + 1) % 5

    while all_rock_positions:
        stream = jet_stream[jet_stream_index]
        jet_stream_index = (jet_stream_index + 1) % len(jet_stream)

        if stream == "<":
            current_matrix, all_rock_positions = move_rock_left(current_matrix, all_rock_positions)
        else:
            current_matrix, all_rock_positions = move_rock_right(current_matrix, all_rock_positions)
        current_matrix, all_rock_positions, tile_height = move_rock_down(current_matrix, all_rock_positions)
        if tile_height and tile_height > current_tower_height:
            current_tower_height = tile_height

# 1530232558115 too high
# 1525364431487 -> maybe (50)
# 1525364431487 (60)
# 1525364431487 (100)
print(count_height_outside + current_tower_height)
