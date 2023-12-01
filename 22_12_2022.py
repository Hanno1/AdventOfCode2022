def preprocess(data):
    mat = []
    for line in data:
        mat_line = []
        for char in line:
            mat_line.append(char)
        mat.append(mat_line)
    return mat

def get_positions(mat):
    blizzard_positions = {'left': [], 'right': [], 'top': [], 'bottom': []}
    player_position = set()
    exit_position = None
    for row in range(len(mat)):
        if row == len(mat) - 1:
            for col in range(len(mat[row])):
                if mat[row][col] == '.':
                    exit_position = (row, col)
                    break
        for col in range(len(mat[row])):
            pos = mat[row][col]
            # get player position
            if pos == 'E':
                player_position.add((row, col))
            # get blizzard positions
            if pos == '>':
                blizzard_positions['right'].append((row, col))
            elif pos == '<':
                blizzard_positions['left'].append((row, col))
            elif pos == '^':
                blizzard_positions['top'].append((row, col))
            elif pos == 'v':
                blizzard_positions['bottom'].append((row, col))
    return player_position, exit_position, blizzard_positions

def move_blizzards(mat, player, blizzards):
    row_length = len(mat[0]) - 2
    col_length = len(mat) - 2

    new_blizzards = {'left': [], 'right': [], 'top': [], 'bottom': []}

    left = blizzards['left']
    for blizzard in left:
        row, col = blizzard
        col -= 1
        if mat[row][col] == '#':
            col = row_length
        new_blizzards['left'].append((row, col))
    right = blizzards['right']
    for blizzard in right:
        row, col = blizzard
        col += 1
        if mat[row][col] == '#':
            col = 1
        blizzard = (row, col)
        new_blizzards['right'].append(blizzard)
    top = blizzards['top']
    for blizzard in top:
        row, col = blizzard
        row -= 1
        if mat[row][col] == '#':
            row = col_length
        blizzard = (row, col)
        new_blizzards['top'].append(blizzard)
    bottom = blizzards['bottom']
    for blizzard in bottom:
        row, col = blizzard
        row += 1
        if mat[row][col] == '#':
            row = 1
        blizzard = (row, col)
        new_blizzards['bottom'].append(blizzard)
    return new_blizzards

def move_player(mat, player_pos, exit, blizzards):
    all_blizzards = set()
    for blizzard in blizzards.values():
        for pos in blizzard:
            all_blizzards.add(pos)
    new_player_positions = set()
    for pos in player_pos:
        row, col = pos
        # player stays on tile
        if (row, col) not in all_blizzards:
            new_player_positions.add((row, col))
        # player moves
        # move left
        if (row, col - 1) not in all_blizzards and mat[row][col - 1] != '#':
            new_player_positions.add((row, col - 1))
        # move right
        if (row, col + 1) not in all_blizzards and mat[row][col + 1] != '#':
            new_player_positions.add((row, col + 1))
        # move up
        if (row - 1, col) not in all_blizzards and row - 1 >= 0 and mat[row - 1][col] != '#':
            new_player_positions.add((row - 1, col))
        # move down
        if (row + 1, col) not in all_blizzards and row + 1 <= len(mat) - 1 and mat[row + 1][col] != '#':
            new_player_positions.add((row + 1, col))
    for pos in new_player_positions:
        row, col = pos
        if row == exit[0] and col == exit[1]:
            return 'Done'
    return new_player_positions


with open('input.txt') as f:
    data = f.read().split('\n')

data = preprocess(data)
player, exit, blizzards = get_positions(data)
entrance = list(player)[0]
# print(player, entrance, exit, blizzards)

mins = 0
for i in range(1000):
    blizzards = move_blizzards(data, player, blizzards)
    player = move_player(data, player, exit, blizzards)

    if player == 'Done':
        mins += i + 1
        break

player = set()
player.add((exit[0], exit[1]))
# move back to start
for i in range(1000):
    blizzards = move_blizzards(data, player, blizzards)
    player = move_player(data, player, entrance, blizzards)

    if player == 'Done':
        mins += i + 1
        break

player = set()
player.add((entrance[0], entrance[1]))
# move back
for i in range(1000):
    blizzards = move_blizzards(data, player, blizzards)
    player = move_player(data, player, exit, blizzards)

    if player == 'Done':
        mins += i + 1
        break

print(mins)
