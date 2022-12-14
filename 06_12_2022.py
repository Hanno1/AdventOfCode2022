def check_double(list_of_chars):
    for i in range(len(list_of_chars)):
        for j in range(i+1, len(list_of_chars)):
            if list_of_chars[i] == list_of_chars[j]:
                return False
    return True


global_line = None
with open("input.txt") as file:
    for line in file:
        global_line = line

chars = []
position = 0
for c in global_line:
    if len(chars) < 14:
        chars.append(c)
        if len(chars) == 14 and check_double(chars):
            break
    elif len(chars) == 14:
        chars.pop(0)
        chars.append(c)
        if check_double(chars):
            print(c)
            break
    position += 1
print(position + 1)
