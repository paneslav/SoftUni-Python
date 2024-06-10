from collections import deque

player_one_symbol = '*'
player_two_symbol = 'x'

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, + 1),
    (-1, -1),
    (-1, +1),
    (+1, -1),
    (+1, +1)
]

players_turn = deque([(1, player_one_symbol), (2, player_two_symbol)])

rows, cols = 6, 7

board = []

for row in range(rows):
    board.append(['0'] * cols)

print(*board, sep='\n')

while True:

    try:
        column_choice = int(input(f'Player {players_turn[0][0]}, please select a column in the range of 1 to 7: ')) - 1
    except ValueError or IndexError:
        print(f"Please select a valid number in the range of 1 to 7: ")
        continue

    starting_row = 0

    if board[starting_row][column_choice] != '0':
        print(f"This column is full, please select another.")
        continue

    for i in range(rows):
        if i + 1 == rows:
            board[i][column_choice] = players_turn[0][-1]
            break

        if board[i + 1][column_choice] != '0':
            board[i][column_choice] = players_turn[0][-1]
            break

    for row in range(rows):
        for col in range(cols):

            if board[row][col] != players_turn[0][-1]:
                continue

            for direction in directions:
                r, c = row, col
                for _ in range(3):
                    r = r + direction[0]
                    c = c + direction[-1]

                    if not (0 <= r < rows and 0 <= c < cols):
                        break

                    if board[r][c] != players_turn[0][-1]:
                        break
                else:
                    print(f"Winner is player {players_turn[0][0]}!")
                    raise SystemExit

    players_turn.append(players_turn.popleft())

    print(*board, sep='\n')
