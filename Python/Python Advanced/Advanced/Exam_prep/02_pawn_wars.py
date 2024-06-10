from collections import deque


def check_for_queen_promotion(current_player, white, black):
    if current_player == 'white':
        row = white[0]
        col = white[1]
        if row == 0:
            print(
                f"Game over! {current_player.capitalize()} pawn is promoted to a queen at {board_mapping[col][0]}{board_mapping[row][1]}.")
            return True
    else:
        row = black[0]
        col = black[1]
        if row == 7:
            print(
                f"Game over! {current_player.capitalize()} pawn is promoted to a queen at {board_mapping[col][0]}{board_mapping[row][1]}.")
            return True

    return False


def check_diagonal(current_player, white, black):
    white_row, white_col = white
    black_row, black_col = black

    if white_row - black_row == 1 and abs(white_col - black_col) == 1:
        if current_player == 'white':
            print(
                f"Game over! {current_player.capitalize()} win, capture on {board_mapping[black_col][0]}{board_mapping[black_row][1]}.")
        else:
            print(
                f"Game over! {current_player.capitalize()} win, capture on {board_mapping[white_col][0]}{board_mapping[white_row][1]}.")
        return True


def move_forward(current_player, position):
    if current_player == 'white':
        row = position[0] - 1
        col = position[1]
        return [row, col]
    elif current_player == 'black':
        row = position[0] + 1
        col = position[1]
        return [row, col]


players = deque(['white', 'black'])
board = []
board_mapping = {
    0: ['a', 8],
    1: ['b', 7],
    2: ['c', 6],
    3: ['d', 5],
    4: ['e', 4],
    5: ['f', 3],
    6: ['g', 2],
    7: ['h', 1],
}
white_position = []
black_position = []

for row in range(8):
    col = input().split()

    if 'b' in col:
        black_position = [row, col.index('b')]
    if 'w' in col:
        white_position = [row, col.index('w')]

    board.append(col)

while True:
    current_player = players.popleft()
    if check_diagonal(current_player, white_position, black_position):
        break

    if current_player == 'white':
        white_position = move_forward(current_player, white_position)
    elif current_player == 'black':
        black_position = move_forward(current_player, black_position)

    if check_for_queen_promotion(current_player, white_position, black_position):
        break

    players.append(current_player)
