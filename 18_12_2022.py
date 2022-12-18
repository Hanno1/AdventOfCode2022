import copy
import math

cubes = []
min_x_y_z = [math.inf, math.inf, math.inf]
max_x_y_z = [-1, -1, -1]
with open("input.txt") as file:
    for line in file:
        split_line = line.replace("\n", "").split(",")
        cubes.append([int(i) for i in split_line])

        min_x_y_z = [min(cubes[-1][i], min_x_y_z[i]) for i in range(3)]
        max_x_y_z = [max(cubes[-1][i], max_x_y_z[i]) for i in range(3)]
free_sides = [6 for _ in range(len(cubes))]
print(min_x_y_z)
print(max_x_y_z)

water_start = [i-1 for i in min_x_y_z]


def simulate_water():
    water_list = [water_start]
    water_visited = []
    water_min = [i - 1 for i in min_x_y_z]
    water_max = [i + 1 for i in max_x_y_z]
    while water_list:
        new_water_list = []
        print(f"Length of Water list: {len(water_list)}")
        # simulate water one step -> left, right, up, down, forward, backward
        for water_drop_counter in range(len(water_list)):
            # flow left
            water_drop = copy.deepcopy(water_list[water_drop_counter])
            water_drop[0] -= 1
            if water_drop not in cubes and water_drop not in water_visited and water_drop[0] >= water_min[0]\
                    and water_drop not in new_water_list:
                new_water_list.append(copy.deepcopy(water_drop))
            # flow right
            water_drop[0] += 2
            if water_drop not in cubes and water_drop not in water_visited and water_drop[0] <= water_max[0]\
                    and water_drop not in new_water_list:
                new_water_list.append(copy.deepcopy(water_drop))
            water_drop[0] -= 1
            # flow forward and backward
            water_drop[1] -= 1
            if water_drop not in cubes and water_drop not in water_visited and water_drop[1] >= water_min[1]\
                    and water_drop not in new_water_list:
                new_water_list.append(copy.deepcopy(water_drop))
            water_drop[1] += 2
            if water_drop not in cubes and water_drop not in water_visited and water_drop[1] <= water_max[1]\
                    and water_drop not in new_water_list:
                new_water_list.append(copy.deepcopy(water_drop))
            water_drop[1] -= 1
            # flow up and down
            water_drop[2] -= 1
            if water_drop not in cubes and water_drop not in water_visited and water_drop[2] >= water_min[2]\
                    and water_drop not in new_water_list:
                new_water_list.append(copy.deepcopy(water_drop))
            water_drop[2] += 2
            if water_drop not in cubes and water_drop not in water_visited and water_drop[2] <= water_max[2]\
                    and water_drop not in new_water_list:
                new_water_list.append(copy.deepcopy(water_drop))
            water_drop[2] -= 1
            water_visited.append(copy.deepcopy(water_drop))
        water_list = new_water_list
    # now we know there the water is
    # and we know there the lava is
    # so lets check cubes again
    new_free_sides = [6 for _ in range(len(cubes))]
    for cube_counter in range(len(cubes)):
        check_cube_and_water(cube_counter, water_visited, new_free_sides)
    print(sum(new_free_sides))


def check_cube(cube_index):
    c_x, c_y, c_z = cubes[cube_index]
    for cube_index_2 in range(cube_index + 1, len(cubes)):
        c2_x, c2_y, c2_z = cubes[cube_index_2]
        sum_of_abs = abs(c_x - c2_x) + abs(c_y - c2_y) + abs(c_z - c2_z)
        if sum_of_abs == 1:
            free_sides[cube_index] -= 1
            free_sides[cube_index_2] -= 1


def check_cube_and_water(cube_index, water_list, new_frees):
    c_x, c_y, c_z = cubes[cube_index]
    need_to_explore = [[c_x + i, c_y, c_z] for i in [-1, 1]]
    for i in [-1, 1]:
        need_to_explore.append([c_x, c_y + i, c_z])
    for i in [-1, 1]:
        need_to_explore.append([c_x, c_y, c_z + i])
    for cube_index_2 in range(cube_index + 1, len(cubes)):
        c2_x, c2_y, c2_z = cubes[cube_index_2]
        sum_of_abs = abs(c_x - c2_x) + abs(c_y - c2_y) + abs(c_z - c2_z)
        if sum_of_abs == 1:
            new_frees[cube_index] -= 1
            new_frees[cube_index_2] -= 1
            need_to_explore.remove([c2_x, c2_y, c2_z])
    for el in need_to_explore:
        if el not in water_list and el not in cubes:
            new_frees[cube_index] -= 1


# task 1
"""for cube_counter in range(len(cubes)):
    check_cube(cube_counter)

print(free_sides)
print(sum(free_sides))"""

# task 2
simulate_water()
