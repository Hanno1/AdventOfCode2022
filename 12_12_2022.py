matrix = []
start_pos = []
end_position = []
row_count = 0
path_length_matrix = []

current_heads = []

with open("input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        row = []
        path_length_row = []
        col_count = 0
        for char in line:
            if char == "S":
                start_pos = [row_count, col_count]
                row.append(ord("a") - 97)
                path_length_row.append(0)
                current_heads.append(start_pos)
            elif char == "E":
                end_position = [row_count, col_count]
                row.append(ord("z") - 97)
                path_length_row.append(-1)
            elif char == "a":
                row.append(ord("a") - 97)
                path_length_row.append(0)
                current_heads.append([row_count, col_count])
            else:
                row.append(ord(char) - 97)
                path_length_row.append(-1)
            col_count += 1
        row_count += 1
        matrix.append(row)
        path_length_matrix.append(path_length_row)


def search_one_position(current_position):
    current_row = current_position[0]
    current_col = current_position[1]
    pathlength = path_length_matrix[current_row][current_col]
    current_tile = matrix[current_row][current_col]

    new_positions = []

    # move left
    if current_col != 0:
        left_tile = matrix[current_row][current_col-1]
        if left_tile - 1 <= current_tile:
            new_position = [current_row, current_col-1]
            entry = path_length_matrix[new_position[0]][new_position[1]]
            if entry != -1:
                if pathlength + 1 < entry:
                    path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                    new_positions.append(new_position)
            else:
                path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                new_positions.append(new_position)
    if current_col != len(matrix[0])-1:
        right_tile = matrix[current_row][current_col+1]
        if right_tile - 1 <= current_tile:
            new_position = [current_row, current_col+1]
            entry = path_length_matrix[new_position[0]][new_position[1]]
            if entry != -1:
                if pathlength + 1 < entry:
                    path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                    new_positions.append(new_position)
            else:
                path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                new_positions.append(new_position)
    if current_row != 0:
        right_tile = matrix[current_row-1][current_col]
        if right_tile - 1 <= current_tile:
            new_position = [current_row-1, current_col]
            entry = path_length_matrix[new_position[0]][new_position[1]]
            if entry != -1:
                if pathlength + 1 < entry:
                    path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                    new_positions.append(new_position)
            else:
                path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                new_positions.append(new_position)
    if current_row != len(matrix)-1:
        right_tile = matrix[current_row+1][current_col]
        if right_tile - 1 <= current_tile:
            new_position = [current_row+1, current_col]
            entry = path_length_matrix[new_position[0]][new_position[1]]
            if entry != -1:
                if pathlength + 1 < entry:
                    path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                    new_positions.append(new_position)
            else:
                path_length_matrix[new_position[0]][new_position[1]] = pathlength + 1
                new_positions.append(new_position)
    return new_positions


def breadth_first_search(current_heads):
    while current_heads:
        current_head = current_heads[0]
        new_positions = search_one_position(current_head)
        for position in new_positions:
            if position[0] == end_position[0] and position[1] == end_position[1]:
                current_heads = []
                print(path_length_matrix[end_position[0]][end_position[1]])
                break
            else:
                current_heads.append(position)
        if current_heads:
            current_heads.pop(0)


print(current_heads)
breadth_first_search(current_heads)
"""for row in path_length_matrix:
    print(row)"""
