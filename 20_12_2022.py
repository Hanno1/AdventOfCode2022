import copy


numbers_list = []
orders = []
with open("input.txt") as file:
    for line in file:
        numbers_list.append(int(line.replace("\n", "")) * 811589153)

list_length = len(numbers_list) - 1
# change duplicates
unique_elements = []
for el in numbers_list:
    if el not in unique_elements:
        unique_elements.append(el)

unique_elements_check = copy.deepcopy(unique_elements)

new_els_old_els = []
for unique_el in unique_elements:
    multiplication = list_length
    index = 0
    for el_counter in range(len(numbers_list)):
        el = numbers_list[el_counter]
        if el == unique_el:
            if index == 0:
                # first element
                index += 1
            else:
                new_element = unique_el + index * multiplication
                while new_element in unique_elements_check:
                    multiplication += list_length
                    new_element = unique_el + index * multiplication
                multiplication += list_length
                index += 1
                new_els_old_els.append([new_element, unique_el])
                numbers_list[el_counter] = new_element
                unique_elements_check.append(new_element)

orders = copy.deepcopy(numbers_list)
# print(numbers_list)
for i in range(10):
    for order_el in orders:
        # print(f"Element {order_el}, current list {numbers_list}")
        if order_el == 0:
            continue
        current_index = numbers_list.index(order_el)
        numbers_list.remove(order_el)
        if order_el > 0:
            for number in range(order_el % list_length):
                if current_index == list_length:
                    current_index = 0
                current_index += 1
        else:
            for number in range((-order_el) % list_length):
                if current_index == 0:
                    current_index = list_length
                current_index -= 1
        numbers_list.insert(current_index, order_el)

# change back
for new_el, old_el in new_els_old_els:
    index = numbers_list.index(new_el)
    numbers_list[index] = old_el

print(numbers_list)

current_index = numbers_list.index(0)
steps = 1000 % len(numbers_list)
end_result = 0
for i in range(3):
    # move current index steps-many times
    for j in range(steps):
        current_index += 1
        if current_index == len(numbers_list):
            current_index = 0
    end_result += numbers_list[current_index]

print(end_result)
