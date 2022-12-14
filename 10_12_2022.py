cmds = []
with open("input.txt") as file:
    for line in file:
        cmds.append(line.replace("\n", ""))

cycle = 0
value = 1
value_list = []
for cmd in cmds:
    if cmd == "noop":
        cycle += 1
        value_list.append(value)
    else:
        number_to_add = int(cmd.split(" ")[1])
        for i in range(2):
            cycle += 1
            if i == 0:
                value_list.append(value)
        value += number_to_add
        value_list.append(value)


result = ""
result_pos = 0
sprite_middle_pos = 1
for value in value_list:
    if sprite_middle_pos - 1 <= result_pos % 40 <= sprite_middle_pos + 1:
        result += "#"
    else:
        result += "."
    result_pos += 1
    sprite_middle_pos = value

cycle = 40
while True:
    if cycle-1 < len(result):
        print(result[cycle - 40:cycle])
        cycle += 40
    else:
        break

"""sum_of_values = 0
cycle = 20
while True:
    if cycle > 220:
        break
    if cycle - 1 < len(value_list):
        # print(cycle, value_list[cycle - 1])
        sum_of_values += value_list[cycle - 2] * cycle
        cycle += 40
    else:
        break

print(sum_of_values)"""
