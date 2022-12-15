positions = []
beacons = []
with open("input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        new_line = line.split(" ")
        complete_information = []
        for el in new_line:
            if el.__contains__("="):
                complete_information.append(int(el.split("=")[1].replace(",", "").replace(":", "")))
        x_distance_to_beacon = abs(complete_information[0] - complete_information[2])
        y_distance_to_beacon = abs(complete_information[1] - complete_information[3])
        beacons.append([complete_information[3], complete_information[2]])
        positions.append([complete_information[1], complete_information[0], x_distance_to_beacon + y_distance_to_beacon])

# task 1: for special_line in range(2000000,2000001):...
# task 2
for special_line in range(0, 4000000):
    print(special_line)

    special_points = []
    relevant_beacons = []
    for beacon in beacons:
        if beacon[0] == special_line and beacon[1] not in relevant_beacons:
            relevant_beacons.append(beacon[1])

    for sensor in positions:
        current_position = sensor[0]
        width = sensor[2]
        distance = abs(current_position - special_line)
        if distance <= width:
            left_point = sensor[1] - (width - distance)
            right_point = sensor[1] + (width - distance)
            special_points.append([left_point, right_point])

    sorted_points = []
    while special_points:
        mini = special_points[0][0]
        arg_mini = 0
        for point_counter in range(len(special_points)):
            point = special_points[point_counter]
            if point[0] < mini:
                arg_mini = point_counter
                mini = point[0]
        sorted_points.append(special_points[arg_mini])
        special_points.remove(special_points[arg_mini])

    new_intervals = [sorted_points[0]]
    for index in range(1, len(sorted_points)):
        first = new_intervals[-1]
        second = sorted_points[index]
        # first case - second beginning is after first end
        if first[1] + 1 < second[0]:
            new_intervals.append(second)
        # second case - second beginning is smaller then first end but second end is larger then first end
        elif second[0] <= first[1] + 1 <= second[1]:
            new_intervals[-1] = [first[0], second[1]]
        # third and last case - second interval is completely contained in the first
        elif first[0] <= second[1] <= first[1]:
            pass
        else:
            print("Unknown Case!")

    if len(new_intervals) >= 2:
        print(special_line, new_intervals)
        print((new_intervals[1][0] - 1) * 4000000 + special_line)

        # task 2: 2636475 [[-309541, 3129624], [3129626, 4356534]]
        # -> 12518502636475

        break
