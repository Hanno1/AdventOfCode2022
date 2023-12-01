import math

def preprocessing(data):
    mat = []
    for line in data:
        mat.append(list(line))
    return mat

def elves_positions(mat):
    elves_position = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == '#':
                elves_position.append((row, col))
    return elves_position

def check_adjacent_tiles(row, col, elves_positions):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (row + i, col + j) in elves_positions:
                return False
    return True

def try_moving(row, col, elves_positions, direction):
    if direction == 'N':
        # move north and check if empty
        for c in range(-1, 2):
            if (row - 1, col + c) in elves_positions:
                return 'False', -1
        return row - 1, col
    elif direction == 'S':
        # move south and check if empty
        for c in range(-1, 2):
            if (row + 1, col + c) in elves_positions:
                return 'False', -1
        return row + 1, col
    elif direction == 'W':
        # move west and check if empty
        for r in range(-1, 2):
            if (row + r, col - 1) in elves_positions:
                return 'False', -1
        return row, col - 1
    elif direction == 'E':
        # move east and check if empty
        for r in range(-1, 2):
            if (row + r, col + 1) in elves_positions:
                return 'False', -1
        return row, col + 1
    raise ValueError('Wrong direction')

def first_mvmt(elves_position, directions):
    new_elves_position = []
    for elve_position in elves_position:
        r, c = elve_position
        moved = False
        # check 8 adjacent positions
        # if empty -> dont do anything
        if check_adjacent_tiles(r, c, elves_position):
            moved = True
            new_elves_position.append((r, c))
            continue

        # if occupied -> move in directions
        for direction in directions:
            r_, c_ = try_moving(r, c, elves_position, direction)
            if r_ != 'False':
                moved = True
                new_elves_position.append((r_, c_))
                break
    
        if not moved:
            new_elves_position.append((r, c))
            continue
    # check if elves position is the same as a other elves position
    counter = 0
    for (row, col) in new_elves_position:
        if new_elves_position.count((row, col)) > 1:
            # move all elves back
            duplicated_indizes = [i for i, x in enumerate(new_elves_position) if x == (row, col)]
            for index in duplicated_indizes:
                new_elves_position[index] = elves_position[index]
        counter += 1

    gg = True
    for i, (row, col) in enumerate(new_elves_position):
        orig_pos = elves_position[i]
        if row != orig_pos[0] or col != orig_pos[1]:
            gg = False
            break
    if gg:
        return 'Done'
    
    return new_elves_position

def get_first_answer():
    positions = move(10)
    min_row, max_row, min_col, max_col = math.inf, -math.inf, math.inf, -math.inf
    for (row, col) in positions:
        if row < min_row:
            min_row = row
        if row > max_row:
            max_row = row
        if col < min_col:
            min_col = col
        if col > max_col:
            max_col = col

    print(max_row, min_row, max_col, min_col)
    print(len(positions))
    print(((max_row - min_row + 1) * (max_col - min_col + 1)) - len(positions))

def move(moves):
    with open('input.txt') as f:
        data = f.read().split('\n')

    matrix = preprocessing(data)
    directions = ['N', 'S', 'W', 'E']
    elves_position = elves_positions(matrix)

    for i in range(moves):
        elves_position = first_mvmt(elves_position, directions)
        print("Round", i + 1)
        if elves_position == 'Done':
            print('---' * 20)
            print(f'Round {i + 1}')
            print('Done')
            break
        # change directions
        tmp = directions.pop(0)
        directions.append(tmp)
    return elves_position

move(1200)
# get_first_answer()