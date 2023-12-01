def draw_blizzards():
    for bliz in blizzards_up:
        matrix[bliz[0]][bliz[1]] = "^"
    for bliz in blizzards_down:
        if matrix[bliz[0]][bliz[1]] == "^":
            matrix[bliz[0]][bliz[1]] = "2"
        else:
            matrix[bliz[0]][bliz[1]] = "v"
    for bliz in blizzards_left:
        if matrix[bliz[0]][bliz[1]] == "2":
            matrix[bliz[0]][bliz[1]] = "3"
        elif matrix[bliz[0]][bliz[1]] == "^" or matrix[bliz[0]][bliz[1]] == "v":
            matrix[bliz[0]][bliz[1]] = "2"
        else:
            matrix[bliz[0]][bliz[1]] = "<"
    for bliz in blizzards_right:
        if matrix[bliz[0]][bliz[1]] == "2":
            matrix[bliz[0]][bliz[1]] = "3"
        if matrix[bliz[0]][bliz[1]] == "3":
            matrix[bliz[0]][bliz[1]] = "4"
        elif matrix[bliz[0]][bliz[1]] == "^" or matrix[bliz[0]][bliz[1]] == "v" or matrix[bliz[0]][bliz[1]] == "<":
            matrix[bliz[0]][bliz[1]] = "2"
        else:
            matrix[bliz[0]][bliz[1]] = ">"
    print("---------------------------------")
    for line in matrix:
        print(line)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):
            matrix[row][col] = "."


def move_blizzards():
    # move all up
    for tmp_counter in range(len(blizzards_up)):
        tmp = blizzards_up[tmp_counter]
        tmp[0] -= 1
        if tmp[0] == 1:
            tmp[0] = len(matrix) - 2
        blizzards_up[tmp_counter] = tmp

    # move all down
    for tmp_counter in range(len(blizzards_down)):
        tmp = blizzards_down[tmp_counter]
        tmp[0] += 1
        if tmp[0] == len(matrix) - 1:
            tmp[0] = 1
        blizzards_down[tmp_counter] = tmp

    # move all right
    for tmp in blizzards_right:
        tmp[1] += 1
        if tmp[1] == len(matrix[0]) - 1:
            tmp[1] = 1

    # move all left
    for tmp in blizzards_left:
        tmp[1] -= 1
        if tmp[1] == 0:
            tmp[1] = len(matrix) - 2


def move_player(pos_):
    current_row, current_col = pos_
    new_pos_ = [[current_row, current_col], [current_row - 1, current_col], [current_row + 1, current_col],
                [current_row, current_col - 1], [current_row, current_col + 1]]
    actual_pos = []
    for pos in new_pos_:
        if matrix[pos[0]][pos[1]] != "#" and 0 <= pos[0] <= len(matrix) - 1 and 0 <= pos[1] <= len(matrix[0]) - 1:
            actual_pos.append(pos)
    return actual_pos


matrix = []
with open("input.txt") as file:
    for line in file:
        actual_line = line.replace("\n", "")
        matrix.append([c for c in actual_line])

current_pos = []
for col in range(len(matrix[0])):
    if matrix[0][col] == "E":
        current_pos = [[0, col]]
        break

blizzards_up = []
blizzards_down = []
blizzards_left = []
blizzards_right = []
for row in range(1, len(matrix) - 1):
    for col in range(1, len(matrix[0]) - 1):
        entry = matrix[row][col]
        if entry == "v":
            blizzards_down.append([row, col])
        elif entry == "^":
            blizzards_up.append([row, col])
        elif entry == "<":
            blizzards_left.append([row, col])
        elif entry == ">":
            blizzards_right.append([row, col])
        matrix[row][col] = "."

turns = 20

draw_blizzards()
done = False
for turn in range(turns):
    print(f"turn: {turn}")
    move_blizzards()

    new_current_pos = []
    for position in current_pos:
        new_pos = move_player(position)
        for p in new_pos:
            if p not in blizzards_down and p not in blizzards_up and p not in blizzards_left and \
                    p not in blizzards_right and p not in new_current_pos:
                new_current_pos.append(p)
                if matrix[p[0]][p[1]] == "A":
                    print(f"DONE: {turn}")
                    done = True
                    break
    print("............................")
    for pos in current_pos:
        print(pos)
    current_pos = new_current_pos
    if done:
        break
