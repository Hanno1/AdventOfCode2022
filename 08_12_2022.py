mat = []
with open("input.txt") as file:
    for line in file:
        new_mat = [int(c) for c in line.replace("\n", "")]
        mat.append(new_mat)

# task 1
"""visible_trees_sides = []
for row in range(len(mat)):
    biggest_element = -1
    for col in range(len(mat[0])):
        current_element = mat[row][col]
        if current_element > biggest_element:
            biggest_element = current_element
            visible_trees_sides.append((row, col))
            if biggest_element == 9:
                break
    biggest_element = -1
    for col in range(len(mat[0])-1, -1, -1):
        current_element = mat[row][col]
        if visible_trees_sides.__contains__((row, col)):
            biggest_element = current_element
            break
        if current_element > biggest_element:
            biggest_element = current_element
            visible_trees_sides.append((row, col))
            if biggest_element == 9:
                break

visible_trees_cols = []
for col in range(len(mat[0])):
    biggest_element = -1
    for row in range(len(mat)):
        current_element = mat[row][col]

        if visible_trees_cols.__contains__((row, col)):
            biggest_element = current_element
            break
        if current_element > biggest_element:
            biggest_element = current_element
            visible_trees_cols.append((row, col))
            if biggest_element == 9:
                break
    biggest_element = -1
    for row in range(len(mat)-1, -1, -1):
        current_element = mat[row][col]
        if visible_trees_cols.__contains__((row, col)):
            biggest_element = current_element
            break
        if current_element > biggest_element:
            biggest_element = current_element
            visible_trees_cols.append((row, col))
            if biggest_element == 9:
                break


visible_trees = len(visible_trees_cols) + len(visible_trees_sides)
for el in visible_trees_sides:
    if el in visible_trees_cols:
        visible_trees -= 1

print(visible_trees)"""


def check_directions(tmp_row, tmp_col, matrix):
    height = matrix[tmp_row][tmp_col]
    # check left
    left_vis = 0
    for c in range(tmp_col - 1, -1, -1):
        left_vis += 1
        if matrix[tmp_row][c] >= height:
            break
    # check right
    right_vis = 0
    for c in range(tmp_col + 1, len(matrix[0])):
        right_vis += 1
        if matrix[tmp_row][c] >= height:
            break
    # check up
    up_vis = 0
    for r in range(tmp_row - 1, -1, -1):
        up_vis += 1
        if matrix[r][tmp_col] >= height:
            break
    # check down
    down_vis = 0
    for r in range(tmp_row + 1, len(mat[0])):
        down_vis += 1
        if matrix[r][tmp_col] >= height:
            break
    return up_vis * left_vis * right_vis * down_vis

# task 2
maxi = 0
for row in range(1, len(mat) - 1):
    for col in range(1, len(mat[0]) - 1):
        check = check_directions(row, col, mat)
        if check > maxi:
            maxi = check

print(maxi)
