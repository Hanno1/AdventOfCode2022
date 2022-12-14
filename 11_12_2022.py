def increase_worry_lvl(function, value):
    tmp_op = function[0]
    if tmp_op == "+":
        add_value = 0
        for entry in function[1:]:
            if entry == "x":
                add_value += value
            else:
                add_value += entry
        return add_value
    else:
        mult_value = 1
        for entry in function[1:]:
            if entry == "x":
                mult_value *= value
            else:
                mult_value *= entry
        return mult_value


def test_function(function, value):
    divisor = function[1]
    if value % divisor == 0:
        return function[2]
    return function[3]


def print_item_list(items_list_tmp):
    count = 0
    for line_tmp in items_list_tmp:
        print(f"Monkey {count}: ", line_tmp)
        count += 1
    print("--------------------------------")


monkeys = []
with open("input.txt") as file:
    new_monkey = []
    for line in file:
        if "Monkey" in line:
            if new_monkey:
                monkeys.append(new_monkey)
            new_monkey = []
            continue
        if line == "\n":
            continue
        new_monkey.append(line.replace("\n", "").split(":")[1:])

if new_monkey:
    monkeys.append(new_monkey)

items_list = []
for monkey in monkeys:
    string_items = monkey[0][0].split(",")
    actual_items = []
    for item in string_items:
        actual_items.append(int(item))
    items_list.append(actual_items)

operation_list = []
for monkey in monkeys:
    string_operation = monkey[1][0].split("=")[1]
    final_operation = []
    if "+" in string_operation:
        new_string_operation = string_operation.split("+")
        final_operation.append("+")
    else:
        new_string_operation = string_operation.split("*")
        final_operation.append("*")
    for el in new_string_operation:
        if "old" in el:
            final_operation.append("x")
        else:
            final_operation.append(int(el))
    operation_list.append(final_operation)

test_list = []
for monkey in monkeys:
    current_test = ["/", int(monkey[2][0].split(" ")[-1]), int(monkey[3][0].split(" ")[-1]),
                    int(monkey[4][0].split(" ")[-1])]
    test_list.append(current_test)

monkey_dict = dict()
for monkey_index in range(len(monkeys)):
    monkey_dict[monkey_index] = [items_list[monkey_index], operation_list[monkey_index], test_list[monkey_index]]

mod_mult = 7*2*19*3*13*11*5*17
all_rounds = 10000
current_round = 0
all_items = items_list
inspecting_items_counter = [0 for i in range(len(monkey_dict))]
while current_round < all_rounds:
    current_round += 1
    print(f"Round {current_round}")
    for key in monkey_dict:
        # inspection
        monkey = monkey_dict[key]
        monkey_items = monkey[0]
        operation = monkey[1]
        test = monkey[2]
        inspecting_items_counter[key] += len(monkey_items)
        for item in monkey_items:
            # increase worry lvl and decrease it again
            # task 1 result = increase_worry_lvl(operation, item) // 3
            result = increase_worry_lvl(operation, item) % mod_mult
            # test
            test_result = test_function(test, result)
            # throw item
            monkey_dict[test_result][0].append(result)
        monkey_dict[key][0] = []
    # print(print_item_list(inspecting_items_counter))

print(monkey_dict)
print(inspecting_items_counter)

first_max = max(inspecting_items_counter)
inspecting_items_counter.remove(first_max)
second_max = max(inspecting_items_counter)
print(first_max * second_max)

