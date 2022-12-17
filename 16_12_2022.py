import copy

import numpy as np


def compute_distance(source_tmp, destination_tmp):
    if source_tmp == destination_tmp:
        return 0
    path_length = 0
    heads = [source_tmp]
    explored = []
    while True:
        # move all heads in heads
        new_heads = []
        for head in heads:
            # move the head
            for destination in flow_map[head][1]:
                if destination == destination_tmp:
                    return path_length + 1
                elif destination not in explored:
                    new_heads.append(destination)
            explored.append(head)
        path_length += 1
        heads = new_heads


def simulate_probabilistic(simulations=1):
    # probabilistic idea
    max_points = 0
    for simul in range(simulations):
        print(f"Simulation {simul}")

        actual_minute = 0
        current_position = "AA"
        points = 0
        flow_map_copy = copy.deepcopy(flow_map)

        while actual_minute < 30:
            # compute next best point (evaluation)
            current_position_index = all_positions.index(current_position)
            sum_eval = 0
            possible_evals = []
            possible_positions = []
            all_distances = []
            for pos_counter in range(len(all_positions)):
                position = all_positions[pos_counter]
                pressure = flow_map_copy[position][0]
                if pressure == 0:
                    continue
                current_distance = distance_matrix[pos_counter][current_position_index]
                # compute evaluation -> it gives up pressure for 30 min
                # minus the time we have now (actual minutes)
                # minus the distance, since we have to move there
                # minus 1 cause we have to open it
                evaluation = (30 - current_distance - 1 - actual_minute) * pressure
                if evaluation < 0:
                    evaluation = 0
                sum_eval += evaluation
                possible_evals.append(evaluation)
                possible_positions.append(position)
                all_distances.append(current_distance)
            if sum_eval == 0:
                break
            new_possible_evals = []
            for entry in possible_evals:
                new_possible_evals.append(entry / sum_eval)
            if sum_eval > 0:
                new_pos = np.random.choice([i for i in range(len(possible_positions))], p=new_possible_evals)
                max_pos = possible_positions[new_pos]
                max_distance = all_distances[new_pos]
                max_eval = possible_evals[new_pos]
                # print(f"Moved and opened {max_pos}")
                actual_minute += max_distance
                points += max_eval
                current_position = max_pos
                flow_map_copy[max_pos][0] = 0
            actual_minute += 1

        max_points = max(points, max_points)
    return max_points


flow_map = dict()
all_positions = []
with open("input.txt") as file:
    for line in file:
        actual_line = line.replace("\n", "").split(" ")
        source = actual_line[1]
        rate = int(actual_line[4].replace(";", "").split("=")[1])
        destinations = [actual_line[i].replace(",", "") for i in range(9, len(actual_line))]
        flow_map[source] = [rate, destinations]
        all_positions.append(source)

distance_matrix = [[0 for i in range(len(all_positions))] for j in range(len(all_positions))]
for row in range(len(distance_matrix)):
    for col in range(row+1, len(distance_matrix[row])):
        dist = compute_distance(all_positions[row], all_positions[col])
        distance_matrix[row][col] = dist
        distance_matrix[col][row] = dist

# simulate all
# task 1 all_current_paths = [[["AA", count], [], 0, 0]]
# task 2 -> save position of the elephant
# save the current position, as well as the opened positions, and the current minute, as well as the current points
all_current_paths = [[["AA", 0], ["AA", 0], ["AA"], 0]]
max_eval = 0
max_minute = 26
current_minute = 0

max_eval_tmp = 0
offset = 0.3

while all_current_paths:
    print(f"Current Minute: ", current_minute)
    print(f"Path Count: ", len(all_current_paths))
    print(f"Maxi temp: ", max_eval_tmp)

    new_all_current_paths = []
    for path_counter in range(len(all_current_paths)):
        current_me, current_elephant, visited, current_eval = all_current_paths[path_counter]
        current_me_position, current_me_turns = current_me
        current_el_position, current_el_turns = current_elephant

        added = False

        if current_eval < max_eval_tmp * offset:
            continue

        if current_me_turns != 0 and current_el_turns != 0:
            # player and el not ready to move -> subtract one minute
            all_current_paths[path_counter][0][1] -= 1
            all_current_paths[path_counter][1][1] -= 1
            new_all_current_paths.append(all_current_paths[path_counter])
            added = True
            continue

        first_pos_index = all_positions.index(current_me_position)
        second_pos_index = all_positions.index(current_el_position)

        if current_me_turns == 0 and current_el_turns != 0:
            # move player but not the elephant
            for pos_counter in range(len(all_positions)):
                # create new paths
                new_position = all_positions[pos_counter]
                current_distance = distance_matrix[first_pos_index][pos_counter] + 1
                pressure = flow_map[new_position][0]
                evaluation = (max_minute - current_distance - current_minute) * pressure

                if new_position not in visited and evaluation > 0:
                    new_visited = copy.deepcopy(visited)
                    if not new_visited:
                        new_visited = [new_position]
                    else:
                        new_visited.append(new_position)
                    max_eval_tmp = max(max_eval_tmp, current_eval + evaluation)
                    new_all_current_paths.append([[new_position, current_distance - 1],
                                                  [current_el_position, current_el_turns - 1], new_visited,
                                                  current_eval + evaluation])
                    added = True
        elif current_me_turns != 0 and current_el_turns == 0:
            # only move elephant
            for pos_counter in range(len(all_positions)):
                # create new paths
                new_position = all_positions[pos_counter]
                current_distance = distance_matrix[second_pos_index][pos_counter] + 1
                pressure = flow_map[new_position][0]
                evaluation = (max_minute - current_distance - current_minute) * pressure

                if new_position not in visited and evaluation > 0:
                    new_visited = copy.deepcopy(visited)
                    if not new_visited:
                        new_visited = [new_position]
                    else:
                        new_visited.append(new_position)
                    max_eval_tmp = max(max_eval_tmp, current_eval + evaluation)
                    new_all_current_paths.append([[current_me_position, current_me_turns - 1],
                                                  [new_position, current_distance - 1], new_visited,
                                                  current_eval + evaluation])
                    added = True
        else:
            # move both
            # move the player first
            # choose two new positions
            move_me = False
            move_el = False
            for pos_me_counter in range(len(all_positions)):

                # all values for me
                new_me_position = all_positions[pos_me_counter]
                current_me_distance = distance_matrix[first_pos_index][pos_me_counter] + 1
                pressure_me = flow_map[new_me_position][0]
                evaluation_me = (max_minute - current_me_distance - current_minute) * pressure_me

                if new_me_position in visited or evaluation_me <= 0:
                    continue
                move_me = True
                for pos_el_counter in range(len(all_positions)):
                    # all values for the el
                    new_el_position = all_positions[pos_el_counter]
                    current_el_distance = distance_matrix[second_pos_index][pos_el_counter] + 1
                    pressure_el = flow_map[new_el_position][0]
                    evaluation_el = (max_minute - current_el_distance - current_minute) * pressure_el

                    if new_el_position in visited or evaluation_el <= 0:
                        continue
                    move_el = True

                    if new_el_position == new_me_position:
                        new_visited = copy.deepcopy(visited)
                        if not new_visited:
                            new_visited = [new_me_position]
                        else:
                            new_visited.append(new_me_position)
                        if evaluation_me > evaluation_el:
                            max_eval_tmp = max(max_eval_tmp, current_eval + evaluation_me)
                            new_all_current_paths.append([[new_me_position, current_me_distance - 1],
                                                          [current_el_position, 0], new_visited,
                                                          current_eval + evaluation_me])
                        else:
                            max_eval_tmp = max(max_eval_tmp, current_eval + evaluation_el)
                            new_all_current_paths.append([[current_me_position, 0],
                                                          [new_el_position, current_el_distance - 1], new_visited,
                                                          current_eval + evaluation_el])
                    else:
                        new_visited = copy.deepcopy(visited)
                        if not new_visited:
                            new_visited = [new_me_position, new_el_position]
                        else:
                            new_visited.append(new_me_position)
                            new_visited.append(new_el_position)
                        max_eval_tmp = max(max_eval_tmp, current_eval + evaluation_el + evaluation_me)
                        new_all_current_paths.append([[new_me_position, current_me_distance - 1],
                                                      [new_el_position, current_el_distance - 1], new_visited,
                                                      current_eval + evaluation_me + evaluation_el])
                    added = True
            if not move_me:
                # try to move me
                for pos_counter in range(len(all_positions)):
                    # create new paths
                    new_position = all_positions[pos_counter]
                    current_distance = distance_matrix[first_pos_index][pos_counter] + 1
                    pressure = flow_map[new_position][0]
                    evaluation = (max_minute - current_distance - current_minute) * pressure

                    if new_position not in visited and evaluation > 0:
                        new_visited = copy.deepcopy(visited)
                        if not new_visited:
                            new_visited = [new_position]
                        else:
                            new_visited.append(new_position)
                        max_eval_tmp = max(max_eval_tmp, current_eval + evaluation)
                        new_all_current_paths.append([[new_position, current_distance - 1],
                                                      [current_el_position, current_el_turns], new_visited,
                                                      current_eval + evaluation])
                        added = True
            if not move_el:
                # try to move el
                for pos_counter in range(len(all_positions)):
                    # create new paths
                    new_position = all_positions[pos_counter]
                    current_distance = distance_matrix[second_pos_index][pos_counter] + 1
                    pressure = flow_map[new_position][0]
                    evaluation = (max_minute - current_distance - current_minute) * pressure

                    if new_position not in visited and evaluation > 0:
                        new_visited = copy.deepcopy(visited)
                        if not new_visited:
                            new_visited = [new_position]
                        else:
                            new_visited.append(new_position)
                        max_eval_tmp = max(max_eval_tmp, current_eval + evaluation)
                        new_all_current_paths.append([[current_me_position, current_me_turns - 1],
                                                      [new_position, current_distance - 1], new_visited,
                                                      current_eval + evaluation])
                        added = True
        if not added:
            max_eval = max(max_eval, current_eval)
    all_current_paths = new_all_current_paths
    current_minute += 1

# 2135
print(max_eval)
