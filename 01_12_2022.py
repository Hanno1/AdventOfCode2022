def task_1():
    snack_list = []
    with open("input.txt", "r") as file:
        summe = 0
        for line in file:
            if line == "\n":
                snack_list.append(summe)
                summe = 0
            else:
                summe += int(line.split("\n")[0])
    # task 1.1
    maxi = max(snack_list)
    print(maxi)

    # solution task 1.2
    sum_maxi = maxi
    snack_list.remove(maxi)
    sum_maxi += max(snack_list)
    snack_list.remove(max(snack_list))
    sum_maxi += max(snack_list)
    print(sum_maxi)


task_1()
