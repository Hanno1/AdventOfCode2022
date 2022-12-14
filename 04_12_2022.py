def task():
    entry_list = []
    with open("input.txt") as file:
        for line in file:
            entry_list.append(line.replace("\n", ""))
    special_pairs = 0
    for line in entry_list:
        first_entry, second_entry = line.split(",")
        first_begin, first_end = first_entry.split("-")
        second_begin, second_end = second_entry.split("-")

        first_begin = int(first_begin)
        first_end = int(first_end)
        second_begin = int(second_begin)
        second_end = int(second_end)

        # first task
        """if int(first_begin) <= int(second_begin) and int(first_end) >= int(second_end):
            special_pairs += 1
        elif int(second_begin) <= int(first_begin) and int(second_end) >= int(first_end):
            special_pairs += 1"""

        # second task
        if first_begin <= second_begin <= first_end or first_begin <= second_end <= first_end:
            special_pairs += 1
        elif first_begin <= second_begin and first_end >= second_end:
            special_pairs += 1
        elif second_begin <= first_begin and second_end >= first_end:
            special_pairs += 1
    print(special_pairs)


task()
