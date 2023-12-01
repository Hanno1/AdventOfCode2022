def snafu_to_decimal(snafu_number):
    base = 5
    exon = 0
    result = 0
    for i in range(len(snafu_number) - 1, -1, -1):
        c = snafu_number[i]
        try:
            actual_number = int(c)
            result += actual_number * base**exon
        except ValueError:
            if c == "=":
                result += -2 * base ** exon
            else:
                result -= base ** exon
        exon += 1
    return result


def decimal_to_snafu(decimal_number):
    new_number = []
    # the idea is that if we get a 3 or 4 we look at the previous number and go higher
    current_number = decimal_number
    while current_number > 0:
        mod = current_number % 5
        if mod == 3:
            mod = -2
        elif mod == 4:
            mod = -1
        current_number = (current_number - mod) // 5
        if 0 <= mod <= 2:
            new_number.append(str(mod))
        else:
            if mod == -1:
                new_number.append("-")
            else:
                new_number.append("=")
    new_number.reverse()
    return new_number


snafu_numbers = []
with open("input.txt") as file:
    for line in file:
        snafu_numbers.append([c for c in line.replace("\n", "")])

sum_ = 0
for number in snafu_numbers:
    sum_ += snafu_to_decimal(number)

print(sum_)
l = decimal_to_snafu(sum_)
new_string = ""
for c in l:
    new_string += c
print(new_string)
