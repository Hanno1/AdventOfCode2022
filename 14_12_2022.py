import copy

lines = []
with open("input.txt") as file:
    for line in file:
        lines.append(line.replace("\n", "").split("->"))

left_index = 0
matrix = [["." for i in range(left_index, 1000)] for j in range(300)]
max_row = 0
max_column = 0
min_column = 500
for i in range(len(lines)):
    prev_el = None
    for j in range(len(lines[i])):
        first, second = lines[i][j].split(",")
        lines[i][j] = [int(first), int(second)]
        if int(second) > max_row:
            max_row = int(second)
        if int(first) > max_column:
            max_column = int(first)
        if int(first) < min_column:
            min_column = int(first)
        if prev_el is not None:
            current = [int(first), int(second)]
            if abs(prev_el[0] - current[0]) > 0:
                if prev_el[0] > current[0]:
                    for new_i in range(current[0], prev_el[0] + 1):
                        matrix[current[1]][new_i - left_index] = "#"
                elif current[0] > prev_el[0]:
                    for new_i in range(prev_el[0], current[0] + 1):
                        matrix[current[1]][new_i - left_index] = "#"
            elif abs(prev_el[1] - current[1]) > 0:
                if prev_el[1] > current[1]:
                    for new_i in range(current[1], prev_el[1] + 1):
                        matrix[new_i][current[0] - left_index] = "#"
                elif current[1] > prev_el[1]:
                    for new_i in range(prev_el[1], current[1] + 1):
                        matrix[new_i][current[0] - left_index] = "#"
            else:
                matrix[current[1]][current[0] - left_index] = "#"
        prev_el = [int(first), int(second)]

# draw floor
for i in range(min_column - 400, max_column + 400):
    matrix[max_row + 2][i - left_index] = "#"

starting_point = [500, 0]
current_point = copy.deepcopy(starting_point)
moved = False
one_fallen = False
turns = 0
while not one_fallen:
    current_point = copy.deepcopy(starting_point)
    while True:
        moved = False
        if current_point[1] + 1 == len(matrix):
            one_fallen = True
            break
        # move down
        if matrix[current_point[1] + 1][current_point[0] - left_index] == ".":
            current_point[1] += 1
            moved = True
        # move diagonal left
        elif matrix[current_point[1] + 1][current_point[0] - 1 - left_index] == ".":
            current_point[1] += 1
            current_point[0] -= 1
            moved = True
        elif matrix[current_point[1] + 1][current_point[0] + 1 - left_index] == ".":
            current_point[1] += 1
            current_point[0] += 1
            moved = True
        if not moved:
            if current_point[0] == 500 and current_point[1] == 0:
                # exit
                one_fallen = True
                print("HERE!!")
                break
            matrix[current_point[1]][current_point[0] - left_index] = "o"
            """for line in matrix:
                print(line)"""
            break
    turns += 1

print(turns)
