matrix = []
size = 6
winning_position = ()
walls = []
traps = []
stunned_players = {}

game_over = False

move_order = input().split(', ')
for player in move_order:
    stunned_players[player] = 0

for row in range(size):
    line = input().split()
    for col in range(size):
        if line[col] == 'T':
            traps.append((row, col))
            continue

        if line[col] == 'E':
            winning_position = (row, col)
            continue

        if line[col] == 'W':
            walls.append((row, col))
    matrix.append(line)

while True:
    player_coordinates = input()
    current_player = move_order.pop(0)
    move_order.append(current_player)
    player_in_queue = move_order[0]

    if stunned_players[current_player] != 0:
        stunned_players[current_player] -= 1
        continue

    row, col = player_coordinates[1:-1].split(', ')

    spot_on_board = matrix[int(row)][int(col)]

    if spot_on_board == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    if spot_on_board == 'T':
        print(f"{current_player} is out of the game! The winner is {player_in_queue}.")
        break

    if spot_on_board == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        stunned_players[current_player] += 1




# print(*matrix, sep='\n')
# print(exit, walls, traps)


