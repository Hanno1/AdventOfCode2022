stack_numbers = 9
stacks = [[] for i in range(stack_numbers)]
operations = []

stacks_top = True
with open("input.txt") as file:
    for line in file:
        if stacks_top:
            if line.__contains__('1'):
                stacks_top = False
                continue
            else:
                index = 0
                position = 0
                new_line = line.split(" ")
                while True:
                    if new_line[index:index+4] == ["","","",""]:
                        index += 4
                        position += 1
                    else:
                        stacks[position].append(new_line[index][1])
                        position += 1
                        if new_line[index].__contains__("\n"):
                            break
                        index += 1

        if not stacks_top:
            new_line = line.split(" ")
            if len(new_line) > 5:
                operations.append([new_line[1], new_line[3], new_line[5].replace("\n", "")])

for line in stacks:
    line = line.reverse()

for op in operations:
    number = int(op[0])
    origin = int(op[1])-1
    destination = int(op[2])-1

    """for j in range(number):
        poped = stacks[origin].pop()
        stacks[destination].append(poped)"""

    poped = stacks[origin][-number:]
    for j in range(number):
        stacks[origin].pop()
    for el in poped:
        stacks[destination].append(el)

answer = ""
for line in stacks:
    answer += line[-1]

print(stacks)
print(answer)
