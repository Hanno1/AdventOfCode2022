def task_1():

    dict_single = {"X": 1, "Y": 2, "Z": 3}
    dict_double = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6,
                   "C X": 6, "C Y": 0, "C Z": 3}
    dict_second_task = {"A X": "Z", "A Y": "X", "A Z": "Y", "B X": "X", "B Y": "Y", "B Z": "Z",
                   "C X": "Y", "C Y": "Z", "C Z": "X"}

    l = []
    with open("input.txt", "r") as file:
        for line in file:
            l.append(line.split("\n")[0])

    sum_of_points = 0
    # task 1
    """for line in l:
        sum_of_points += dict_double[line]
        sum_of_points += dict_single[line.split(" ")[1]]"""
    # print(sum_of_points)

    # task 2
    for line in l:
        oponent, me = line.split(" ")
        sum_of_points += dict_single[dict_second_task[line]]
        if me == "X":
            # we need to lose
            pass
        elif me == "Y":
            # draw
            sum_of_points += 3
        else:
            # win
            sum_of_points += 6
    print(sum_of_points)


task_1()
