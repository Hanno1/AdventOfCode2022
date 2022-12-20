import copy


def mine_mats(robots_counter_tmp, current_mats_tmp):
    new_mats_tmp = []
    for i in range(4):
        new_mats_tmp.append(current_mats_tmp[i] + robots_counter_tmp[i])
    return new_mats_tmp


blueprints = []
with open("input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        line_split = line.split(".")

        # ore robot
        ore_robot = int(line_split[0].split(" ")[-2])
        # clay robot
        clay_robot = int(line_split[1].split(" ")[-2])
        # obsidian robot
        obsidian_robot = [int(line_split[2].split(" ")[-5]), int(line_split[2].split(" ")[-2])]
        # geode robot
        geode_robot = [int(line_split[3].split(" ")[-5]), int(line_split[3].split(" ")[-2])]

        # add robots to blueprint
        blueprints.append([ore_robot, clay_robot, obsidian_robot, geode_robot])

max_minute = 24
robot_max = 4
bp_counter = 0
quality_lvl = 0
for bp in blueprints:
    bp_counter += 1

    print(f"Blueprint {bp_counter}")

    ore_robot_cost = bp[0]
    clay_robot_cost = bp[1]
    obsidian_robot_cost = bp[2]
    geode_robot_cost = bp[3]

    current_minute = 1

    states_to_be_explored = [[[0, 0, 0, 0], [1, 0, 0, 0]]]
    max_geodes_min = 0

    while current_minute <= max_minute:
        new_states_to_be_explored = []
        print(f"{len(states_to_be_explored)} have to be explored! Minute {current_minute}")
        for state in states_to_be_explored:

            current_mats = state[0]
            current_robots_counter = state[1]

            new_mats = mine_mats(current_robots_counter, current_mats)
            max_geodes_min = max(max_geodes_min, new_mats[-1])

            """if current_minute >= 13 and current_robots_counter[2] < 1:
                continue
            if current_minute >= 17 and current_robots_counter[2] < 2:
                continue
            if max_geodes_min - new_mats[-1] > 1 and current_robots_counter[3] == 0:
                continue"""

            # mine mats
            # try to create new robots
            # try to create geode robot
            if current_mats[0] >= geode_robot_cost[0] and current_mats[2] >= geode_robot_cost[1]:
                # print("Creating Geode Mining Robot!")
                new_mats[0] -= geode_robot_cost[0]
                new_mats[2] -= geode_robot_cost[1]
                current_robots_counter[3] += 1
                new_states_to_be_explored.append([new_mats, current_robots_counter])
                continue
            # try to create a ore robot
            if current_mats[0] >= ore_robot_cost and robot_max > current_robots_counter[0]:
                # print("Creating Ore Robot!")
                mats_tmp = copy.deepcopy(new_mats)
                mats_tmp[0] -= ore_robot_cost
                new_robots_counter = copy.deepcopy(current_robots_counter)
                new_robots_counter[0] += 1
                new_states_to_be_explored.append([mats_tmp, new_robots_counter])
            # try to create clay robot
            if current_mats[0] >= clay_robot_cost and robot_max > current_robots_counter[1]:
                # print("Creating Clay Robot!")
                mats_tmp = copy.deepcopy(new_mats)
                mats_tmp[0] -= clay_robot_cost
                new_robots_counter = copy.deepcopy(current_robots_counter)
                new_robots_counter[1] += 1
                new_states_to_be_explored.append([mats_tmp, new_robots_counter])
            # try to create obsidian robot
            if current_mats[0] >= obsidian_robot_cost[0] and current_mats[1] >= obsidian_robot_cost[1] and \
                    robot_max >= current_robots_counter[2]:
                # print("Creating Obsidian Robot!")
                mats_tmp = copy.deepcopy(new_mats)
                mats_tmp[0] -= obsidian_robot_cost[0]
                mats_tmp[1] -= obsidian_robot_cost[1]

                new_robots_counter = copy.deepcopy(current_robots_counter)
                new_robots_counter[2] += 1
                new_states_to_be_explored.append([mats_tmp, new_robots_counter])

            new_states_to_be_explored.append([new_mats, current_robots_counter])
        states_to_be_explored = new_states_to_be_explored
        current_minute += 1

    max_geodes = 0
    for state in states_to_be_explored:
        max_geodes = max(max_geodes, state[0][-1])

    print(max_geodes)
    print("----------------------------------")

    quality_lvl += max_geodes * bp_counter

# false 578
# false 815
print(quality_lvl)
