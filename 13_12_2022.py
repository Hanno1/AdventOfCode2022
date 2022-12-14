import ast
import copy


def compare_lines_rek(left_line, right_line):
    left_index = 0
    right_index = 0

    if not left_line:
        return 1
    for el in left_line:
        if left_index >= len(left_line):
            return 1
        elif right_index >= len(right_line):
            return -1
        if type(el) == list and type(right_line[right_index]) == list:
            result = compare_lines_rek(el, right_line[right_index])
            if result == -1 or result == 1:
                return result
        elif type(el) == int and type(right_line[right_index]) == int:
            if el < right_line[right_index]:
                return 1
            elif el > right_line[right_index]:
                return -1
        elif type(el) == int and type(right_line[right_index]) == list:
            result = compare_lines_rek([el], right_line[right_index])
            if result == -1 or result == 1:
                return result
        elif type(el) == list and type(right_line[right_index]) == int:
            result = compare_lines_rek(el, [right_line[right_index]])
            if result == -1 or result == 1:
                return result
        left_index += 1
        right_index += 1
    if len(left_line) < len(right_line):
        return 1
    return 0


commands = []
second_turn = []
with open("input.txt") as file:
    left = []
    right = []
    left_turn = True
    for line in file:
        if line == "\n":
            left = []
            right = []
            left_turn = True
            continue
        second_turn.append(ast.literal_eval(line.replace("\n", "")))
        """elif left_turn:
            left = ast.literal_eval(line.replace("\n", ""))
            left_turn = False
        else:
            right = ast.literal_eval(line.replace("\n", ""))
            commands.append([left, right])"""

"""print(commands)

index_counter = 1
result = 0
for left, right in commands:
    left_index = 0
    right_index = 0
    res = compare_lines_rek(left, right)
    if res == 1:
        result += index_counter
    elif res == 0:
        print(index_counter)
    index_counter += 1

print(result)"""
second_turn.append([[2]])
second_turn.append([[6]])

adj_mat = [[-2 for i in range(len(second_turn))] for j in range(len(second_turn))]

# find longest element
maxi_index = 0
for i in range(len(second_turn)):
    for j in range(i+1, len(second_turn)):
        res = compare_lines_rek(second_turn[i], second_turn[j])
        adj_mat[i][j] = res
        adj_mat[j][i] = -res

one_counter = 0
one_index = 0
for line_counter in range(len(adj_mat)):
    line = adj_mat[line_counter]
    tmp_ones = line.count(1)
    if tmp_ones > one_counter:
        one_counter = tmp_ones
        one_index = line_counter


# one_index leads the first list -> search for biggest list
ordering = [one_index]
while True:
    one_counter = -1
    one_index = -1
    last_el = ordering[-1]
    found_one = False
    for line_counter in range(len(adj_mat)):
        if adj_mat[last_el][line_counter] == -1 or line_counter in ordering:
            continue
        line = adj_mat[line_counter]
        tmp_ones = line.count(1)
        if tmp_ones > one_counter:
            one_counter = tmp_ones
            one_index = line_counter
            found_one = True
    if not found_one:
        break
    ordering.append(one_index)

first_ind = -1
second_ind = -1
counter = 1
for index in ordering:
    if second_turn[index] == [[2]]:
        first_ind = counter
    if second_turn[index] == [[6]]:
        second_ind = counter
    counter += 1

print(first_ind)
print(second_ind)
print(first_ind * second_ind)
