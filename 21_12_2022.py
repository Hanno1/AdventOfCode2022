import copy
from sympy import *


def rek_monkeys_1(current_monkey):
    dict_entry = copy_dict[current_monkey]
    if len(dict_entry) == 1:
        return dict_entry[0]
    if dict_entry[0] == "=":
        solution = rek_monkeys_1(dict_entry[1]) + rek_monkeys_1(dict_entry[2])
        copy_dict[current_monkey] = solution
        return solution
    if dict_entry[0] == "+":
        solution = rek_monkeys_1(dict_entry[1]) + rek_monkeys_1(dict_entry[2])
        copy_dict[current_monkey] = solution
        return solution
    if dict_entry[0] == "-":
        solution = rek_monkeys_1(dict_entry[1]) - rek_monkeys_1(dict_entry[2])
        copy_dict[current_monkey] = solution
        return solution
    elif dict_entry[0] == "*":
        solution = rek_monkeys_1(dict_entry[1]) * rek_monkeys_1(dict_entry[2])
        copy_dict[current_monkey] = solution
        return solution
    elif dict_entry[0] == "/":
        solution = rek_monkeys_1(dict_entry[1]) / rek_monkeys_1(dict_entry[2])
        copy_dict[current_monkey] = solution
        return solution


def rek_monkeys_2(current_monkey):
    dict_entry = copy_dict[current_monkey]
    if current_monkey in visited:
        if len(dict_entry) == 1:
            return dict_entry[0]
        return copy_dict[current_monkey]
    if current_monkey == "humn":
        visited.append(current_monkey)
        copy_dict[current_monkey] = ["x"]
        return "x"
    if len(dict_entry) == 1:
        visited.append(current_monkey)
        copy_dict[current_monkey] = dict_entry
        return dict_entry[0]
    res_1 = rek_monkeys_2(dict_entry[1])
    res_2 = rek_monkeys_2(dict_entry[2])
    compute = False
    if (type(res_1) == int or type(res_1) == float) and (type(res_2) == int or type(res_2) == float):
        compute = True
    if dict_entry[0] == "=":
        if compute:
            solution = (res_1 == res_2)
        else:
            solution = ["=", res_1, res_2]
    elif dict_entry[0] == "+":
        if compute:
            solution = res_1 + res_2
        else:
            solution = ["+", res_1, res_2]
    elif dict_entry[0] == "-":
        if compute:
            solution = res_1 - res_2
        else:
            solution = ["-", res_1, res_2]
    elif dict_entry[0] == "*":
        if compute:
            solution = res_1 * res_2
        else:
            solution = ["*", res_1, res_2]
    else:
        if compute:
            solution = res_1 / res_2
        else:
            solution = ["/", res_1, res_2]
    visited.append(current_monkey)
    copy_dict[current_monkey] = solution
    return solution


def bracket_equation_to_string_rek(current_expression):
    if type(current_expression) == int or type(current_expression) == float or current_expression == "x":
        return current_expression
    left_op = bracket_equation_to_string_rek(current_expression[1])
    right_op = bracket_equation_to_string_rek(current_expression[2])
    operation = current_expression[0]
    if operation == "+":
        return f"({left_op}+{right_op})"
    if operation == "*":
        return f"({left_op}*{right_op})"
    if operation == "-":
        return f"({left_op}-{right_op})"
    if operation == "/":
        return f"({left_op}/{right_op})"
    else:
        print(f"Unknown Operation {operation}")
        raise ValueError


monkey_dict = dict()
possible_actions = ["*", "+", "/", "-"]
with open("input.txt") as file:
    for line in file:
        actual_line = line.replace("\n", "")
        actual_line_split = actual_line.split(":")
        monkey_name = actual_line_split[0]
        if monkey_name == "root":
            computation = ["=", actual_line_split[1].split("+")[0].replace(" ", ""),
                           actual_line_split[1].split("+")[1].replace(" ", "")]
            monkey_dict[monkey_name] = computation
            continue
        elif monkey_name == "humn":
            computation = ["~"]
            monkey_dict[monkey_name] = computation
            continue
        computation = []
        try:
            computation.append(int(actual_line_split[1]))
        except Exception:
            for action in possible_actions:
                if action in actual_line_split[1]:
                    computation = [action, actual_line_split[1].split(action)[0].replace(" ", ""),
                                   actual_line_split[1].split(action)[1].replace(" ", "")]
                    break
        monkey_dict[monkey_name] = computation

# print(monkey_dict)
copy_dict = copy.deepcopy(monkey_dict)
visited = []

eq = rek_monkeys_2("root")
print(eq)

s1 = bracket_equation_to_string_rek(eq[1])
s2 = bracket_equation_to_string_rek(eq[2])

x = symbols("x")

sol = solve(str(s1) + "-" + str(s2), x)
print(sol)
