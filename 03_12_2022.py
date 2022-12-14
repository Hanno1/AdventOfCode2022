def task1():
    backpacks = []
    with open("input.txt") as file:
        for line in file:
            backpacks.append(line)

    sum_of_values = 0
    small_order = ord("a")
    big_order = ord("A")
    """for line in backpacks:
        length = len(line) - 1
        first_comp = line[:int(length/2)]
        second_comp = line[int(length/2):]

        joind_chars = []
        for char in first_comp:
            if char in second_comp and char not in joind_chars:
                joind_chars.append(char)

        for c in joind_chars:
            if ord(c) >= 97:
                sum_of_values += 1 + (ord(c)) - small_order
            else:
                sum_of_values += 27 + (ord(c)) - big_order
    print(sum_of_values)"""
    # second task
    triple_line = []
    counter = 0
    for line in backpacks:
        if counter == 3:
            common_char = None
            for l in triple_line[0]:
                if l in triple_line[1] and l in triple_line[2]:
                    common_char = l
                    break
            if ord(common_char) >= 97:
                sum_of_values += 1 + (ord(common_char)) - small_order
            else:
                sum_of_values += 27 + (ord(common_char)) - big_order
            triple_line = []
            counter = 0
        counter += 1
        triple_line.append(line.replace("\n", ""))
    common_char = None
    for l in triple_line[0]:
        if l in triple_line[1] and l in triple_line[2]:
            common_char = l
            break
    if ord(common_char) >= 97:
        sum_of_values += 1 + (ord(common_char)) - small_order
    else:
        sum_of_values += 27 + (ord(common_char)) - big_order
    print(sum_of_values)

task1()
